##############################################################################################################################################
# 
# printedLABs - Webcam Powermeter
# 
# 
# Thorsten Schumacher 
# University of Bayreuth - Germany
# Thorsten.Schumacher@uni-bayreuth.de
# Version 1.0
#                                                                               
#
##############################################################################################################################################


# import relevant external modules
import cv2
from numpy import sum as npsum
from numpy import max as npmax
import sys
import time
import nest_asyncio # get rid of async warnings (event loop issue)
nest_asyncio.apply() 

from threading import Thread
from PySide6.QtWidgets import QMainWindow, QApplication
import PySide6.QtCore as qtc
from PySide6.QtGui import QIcon

# import own modules and gui
from interface_spectrometer.powermeter_gui import Ui_camcom_mainwin
from interface_spectrometer.Workerclass import CamreadWorker, LivecamWorker, Camconnect


################## class for status messages #####################
class Statusemitter(qtc.QObject):
    messagesignal = qtc.Signal(str)

    def sendmessage(self, mymessage)    :
        self.messagesignal.emit(mymessage)

##############################################################################################################################################
#                                                          MAIN WINDOW                                                                       #
##############################################################################################################################################
# to create single exe incl. icon (e.g. TaskManager ...) use in pyintaller ....  "pyinstaller --onefile --noconsole --icon=confs/SWicon.png PowerCam.py"


