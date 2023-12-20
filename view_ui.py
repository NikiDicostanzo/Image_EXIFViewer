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
        MainWindow.resize(572, 479)
        MainWindow.setStyleSheet("background-color: rgb(229, 241, 255);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

         #--
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 400, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 400, 75, 24))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 400, 75, 24))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Downloads/arrow-left2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 400, 75, 24))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Downloads/right-arrow2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 400, 75, 24))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Downloads/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidgetInf = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetInf.setGeometry(QtCore.QRect(310, 30, 251, 351))
        self.tabWidgetInf.setStyleSheet("background-color: rgb(237, 255, 254);")
        self.tabWidgetInf.setObjectName("tabWidgetInf")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(8, 5, 231, 261))
        self.label.setStyleSheet("background-color: rgb(240, 255, 253);")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.tabWidgetInf.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(8, 5, 231, 311))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.tabWidgetInf.addTab(self.tab_2, "")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 291, 351))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../Downloads/arrow-up.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 22))
        self.menubar.setObjectName("menubar")
        self.menuprova = QtWidgets.QMenu(self.menubar)
        self.menuprova.setObjectName("menuprova")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionApri = QtWidgets.QAction(MainWindow)
        self.actionApri.setObjectName("actionApri")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuprova.addSeparator()
        self.menuprova.addAction(self.actionApri)
        self.menuprova.addAction(self.actionSave)
        self.menubar.addAction(self.menuprova.menuAction())


        #My image in window
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(10, 30, 431, 501))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 4)

        self.retranslateUi(MainWindow)
        self.tabWidgetInf.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Apri"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Nome</span></p><p><span style=\" font-size:10pt; font-style:italic;\">    - ciao</span></p><p><span style=\" font-size:10pt; font-style:italic;\">Data</span></p><p><span style=\" font-size:10pt; font-style:italic;\">    - 10.10.20</span></p><p><span style=\" font-size:10pt; font-style:italic;\">Bho</span></p><p><span style=\" font-size:10pt; font-style:italic;\">    - foksog</span></p></body></html>"))
        self.tabWidgetInf.setTabText(self.tabWidgetInf.indexOf(self.tab), _translate("MainWindow", "Generali"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Tag non presenti</span></p></body></html>"))
        self.tabWidgetInf.setTabText(self.tabWidgetInf.indexOf(self.tab_2), _translate("MainWindow", "Exif"))
        self.menuprova.setTitle(_translate("MainWindow", "prova"))
        self.actionApri.setText(_translate("MainWindow", "Apri"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

