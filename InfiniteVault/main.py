# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Aug  2 15:52:07 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1096, 778)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeView = QtWidgets.QTreeView(self.frame)
        self.treeView.setGeometry(QtCore.QRect(20, 2, 711, 621))
        self.treeView.setObjectName("treeView")
        self.createbutton = QtWidgets.QPushButton(self.frame)
        self.createbutton.setGeometry(QtCore.QRect(740, 635, 93, 28))
        self.createbutton.setObjectName("createbutton")
        self.foldername = QtWidgets.QLineEdit(self.frame)
        self.foldername.setGeometry(QtCore.QRect(160, 650, 571, 22))
        self.foldername.setObjectName("foldername")
        self.exitbutton = QtWidgets.QPushButton(self.frame)
        self.exitbutton.setGeometry(QtCore.QRect(840, 635, 93, 28))
        self.exitbutton.setObjectName("exitbutton")
        self.deletebutton = QtWidgets.QPushButton(self.frame)
        self.deletebutton.setGeometry(QtCore.QRect(740, 670, 93, 28))
        self.deletebutton.setObjectName("deletebutton")
        self.logoutbutton = QtWidgets.QPushButton(self.frame)
        self.logoutbutton.setGeometry(QtCore.QRect(840, 670, 93, 28))
        self.logoutbutton.setObjectName("logoutbutton")
        self.searchbutton = QtWidgets.QPushButton(self.frame)
        self.searchbutton.setGeometry(QtCore.QRect(740, 380, 93, 28))
        self.searchbutton.setObjectName("searchbutton")
        self.browsebutton = QtWidgets.QPushButton(self.frame)
        self.browsebutton.setGeometry(QtCore.QRect(740, 110, 93, 28))
        self.browsebutton.setObjectName("browsebutton")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 650, 133, 16))
        self.label.setObjectName("label")
        self.searchlineedit = QtWidgets.QLineEdit(self.frame)
        self.searchlineedit.setGeometry(QtCore.QRect(740, 250, 191, 22))
        self.searchlineedit.setObjectName("searchlineedit")
        self.searchlinelabel = QtWidgets.QLabel(self.frame)
        self.searchlinelabel.setGeometry(QtCore.QRect(740, 220, 171, 16))
        self.searchlinelabel.setObjectName("searchlinelabel")
        self.typeselectlabel = QtWidgets.QLabel(self.frame)
        self.typeselectlabel.setGeometry(QtCore.QRect(740, 310, 171, 16))
        self.typeselectlabel.setObjectName("typeselectlabel")
        self.typeselectcombobox = QtWidgets.QComboBox(self.frame)
        self.typeselectcombobox.setGeometry(QtCore.QRect(740, 340, 191, 22))
        self.typeselectcombobox.setObjectName("typeselectcombobox")
        self.browselineedit = QtWidgets.QLabel(self.frame)
        self.browselineedit.setGeometry(QtCore.QRect(740, 90, 171, 16))
        self.browselineedit.setObjectName("browselineedit")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1096, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DsKDirectRy", None, -1))
        self.createbutton.setText(QtWidgets.QApplication.translate("MainWindow", "Create", None, -1))
        self.exitbutton.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.deletebutton.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.logoutbutton.setText(QtWidgets.QApplication.translate("MainWindow", "Logout", None, -1))
        self.searchbutton.setText(QtWidgets.QApplication.translate("MainWindow", "Search", None, -1))
        self.browsebutton.setText(QtWidgets.QApplication.translate("MainWindow", "Browse", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Enter the folder name", None, -1))
        self.searchlinelabel.setText(QtWidgets.QApplication.translate("MainWindow", "Enter the folder / file name", None, -1))
        self.typeselectlabel.setText(QtWidgets.QApplication.translate("MainWindow", "Select the file type (if known)", None, -1))
        self.browselineedit.setText(QtWidgets.QApplication.translate("MainWindow", "Browse to save the file", None, -1))