class Powerwin(QMainWindow):
    
     ## initializing stuff when class is called ... all for/inside GUI
    def __init__(self, interfacenum, parentwin, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # stuff for window
        self.ui =  Ui_camcom_mainwin()
        self.ui.setupUi(self)
        self.interfacennr = interfacenum
        self.setWindowFlags(self.windowFlags() | qtc.Qt.WindowStaysOnTopHint) #keep control panel on top
        self.setWindowFlag(qtc.Qt.FramelessWindowHint) ## we dont want to see the window frame
        self.setAttribute(qtc.Qt.WA_TranslucentBackground) ## we dont want to see the window frame
        self.ui.label_status.setStyleSheet("color:#ff0000; background-color: transparent; border-color: transparent; font-size: 12pt") ## to keep the format
        self.ui.label.setStyleSheet("color: rgb(240,240,240); font-weight: bold; background-color: transparent; border-color: transparent; font-size: 14pt") ## to keep the format
        self.parentwin = parentwin # here we have the parent window (experimental control)
        self.setWindowIcon(QIcon('confs/SWicon.png'))  # use this icon on the OS
        self.setWindowTitle("Camer-Powermeter - PrintedLabs")  # this is the Frame Title (shown as WindowName in OS)
        self.ui.frame.setFixedHeight(291)
        self.move(self.parentwin.intwinpos[0], self.parentwin.intwinpos[1]) # move the window to its position
        self.parentwin.intwinpos[1] += 286  #   store in parent window the position for the next interface window
        self.ui.label_unit_2.setVisible(False)  # start without saturation warning ... will be updated permanently, when cam is running
        self.ui.infolabel.setOpenExternalLinks(True) # we allow external links from the infobox to reach printedlabs website
        self.ui.stackedWidget_scopetype.setCurrentIndex(1) # we start with the powermeter window
        self.show() # show main window

        # available sources (IDs) for cv2
        self.camindexfound = ["0"] #we start with one source
        self.ui.comboBox_camport.addItems(self.camindexfound)
        self.integralvalue = 255 # this is the integrated value of a frame ...
        self.resolutiondesired = [2*1920, 2*1080] # this is the desired resolution we are working with ... 
        self.resolution = [2*1920, 2*1080] # self.resolution will be overwritten when cam is connected and readout
        self.frameBW = 0 # we need the variable, will be overwritten
        self.satvalue = 0 # this is the max value in the whole image
        self.satalert = 240 # max value when we start the saturation alert or do auto exposure reduction

        # start an update thread for reading the camera if available and define Flags for the code
        self.threadpool = qtc.QThreadPool()
        self.runcam = False       # Flag for grabbing frames
        self.showlivecam = False   # Flag to check if live image is shown ... required to interrupt image loop
        self.infoopen = False # Flag if infobox is shown
        self.autoexp = False # set the Flag for autoexposure mode
        self.bartimer = qtc.QTimer(self) # updated for progress / powerbar
        self.bartimer.timeout.connect(self.updateprograssbar) # link to function


       # prepare statusmessage signal - connection 
        self.messageemitter = Statusemitter()           # create an Object for signal emission containing the signal send function
        self.messageemitter.messagesignal.connect(self.statusmessage) # this will be the target function of our signal

        
        ## setup calibration and stuff
        self.setexposuretime() # to update slider and labels
   
    ########################################## UI buttons ####################################################
        
        # general stuff
        self.ui.pushButton_comrefresh.clicked.connect(self.scancam)
        self.ui.pushButton_comconnect.clicked.connect(self.launchcamconnect) # later we open worker thread launch.....
        self.ui.pushButton_exit.clicked.connect(self.closeSW)
        self.ui.pushButton_infobox.clicked.connect(self.showinfobox)
        self.ui.pushButton_mini.clicked.connect(self.minimizeSC)

        #camcontrol
        self.ui.horizontalSlider_exposure.valueChanged.connect(self.setexposuretime)
        self.ui.checkBox_showsensor.clicked.connect(self.livecamview)
        self.ui.checkBox_autosens.clicked.connect(self.autoexposure)


   
    ####################################### move frameless window ############################################
    
    def mousePressEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.oldPos = globalPos

    def mouseMoveEvent(self, event):
        p = event.globalPosition()
        globalPos = p.toPoint()
        delta = qtc.QPoint(globalPos - self.oldPos) 
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = globalPos

    ###################################### general functions ##################################################

    def minimizeSC(self):
        self.showMinimized() # minimize control panel
        if self.showlivecam == True:
            self.livecamview() # we click the button and liveview ends

    def statusmessage(self, text):          # writes a message to the status label and resets it after 3000ms
        self.ui.label_status.setText(text)  # the message is set
        self.ui.label_status.repaint()      # label updated
        qtc.QTimer.singleShot(3000, self.resetstatus)   #after 3000ms we call the resetstatus function that writes "waiting" again

    def resetstatus(self):  # resets the status label to waiting
        self.ui.label_status.setText("waiting")
    
    def closeSW(self):
        self.runcam = False         # set flag to interrupt frame grabbing
        self.showlivecam = False    # set flag to interrubt liveview

        time.sleep(0.5)             # wait some time to stop the threads
        try:
            self.mycam.release()    # try to close the cam connection (if no cam is connected its also fine)
        except:
            pass
        self.close()                # close UI

    def showinfobox(self):
        if self.infoopen:
            self.ui.frame.setFixedHeight(291)
            self.ui.stackedWidget_scopetype.setCurrentIndex(1)
            self.infoopen = False
            self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 0)) # set to unactivated mode
        else:
            self.ui.stackedWidget_scopetype.setCurrentIndex(0)
            self.ui.frame.setFixedHeight(421)
            self.infoopen = True
            self.ui.pushButton_infobox.setStyleSheet(u""+ self.buttonstyle("info.png", "infob.png", 1)) # set to activated mode


    def buttonstyle(self, image, imagehover, pressmode): # image is the image button of the style, pressmode: 0 = set to unactivated, 1 = set to activated mode
        if pressmode == 1:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(100, 150, 200);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        if pressmode == 0:
            stylecode = "QPushButton {\n border: none;\n border-radius: 0px;\n	background-color: rgb(90, 90, 90);\n	background-image: url(:/icons/"+ image +");\n	color: white;\n}\n \n QPushButton:hover {\n	background-image: url(:/icons/"+ imagehover +");\n	color: white;\n}\n \n QPushButton:pressed {\n background-color: rgb(130, 180, 230);\n color: white;\n}"
        return stylecode
    
 
    
