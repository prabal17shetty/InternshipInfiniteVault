from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
   def setupUi(self, MainWindow):
       MainWindow.setObjectName("MainWindow")
       MainWindow.resize(492, 431)
       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")
       self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
       self.gridLayout.setObjectName("gridLayout")
       self.frame = QtWidgets.QFrame(self.centralwidget)
       self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
       self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
       self.frame.setObjectName("frame")
       self.reciver_use_id = QtWidgets.QLineEdit(self.frame)
       self.reciver_use_id.setGeometry(QtCore.QRect(20, 330, 241, 31))
       self.reciver_use_id.setObjectName("reciver_use_id")
       self.share_button = QtWidgets.QPushButton(self.frame)
       self.share_button.setGeometry(QtCore.QRect(340, 330, 111, 28))
       self.share_button.setObjectName("share_button")
       self.label = QtWidgets.QLabel(self.frame)
       self.label.setGeometry(QtCore.QRect(20, 310, 181, 16))
       self.label.setObjectName("label")
       self.label_2 = QtWidgets.QLabel(self.frame)
       self.label_2.setGeometry(QtCore.QRect(20, 10, 251, 16))
       self.label_2.setObjectName("label_2")
       self.listWidget = QtWidgets.QListWidget(self.frame)
       self.listWidget.setGeometry(QtCore.QRect(15, 31, 451, 261))
       self.listWidget.setObjectName("listWidget")

       self.listWidget.setAlternatingRowColors(True)
       self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)



       self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
       MainWindow.setCentralWidget(self.centralwidget)
       self.statusbar = QtWidgets.QStatusBar(MainWindow)
       self.statusbar.setObjectName("statusbar")
       MainWindow.setStatusBar(self.statusbar)

       self.retranslateUi(MainWindow)
       QtCore.QMetaObject.connectSlotsByName(MainWindow)

   def retranslateUi(self, MainWindow):
       MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
       self.share_button.setText(QtWidgets.QApplication.translate("MainWindow", "SHARE", None, -1))
       self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Enter  user-id", None, -1))
       self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Select user-id/enter user_id below", None, -1))