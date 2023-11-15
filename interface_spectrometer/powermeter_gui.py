# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'powermeter_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QLabel, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QWidget)
import graphics.buttons_rc

class Ui_camcom_mainwin(object):
    def setupUi(self, camcom_mainwin):
        if not camcom_mainwin.objectName():
            camcom_mainwin.setObjectName(u"camcom_mainwin")
        camcom_mainwin.setEnabled(True)
        camcom_mainwin.resize(446, 294)
        camcom_mainwin.setStyleSheet(u"button->setStyleSheet(\"border-image:url(:/icons/arrow_l.png);\");")
        self.frame = QFrame(camcom_mainwin)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 441, 281))
        self.frame.setStyleSheet(u"background-color: rgb(50, 49, 52);\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(False)
        self.label.setGeometry(QRect(10, 5, 191, 31))
        self.label.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 40, 791, 51))
        self.frame_2.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.comboBox_camport = QComboBox(self.frame_2)
        self.comboBox_camport.setObjectName(u"comboBox_camport")
        self.comboBox_camport.setGeometry(QRect(100, 15, 71, 22))
        self.comboBox_camport.setStyleSheet(u"color: rgb(220,220,220)\n"
"")
        self.pushButton_comrefresh = QPushButton(self.frame_2)
        self.pushButton_comrefresh.setObjectName(u"pushButton_comrefresh")
        self.pushButton_comrefresh.setGeometry(QRect(180, 10, 101, 31))
        self.pushButton_comrefresh.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.pushButton_comconnect = QPushButton(self.frame_2)
        self.pushButton_comconnect.setObjectName(u"pushButton_comconnect")
        self.pushButton_comconnect.setGeometry(QRect(290, 10, 101, 31))
        self.pushButton_comconnect.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	color: rgb(220,220,220);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(16, 10, 81, 31))
        self.label_4.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 105, 71, 21))
        self.label_14.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.checkBox_autosens = QCheckBox(self.frame)
        self.checkBox_autosens.setObjectName(u"checkBox_autosens")
        self.checkBox_autosens.setGeometry(QRect(320, 101, 51, 31))
        self.checkBox_autosens.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.label_exposure = QLabel(self.frame)
        self.label_exposure.setObjectName(u"label_exposure")
        self.label_exposure.setGeometry(QRect(90, 105, 31, 21))
        self.label_exposure.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(0, 0, 0, 50);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"color: rgb(220,220,220);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_exposure.setAlignment(Qt.AlignCenter)
        self.horizontalSlider_exposure = QSlider(self.frame)
        self.horizontalSlider_exposure.setObjectName(u"horizontalSlider_exposure")
        self.horizontalSlider_exposure.setEnabled(True)
        self.horizontalSlider_exposure.setGeometry(QRect(130, 105, 161, 22))
        self.horizontalSlider_exposure.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid black;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    margin: 2px 0;\n"
"	background: rgba(100, 150, 200,50);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(100,150,200);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.horizontalSlider_exposure.setMinimum(-14)
        self.horizontalSlider_exposure.setMaximum(-4)
        self.horizontalSlider_exposure.setValue(-8)
        self.horizontalSlider_exposure.setSliderPosition(-8)
        self.horizontalSlider_exposure.setOrientation(Qt.Horizontal)
        self.horizontalSlider_exposure.setInvertedAppearance(False)
        self.horizontalSlider_exposure.setInvertedControls(False)
        self.label_status = QLabel(self.frame)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setEnabled(False)
        self.label_status.setGeometry(QRect(140, 5, 231, 31))
        self.label_status.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.label_status.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton_mini = QPushButton(self.frame)
        self.pushButton_mini.setObjectName(u"pushButton_mini")
        self.pushButton_mini.setGeometry(QRect(385, 10, 20, 20))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_mini.setFont(font)
        self.pushButton_mini.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(100,100,100);\n"