###################################### camera readout and interface #########################################

    def returnCameraIndexes(self): # this function searches the first "ports" for an camera and stores the found ids
        
                # checks the first 10 indexes.
        index = 0
        camindexfound = []

        while True:
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Use cv2.CAP_DSHOW for Windows

            if not cap.isOpened(): # we are done if no furter camera is found
                break

            _, frame = cap.read()  # Read a frame to check if the camera is working

            if frame is not None: # we find out if there is a frame
                camindexfound.append(str(index)) # the we add the camera as camera
            
            cap.release() # release the cam
            index += 1 # and go to next index

        # finally we update the combobox and store the result in the object
        self.ui.comboBox_camport.clear()    
        self.ui.comboBox_camport.addItems(camindexfound)  
        self.camindexfound = camindexfound
        self.ui.comboBox_camport.setEnabled(True) # we disable the combobox so that nobody can press it while scanning
        self.ui.pushButton_comconnect.setEnabled(True) # enable connect and refresh buttons again
        self.ui.pushButton_comrefresh.setEnabled(True) # enable connect and refresh buttons again

        self.resetstatus() # we are done scanning what propably takes longer than 3 seconds

    def scancam(self):  # we start scanning available camera sources within a thread .. so that nothing freezes
        # scanning can take a long time .. so we keep the status on "scanning"
        self.ui.comboBox_camport.setDisabled(True) # we disable the combobox so that nobody can press it while scanning
        self.ui.pushButton_comconnect.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled after scan again
        self.ui.pushButton_comrefresh.setDisabled(True) # dont push the button before cameras are scanned .. will be enabled after scan again
        self.ui.label_status.setText("scanning camera sources") # set text to scanning
        self.ui.label_status.repaint()
        # we start a thread doing the work and scanning
        scanthread = Thread(target = self.returnCameraIndexes, args=()) 
        scanthread.start()

    def connect2cam(self):
        if self.ui.pushButton_comconnect.text() == "connect": # in case we are not connected but want to
            self.ui.pushButton_comconnect.setDisabled(True) # set buttons and menu disabled to avoid starting a second process
            self.ui.pushButton_comrefresh.setDisabled(True)
            self.ui.comboBox_camport.setDisabled(True)
            self.messageemitter.sendmessage("connecting to camera")
            
            # open camera
            self.mycam = cv2.VideoCapture(int(self.ui.comboBox_camport.currentText()), cv2.CAP_DSHOW)  # , cv2.CAP_MSMF is suggested backend but also default, cv2.CAP_DSHOW comes from chatGPT
            
            self.ui.pushButton_comconnect.setText("disconnect")
            if self.mycam.isOpened():
                self.mycam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
                self.mycam.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolutiondesired[0])
                self.mycam.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolutiondesired[1])
                self.mycam.set(cv2.CAP_PROP_AUTO_WB, 0.75) # thies deactivates white balance
                self.mycam.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25) # deactivates auto exposure
                self.mycam.set(cv2.CAP_PROP_FPS, 30)

                #  since we can only wish a resultion but that depends on the hardware lets see what we got and store it
                self.resolution[1] = int(self.mycam.get(cv2.CAP_PROP_FRAME_HEIGHT))
                self.resolution[0] = int(self.mycam.get(cv2.CAP_PROP_FRAME_WIDTH))
               

                # now we set the camera parameter for the first time
                self.runcam = True  # we set the flag! and afterwards we update the set cam parameter
                self.setexposuretime() # to update slider and labels

                # now start reading the cam in a separate thread
                self.camreadworker = CamreadWorker(self)
                self.ui.pushButton_comconnect.setEnabled(True)
                self.threadpool.start(self.camreadworker)   # run camera thread
                self.messageemitter.sendmessage("camera connected") # and send status
            else:
                self.messageemitter.sendmessage('failed')
                # and set all buttons enabled
                self.ui.pushButton_comconnect.setEnabled(True)
                self.ui.pushButton_comrefresh.setEnabled(True)
                self.ui.comboBox_camport.setEnabled(True)
                self.ui.pushButton_comconnect.setText("connect")

        else: # in case we want to disconnect
         
            self.runcam = False # stop loop 
            time.sleep(0.25) # and give it some time before we release the camera
            
            # reset UI buttons      
            self.ui.pushButton_comconnect.setText("connect")
            self.ui.pushButton_comconnect.setEnabled(True)
            self.ui.pushButton_comrefresh.setEnabled(True)
            self.ui.comboBox_camport.setEnabled(True)
            self.messageemitter.sendmessage("disconnected from camera")
            
            # release camera after everything else is done
            self.mycam.release()


    def launchcamconnect(self):
        # if there is a camera in the list
        if self.ui.comboBox_camport.currentIndex() >= 0:
            self.camlaunchworker = Camconnect(self)
            self.threadpool.start(self.camlaunchworker)
            self.bartimer.start(250) #update the powerbar every 250 ms
                       
        else:
            self.statusmessage("no camera port")


    def camreadupdate(self):       
        # now we start reading
        while self.runcam == True:
   
            self.rval, self.framelive = self.mycam.read()
            Npixel = (self.resolution[0]*self.resolution[1])
            self.integralvalue = npsum(self.frameBW)/Npixel
            # now show the results
            self.ui.label_value.setText("{:.2f}".format(self.integralvalue))
            
            # in any case, we need grayscale for the spectrometer mode
            self.frameBW = cv2.cvtColor(self.framelive, cv2.COLOR_BGR2GRAY)   #convert it into grayscale (Y←0.299⋅R+0.587⋅G+0.114⋅B)
            self.saturated()
            if self.autoexp:
                if self.satvalue > self.satalert:
                    self.ui.horizontalSlider_exposure.setValue(self.ui.horizontalSlider_exposure.value() - 1)
                    self.setexposuretime()


    def updateprograssbar(self):
        self.ui.progressBar.setValue(int(self.integralvalue/255*1023))
        if self.satvalue > self.satalert:
            self.ui.label_unit_2.setVisible(True)
        else:
            self.ui.label_unit_2.setVisible(False)
        
        self.ui.progressBar.repaint()
        self.ui.label_unit_2.repaint()

    def setexposuretime(self):  # update exposure time
        self.ui.label_exposure.setText(str(self.ui.horizontalSlider_exposure.value()))
        if self.runcam == True:
            self.mycam.set(cv2.CAP_PROP_EXPOSURE, self.ui.horizontalSlider_exposure.value())

    
    def autoexposure(self):
        if self.autoexp:
            self.autoexp = False
            self.ui.horizontalSlider_exposure.setVisible(True)
        else:
            self.autoexp = True
            self.ui.horizontalSlider_exposure.setVisible(False)

            
    def saturated(self):
        self.satvalue = npmax(self.frameBW)
        



       
