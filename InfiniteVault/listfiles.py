from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
   def setupUi(self, MainWindow):
       MainWindow.setObjectName("MainWindow")
       MainWindow.resize(800, 600)
       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")
       self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
       self.gridLayout.setObjectName("gridLayout")
       self.frame = QtWidgets.QFrame(self.centralwidget)
       self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
       self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
       self.frame.setObjectName("frame")
       self.listWidget = QtWidgets.QListWidget(self.frame)
       self.listWidget.setGeometry(QtCore.QRect(0, 30, 771, 501))
       self.listWidget.setObjectName("listWidget")


       self.listWidget.setAlternatingRowColors(True)
       self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)

       self.show_result_btn = QtWidgets.QPushButton(self.frame)
       self.show_result_btn.setGeometry(QtCore.QRect(350, 540, 111, 28))
       self.show_result_btn.setObjectName("show_result_btn")
       self.label = QtWidgets.QLabel(self.frame)
       self.label.setGeometry(QtCore.QRect(200, 0, 411, 31))
       self.label.setObjectName("label")
       self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
       MainWindow.setCentralWidget(self.centralwidget)
       self.retranslateUi(MainWindow)
       QtCore.QMetaObject.connectSlotsByName(MainWindow)

   def retranslateUi(self, MainWindow):
       MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DsKDirectRy", None, -1))
       self.show_result_btn.setText(QtWidgets.QApplication.translate("MainWindow", "View ", None, -1))
       #self.file_open_btn.setText(QtWidgets.QApplication.translate("MainWindow", "OPEN", None, -1))
       self.label.setText(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Click on view button to see the search results</span></p></body></html>", None, -1))

