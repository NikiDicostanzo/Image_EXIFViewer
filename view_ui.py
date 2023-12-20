# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout

class View_ui(QLabel):

    def __init__(self, MainWindow, controller):
        
        QLabel.__init__(self, MainWindow)
        self.MainWindow = MainWindow
        self.controller = controller ##
        self.setupUi()

    def setupUi(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 603)
        MainWindow.setStyleSheet("background-color: rgb(229, 241, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

         #--
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton_gps = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_gps.setGeometry(QtCore.QRect(710, 560, 111, 41))
        self.pushButton_gps.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton_gps, 1, 7, 1, 1)

        #Rot sx
        self.pushButton_rotL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotL.setGeometry(QtCore.QRect(10, 560, 111, 41))
        self.pushButton_rotL.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotL.setIcon(icon)
        self.pushButton_rotL.setObjectName("pushButton_rotL")
        self.gridLayout.addWidget(self.pushButton_rotL, 1, 0, 1, 1)

        #Rot dx
        self.pushButton_rotR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotR.setGeometry(QtCore.QRect(130, 560, 111, 41))
        self.pushButton_rotR.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/arrow-left2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotR.setIcon(icon1)
        self.pushButton_rotR.setObjectName("pushButton_rotR")
        self.gridLayout.addWidget(self.pushButton_rotR, 1, 1, 1, 1)

        #-> dx
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 560, 111, 41))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/right-arrow2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)

        #<- sx
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 560, 111, 41))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 3, 1, 1)

        self.tabWidgetInf = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetInf.setGeometry(QtCore.QRect(450, 30, 391, 811))
        self.tabWidgetInf.setStyleSheet("background-color: rgb(237, 255, 254);")
        self.tabWidgetInf.setObjectName("tabWidgetInf")
        self.gridLayout.addWidget(self.tabWidgetInf, 0, 5, 1, 3)

        #My image in window
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(10, 30, 431, 501))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 22))
        self.menubar.setObjectName("menubar")
        self.menuprova = QtWidgets.QMenu(self.menubar)
        self.menuprova.setObjectName("menuprova")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApri = QtWidgets.QAction(MainWindow)
        self.actionApri.setObjectName("actionApri")

        self.menuprova.addSeparator()
        self.menuprova.addAction(self.actionApri)
        self.menubar.addAction(self.menuprova.menuAction())
       
        self.retranslateUi(MainWindow)
        self.tabWidgetInf.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_gps, self.pushButton_rotL)
        MainWindow.setTabOrder(self.pushButton_rotL, self.pushButton_rotR)
        MainWindow.setTabOrder(self.pushButton_rotR, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_gps.setText(_translate("MainWindow", "GPS"))        

        self.menuprova.setTitle(_translate("MainWindow", "prova"))
        self.actionApri.setText(_translate("MainWindow", "Apri"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

