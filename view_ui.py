# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt, QSize
class View_ui(QLabel):

    def __init__(self, MainWindow, controller):
        
        QLabel.__init__(self, MainWindow)
        self.MainWindow = MainWindow
        self.controller = controller 
        self.setupUi()

    def setupUi(self):
        MainWindow = self.MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 653)
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
        self.pushButton_gps.clicked.connect(self.MainWindow.set_gps)
        self.pushButton_gps.setStyleSheet('background-color: rgb(255, 255, 255);')


        #Rot sx
        self.pushButton_rotL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotL.setGeometry(QtCore.QRect(10, 560, 111, 41))
        self.pushButton_rotL.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotL.setIcon(icon)
        self.pushButton_rotL.setObjectName("pushButton_rotL")
        self.pushButton_rotL.clicked.connect(self.MainWindow.rotate_left)
        self.gridLayout.addWidget(self.pushButton_rotL, 1, 0, 1, 1)
        self.pushButton_rotL.setShortcut('q')
        self.pushButton_rotL.setStyleSheet('background-color: rgb(255, 255, 255);')


        #Rot dx
        self.pushButton_rotR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotR.setGeometry(QtCore.QRect(130, 560, 111, 41))
        self.pushButton_rotR.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/arrow-left2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotR.setIcon(icon1)
        self.pushButton_rotR.setObjectName("pushButton_rotR")
        self.pushButton_rotR.clicked.connect(self.MainWindow.rotate_right)
        self.gridLayout.addWidget(self.pushButton_rotR, 1, 1, 1, 1)
        self.pushButton_rotR.setShortcut('w')
        self.pushButton_rotR.setStyleSheet('background-color: rgb(255, 255, 255);')


        #-> dx
        self.pushButton_R = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_R.setGeometry(QtCore.QRect(250, 560, 111, 41))
        self.pushButton_R.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/right-arrow2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_R.setIcon(icon2)
        self.pushButton_R.setObjectName("pushButton_4")
        self.pushButton_R.clicked.connect(MainWindow.left)
        self.pushButton_R.setShortcut('left')
        self.pushButton_R.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.gridLayout.addWidget(self.pushButton_R, 1, 2, 1, 1)

        #<- sx
        self.pushButton_L = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_L.setGeometry(QtCore.QRect(370, 560, 111, 41))
        self.pushButton_L.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_L.setIcon(icon3)
        self.pushButton_L.setObjectName("pushButton_5")
        self.pushButton_L.clicked.connect(MainWindow.right)
        self.pushButton_L.setShortcut('right')
        self.pushButton_L.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.gridLayout.addWidget(self.pushButton_L, 1, 3, 1, 1)

        #Tab with all Data
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
        self.label_image.setAlignment(Qt.AlignCenter)
         # Rescaling
        self.label_image.setScaledContents(False)
        self.label_image.setMinimumSize(300, 300)
        self.label_image.setSizePolicy(
        QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
    

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        #self.menubar.setStyleSheet('background-color: #95B5D9')
        self.menu.setStyleSheet('background-color: rgb(255, 255, 255);')

        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApri = QtWidgets.QAction(MainWindow)
        self.actionApri.setObjectName("actionApri")
        
        self.menu.addSeparator()
        self.menu.addAction(self.actionApri)
        self.menubar.addAction(self.menu.menuAction())
       
        self.retranslateUi(MainWindow)
        self.tabWidgetInf.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_gps, self.pushButton_rotL)
        MainWindow.setTabOrder(self.pushButton_rotL, self.pushButton_rotR)
        MainWindow.setTabOrder(self.pushButton_rotR, self.pushButton_R)
        MainWindow.setTabOrder(self.pushButton_R, self.pushButton_L)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_gps.setText(_translate("MainWindow", "GPS"))        

        self.menu.setTitle(_translate("MainWindow", "Menu"))
        self.actionApri.setText(_translate("MainWindow", "Apri"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