####################################################################### liveview ##############################################################
 
    def livecamview(self):
        if self.runcam == True:
            if self.showlivecam == False:
                self.showlivecam = True                          # we set the Flag and allow livecam view ... for the while loop in setupHW
                self.liveviewworker = LivecamWorker(self)               # and start the worker
                self.threadpool.start(self.liveviewworker)
                self.ui.checkBox_showsensor.setChecked(True)
            else:
                self.showlivecam = False

        else:
            self.statusmessage("no camera connected")
            self.ui.checkBox_showsensor.setChecked(False)


    def setupHW(self):
        self.LVwindow_name = "camera view"
        
        # we prepare the window for full frame image ... to adjust
        cv2.namedWindow(self.LVwindow_name, cv2.WINDOW_GUI_NORMAL)
        cv2.resizeWindow(self.LVwindow_name, 420, int(420 * self.resolution[1]/self.resolution[0])) # size is hard-coded since the window size is fixed
        
        while self.showlivecam == True:    #  interrupt is set by settings live view button
            currpos = self.pos()
            cv2.moveWindow(self.LVwindow_name, currpos.x(), currpos.y() + 281-20)


            # option show image data
            frame = self.frameBW  # we want the whole thing


            cv2.imshow(self.LVwindow_name, frame) # we update the plot    
            key = cv2.waitKey(10) # is needed otherwise the image is not updated ... it needs some time
        
            # ways out of that loop and to finish the software in camera mode
            if key == 27:  # ways to finish the loop
                break
            

        cv2.destroyWindow(self.LVwindow_name)   # finally we close the window 


    ###################################################### Calibration ############################################################################
    

class WindowCom(qtc.QObject):   # we use this to transfer data between windows
    signal = qtc.Signal(object)


class Fakeparentwin():
    def __init__(self):
        self.intwinpos = [100, 10]


##  start gui
if __name__ == "__main__":
    app = QApplication(sys.argv)              # define Qapplication Object
    fakeparentwin = Fakeparentwin()           # that everything is fine for printedLAB Labcontrol  
    experimentUI = Powerwin(0,fakeparentwin)       # define User interface
    app.exec()                                      # execute
    sys.exit(print("code finished"))                # exit code