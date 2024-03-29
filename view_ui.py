# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt, QSize

#helps in setting up the UI components
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
        self.pushButton_gps.setStyleSheet('QPushButton{background-color: rgb(255, 255, 255); font:bold;}')

        #Rot sx
        self.pushButton_rotL = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotL.setGeometry(QtCore.QRect(10, 560, 111, 41))
        self.pushButton_rotL.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/arrow-leftR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotL.setIcon(icon)
        self.pushButton_rotL.setObjectName("pushButton_rotL")
        self.pushButton_rotL.clicked.connect(MainWindow.rotate_left)
        self.gridLayout.addWidget(self.pushButton_rotL, 1, 0, 1, 1)
        self.pushButton_rotL.setShortcut('q')
        self.pushButton_rotL.setStyleSheet('background-color: rgb(255, 255, 255);')

        #Rot dx
        self.pushButton_rotR = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rotR.setGeometry(QtCore.QRect(130, 560, 111, 41))
        self.pushButton_rotR.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/arrow-rightR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_rotR.setIcon(icon1)
        self.pushButton_rotR.setObjectName("pushButton_rotR")
        self.pushButton_rotR.clicked.connect(MainWindow.rotate_right)
        self.gridLayout.addWidget(self.pushButton_rotR, 1, 1, 1, 1)
        self.pushButton_rotR.setShortcut('w')
        self.pushButton_rotR.setStyleSheet('background-color: rgb(255, 255, 255);')

        #<- sx
        self.pushButton_L = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_L.setGeometry(QtCore.QRect(250, 560, 111, 41))
        self.pushButton_L.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_L.setIcon(icon2)
        self.pushButton_L.setObjectName("pushButton_L")
        self.pushButton_L.clicked.connect(MainWindow.left)
        self.pushButton_L.setShortcut('left')
        self.pushButton_L.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.gridLayout.addWidget(self.pushButton_L, 1, 2, 1, 1)

        #-> dx
        self.pushButton_R = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_R.setGeometry(QtCore.QRect(370, 560, 111, 41))
        self.pushButton_R.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_R.setIcon(icon3)
        self.pushButton_R.setObjectName("pushButton_R")
        self.pushButton_R.clicked.connect(MainWindow.right)
        self.pushButton_R.setShortcut('right')
        self.pushButton_R.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.gridLayout.addWidget(self.pushButton_R, 1, 3, 1, 1)

        #Tab with all Data
        self.tabWidgetInf = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetInf.setGeometry(QtCore.QRect(450, 30, 391, 811))
        self.tabWidgetInf.setObjectName("tabWidgetInf")
        self.tabWidgetInf.setMinimumSize(301, 101)
        self.gridLayout.addWidget(self.tabWidgetInf, 0, 5, 1, 3)
        self.tabWidgetInf.setStyleSheet(  
                            "QWidget{background-color:rgb(255, 255, 255);}"
                            "QTreeView{ background-color:  rgb(250, 255, 255);   \n"
                            "   border: 1px solid;}\n"
                            "QTreeView::branch{ \n"
                            "    border-bottom: 1px solid rgb(210, 210, 210);}\n"
                            "QTreeView::branch:closed:has-children {\n"
                            "    border-image: none;\n"
                            "    image: url(icons/tree_item_close.png);\n"
                            "    padding:5px;}                          \n"
                            "QTreeView::branch:open:has-children {\n"
                            "    border-image: none;\n"
                            "    image: url(icons/tree_item_open.png);\n"
                            "    padding:5px;}\n"
                            "QTreeWidget::item {\n"
                            "   color:black; border-bottom: 1px solid rgb(216, 216, 216);}\n"
                            "QTreeWidget{ background: rgb(237, 255, 254)}\n"
                            "QHeaderView::section {          \n"
                            "    padding: 2px;               \n"
                            "    border: 0px solid;  \n"
                            "    background: rgb(200, 220, 240);        \n"
                            "    font: bold}                             \n"
                            "QLabel{background: rgb(237, 255, 254); border: 1px solid; font: italic 20px;}\n"
                            "QScrollBar:vertical { background: #84bde0; border-radius: 0px;}\n")
        
        #My image in window
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(10, 30, 431, 501))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 4)
        self.label_image.setAlignment(Qt.AlignCenter)
         # Rescaling
        self.label_image.setScaledContents(False)
        self.label_image.setMinimumSize(300, 300) # min size when window is resized 
        self.label_image.setSizePolicy(QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding) # 

        # Bar with Menu that contains "Open"
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 22))
        self.menubar.setObjectName("menubar")
        self.menubar.setStyleSheet('QMenuBar{ font: bold; border-bottom:2px solid #96AED0;}\n'
                                   ' QMenuBar::item { \n'
                                   ' border-right: 1px solid #96AED0;\n'
                                   ' padding: 7px; padding-left:18px; padding-right:18px}'
                                   ' QMenuBar::item::selected { background: rgb(200, 220, 240)}')
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu.setStyleSheet('QMenu{ background-color: rgb(255, 255, 255);width:140px; height:36; font: bold; border-left:1px solid} \n'
                                'QMenu::item::selected {color:rgb(200, 220, 240);}')
        # Open image
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApri = QtWidgets.QAction(MainWindow)
        self.actionApri.setObjectName("actionApri")
        self.actionApri.triggered.connect(MainWindow.add_image) 
        
        self.menu.addSeparator()
        self.menu.addAction(self.actionApri) # In future add other actions 
        self.menubar.addAction(self.menu.menuAction())
       
        self.retranslateUi(MainWindow)
        self.tabWidgetInf.setCurrentIndex(0) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_gps, self.pushButton_rotL) # Order all buttons
        MainWindow.setTabOrder(self.pushButton_rotL, self.pushButton_rotR)
        MainWindow.setTabOrder(self.pushButton_rotR, self.pushButton_L)
        MainWindow.setTabOrder(self.pushButton_L, self.pushButton_R)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Image_EXIFViewer", "Image_EXIFViewer"))
        self.pushButton_gps.setText(_translate("Image_EXIFViewer", "GPS"))        

        self.menu.setTitle(_translate("Image_EXIFViewer", "Menu"))
        self.actionApri.setText(_translate("Image_EXIFViewer", "Open image"))