"	background-image: url(:/icons/minimize.png);\n"
"	color: white;\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(100, 150, 200);\n"
"	color: white;\n"
"}\n"
"\n"
"")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 140, 451, 151))
        self.frame_3.setStyleSheet(u"border-radius: 0px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.stackedWidget_scopetype = QStackedWidget(self.frame_3)
        self.stackedWidget_scopetype.setObjectName(u"stackedWidget_scopetype")
        self.stackedWidget_scopetype.setGeometry(QRect(0, 0, 441, 141))
        self.stackedWidget_scopetype.setStyleSheet(u"background-color: transparent;")
        self.pageinfo = QWidget()
        self.pageinfo.setObjectName(u"pageinfo")
        self.infolabel = QLabel(self.pageinfo)
        self.infolabel.setObjectName(u"infolabel")
        self.infolabel.setGeometry(QRect(10, -10, 421, 151))
        self.infolabel.setStyleSheet(u"border-radius: 2px;\n"
"background-color: rgba(255, 0, 100, 0);\n"
"border-color: rgba(5, 5, 5, 0);\n"
"border-width: 1px;\n"
"\n"
"")
        self.infolabel.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.stackedWidget_scopetype.addWidget(self.pageinfo)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 5, 411, 121))
        self.frame_4.setStyleSheet(u"border-radius: 5px;\n"
"border: 3px solid rgba(0, 0, 0, 50);\n"
"background-color: rgba(0, 0, 0, 50);\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_value = QLabel(self.frame_4)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setGeometry(QRect(40, 10, 211, 60))
        self.label_value.setStyleSheet(u"font: 50pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_value.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progressBar = QProgressBar(self.frame_4)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 82, 371, 21))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"background-color: rgb(54, 54, 54);\n"
"border: transparent;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0397727 rgba(0, 0, 255, 255), stop:1 rgba(255, 0, 255, 255));\n"
"border: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.progressBar.setMaximum(1023)
        self.progressBar.setValue(1023)
        self.progressBar.setTextVisible(False)
        self.label_unit = QLabel(self.frame_4)
        self.label_unit.setObjectName(u"label_unit")
        self.label_unit.setGeometry(QRect(280, 35, 111, 35))
        self.label_unit.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_unit.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_unit_2 = QLabel(self.frame_4)
        self.label_unit_2.setObjectName(u"label_unit_2")
        self.label_unit_2.setGeometry(QRect(280, 0, 131, 35))
        self.label_unit_2.setStyleSheet(u"font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(100, 150, 200);\n"
"background-color: transparent;\n"
"border: none;\n"
"")
        self.label_unit_2.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.stackedWidget_scopetype.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget_scopetype.addWidget(self.page_5)
        self.pushButton_infobox = QPushButton(self.frame)
        self.pushButton_infobox.setObjectName(u"pushButton_infobox")
        self.pushButton_infobox.setGeometry(QRect(395, 50, 31, 31))
        self.pushButton_infobox.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(90, 90, 90);\n"
"	background-image: url(:/icons/info.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-image: url(:/icons/infob.png);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(130, 180, 230);\n"
"	color: white;\n"
"}")
        self.checkBox_showsensor = QCheckBox(self.frame)
        self.checkBox_showsensor.setObjectName(u"checkBox_showsensor")
        self.checkBox_showsensor.setGeometry(QRect(380, 101, 51, 31))
        self.checkBox_showsensor.setStyleSheet(u"QCheckBox {\n"
"	\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border: none;\n"
"color: rgb(220,220,220);\n"
"font: 8pt \"MS Shell Dlg 2\";\n"
"}")
        self.pushButton_exit = QPushButton(camcom_mainwin)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setGeometry(QRect(410, 20, 20, 20))
        self.pushButton_exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"	background-color: rgb(120,0,0);\n"
"	background-image: url(:/icons/exit.png);\n"
"	color: white;\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"	color: white;\n"
"}\n"
"\n"
"")

        self.retranslateUi(camcom_mainwin)

        self.stackedWidget_scopetype.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(camcom_mainwin)
    # setupUi

    def retranslateUi(self, camcom_mainwin):
        camcom_mainwin.setWindowTitle(QCoreApplication.translate("camcom_mainwin", u"Form", None))
        self.label.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#f0f0f0;\">PowerCam</span></p></body></html>", None))
        self.pushButton_comrefresh.setText(QCoreApplication.translate("camcom_mainwin", u"refresh", None))
        self.pushButton_comconnect.setText(QCoreApplication.translate("camcom_mainwin", u"connect", None))
        self.label_4.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#6496c8;\">camera</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Sensitivity:</span></p></body></html>", None))
        self.checkBox_autosens.setText(QCoreApplication.translate("camcom_mainwin", u"auto", None))
        self.label_exposure.setText(QCoreApplication.translate("camcom_mainwin", u"-10", None))
        self.label_status.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">waiting</span></p></body></html>", None))
        self.pushButton_mini.setText("")
        self.infolabel.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Webcam-Powermeter - PrintedLabs</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Version: 1.0 - 11/14/2023</span></p><p align=\"justify\"><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">Would you like to learn more about PowerCam and get<br/>a tutorial on all implemented functions? You can find this and<br/>much more on our website </span><a href=\"https://printedlabs.uni-bayreuth.de/\"><span style=\" font-size:10pt; font-weight:600; text-decoration: underline; color:#dc0000;\">printedlabs.uni-bayreuth.de</span></a><span style=\" font-size:10pt; font-weight:600; color:#dcdcdc;\">!</span></p></body></html>", None))
        self.label_value.setText(QCoreApplication.translate("camcom_mainwin", u"---,--", None))
        self.label_unit.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p>arb. units</p></body></html>", None))
        self.label_unit_2.setText(QCoreApplication.translate("camcom_mainwin", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">saturation alert!!!</span></p></body></html>", None))
        self.pushButton_infobox.setText("")
        self.checkBox_showsensor.setText(QCoreApplication.translate("camcom_mainwin", u"show", None))
        self.pushButton_exit.setText("")
    # retranslateUi

