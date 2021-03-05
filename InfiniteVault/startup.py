# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startup.ui',
# licensing of 'startup.ui' applies.
#
# Created: Thu Jul 25 11:31:22 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(12, 12, 1000, 800))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.move(-12,0)


        self.pixmap=QtGui.QPixmap("C:/Users/Prabal Shetty/PycharmProjects/InternshipP1/Startup.png")
        self.label.setPixmap(self.pixmap)
        self.nextbutton = QtWidgets.QPushButton(self.frame)
        self.nextbutton.setGeometry(QtCore.QRect(880, 710, 93, 28))
        self.nextbutton.setObjectName("nextbutton")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DsKDirectRy", None, -1))
        self.nextbutton.setText(QtWidgets.QApplication.translate("MainWindow", "NEXT", None, -1))

