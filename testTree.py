# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_TreeWidget_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(572, 479)
        MainWindow.setStyleSheet("background-color: rgb(229, 241, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 400, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 400, 75, 24))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Downloads/arrow-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 400, 75, 24))
        self.pushButton_3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Downloads/arrow-left2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 400, 75, 24))
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Downloads/right-arrow2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 400, 75, 24))
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../Downloads/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidgetInf = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidgetInf.setGeometry(QtCore.QRect(310, 30, 251, 351))
        self.tabWidgetInf.setStyleSheet("background-color: rgb(237, 255, 254);")
        self.tabWidgetInf.setObjectName("tabWidgetInf")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 10, 241, 301))
        self.treeWidget.setStyleSheet("QHeaderView::section {                          \n"
"    color: black;                               \n"
"    padding: 2px;                               \n"
"    height:20px;                                \n"
"    border: 0px solid #567dbc;                  \n"
"    border-left:0px;                            \n"
"    border-right:0px;                           \n"
"    background: magenta;                        \n"
"}")
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
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
        self.label_3.setPixmap(QtGui.QPixmap("../../../../Downloads/arrow-up.png"))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 26))
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
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "gdgd"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "fdfd"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "sdsds"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "dsds"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "New Item"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidgetInf.setTabText(self.tabWidgetInf.indexOf(self.tab), _translate("MainWindow", "Generali"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Tag non presenti</span></p></body></html>"))
        self.tabWidgetInf.setTabText(self.tabWidgetInf.indexOf(self.tab_2), _translate("MainWindow", "Exif"))
        self.menuprova.setTitle(_translate("MainWindow", "prova"))
        self.actionApri.setText(_translate("MainWindow", "Apri"))
        self.actionSave.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())