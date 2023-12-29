""" Main function """

import webbrowser
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QWidget, QVBoxLayout, QTreeWidgetItem, QTreeWidget, QLabel, QMessageBox
from PyQt5.QtGui import  QPixmap, QTransform
from PyQt5.QtCore import Qt, QSize

from view_ui import View_ui

## View of MVC
class View(QMainWindow):
   
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # print("super: ", super().parent)
        self.ui = View_ui(self, self.controller)

        self.index = 0
        self.angle = 0

        self.ui.actionApri.triggered.connect(self.add_image)

    def add_image(self):
        
        image = QFileDialog.getOpenFileName(self, caption='Open an image',
                                            filter='Image files (*.jpg *.jpeg *.png *.JPG *.PNG)')
        if image[0] != '': # Se non aggiungo immagine
            self.controller.add_image(image)
            self.index = self.controller.get_length() # last image
            self.show_image()
         
            
    def show_image(self):
        if self.controller.get_image() != None:
         
            print('Angle', self.angle)
            if  self.angle==0:
                self.qpix_image = QPixmap(self.controller.get_image())
             
                
                pixmap_resized = self.qpix_image.scaled(QSize(min(self.ui.label_image.size().width(), 512), min(self.ui.label_image.size().height(), 512)),
                                                Qt.KeepAspectRatio, Qt.FastTransformation) #Resize image
               
                self.ui.label_image.setPixmap(pixmap_resized)# show image
                #All data
                self.controller.set_info()
                self.controller.set_exif()
                self.tab_data()
            else:
                self.ui.label_image.setPixmap(self.qpix_image.scaled(QSize(min(self.size().width(), 512), min(self.size().height(), 512)),
                                                Qt.KeepAspectRatio, Qt.FastTransformation))
                                                
                self.angle=0
       
    def left(self):
        print("sx", self.index)
        if self.index > 1:
                self.index -= 1
                self.controller.get_image_index(self.index-1) #parto da 0
                self.show_image()
                
    def right(self):
        print("dx", self.index)
        if self.index < self.controller.get_length() :
                self.index += 1
                self.controller.get_image_index(self.index-1) #parto da 0
                self.show_image()

    def rotate_left(self):
        if self.controller.get_image() is not None:
            self.angle -= 90
            transform = QTransform().rotate(self.angle)
            self.qpix_image = self.qpix_image.transformed(transform, Qt.SmoothTransformation)
            self.show_image()
    
    def rotate_right(self):
        if self.controller.get_image() is not None:
            self.angle += 90
            transform = QTransform().rotate(self.angle)
            self.qpix_image = self.qpix_image.transformed(transform, Qt.SmoothTransformation)
            self.show_image()
    
    ##TAB
    def tab_data(self):
        print("QTabWidget")
        info = self.controller.get_info()
        exif = self.controller.get_exif()
        self.updateInfo(info)
        self.tab_exif_ui(exif)

    def set_color(self, tab):
        tab.setStyleSheet(  "QTreeView{                      \n "       
                            "background-color:  rgb(250, 255, 255);}    \n"
                            "QHeaderView::section {          \n"
                            "    color: black;               \n"
                            "    padding: 2px;               \n"
                            "    height:20px;                \n"
                            "    border: 0px solid #567dbc;  \n"
                            "    border-left:0px;            \n"
                            "    border-right:0px;           \n"
                            "    background: rgb(200, 220, 240);        \n"
                            "}                              \n")

    #Write general data    
    def updateInfo(self, info):
        self.ui.tabWidgetInf.clear() #delete old
        print('LEn',(info))
        tab =  QWidget() #self.ui.tab
        
        self.set_color(tab)
        tab.QHBoxLayout.setStyleSheet('background:red')
        #tab.setObjectName("tab")
        
        if info is not None:
            layout = QVBoxLayout()
            #print('LEn',len(info))
            if len(info):
                infoTree = QTreeWidget()
                self.write_tab(infoTree, info)
            else:
                infoTree = QLabel()
                infoTree.setAlignment(Qt.AlignCenter)
                infoTree.setText('Informazioni generali non disponibili')
            
            layout.addWidget(infoTree)
            tab.setLayout(layout)
            
        self.ui.tabWidgetInf.addTab(tab, "Generali")
        #self.ui.tabWidgetInf.setStyleSheet('background:red;')

    #Write exif data 
    def tab_exif_ui(self, exif):        
        tab_exif =  QWidget() #self.ui.tab
        self.set_color(tab_exif)
        if exif is not None:
            if len(exif):
                exifTree = QTreeWidget()
                self.write_tab(exifTree, exif)
                exifTree.setHeaderLabel('Dettagli:')
            else:
                exifTree = QLabel()
                exifTree.setAlignment(Qt.AlignCenter)
                exifTree.setText('Dati EXIF non disponibili')
        else:
            exifTree = QLabel()
            exifTree.setAlignment(Qt.AlignCenter)
            exifTree.setText('Dati EXIF non disponibili')
        
        layout = QVBoxLayout()
        layout.addWidget(exifTree)
        tab_exif.setLayout(layout)
        self.ui.tabWidgetInf.addTab(tab_exif, "Exif")

    def write_tab(self, widget, data):
        self.widget = widget
        self.widget.clear()
        self.writeData(self.widget.invisibleRootItem(), data)

    ## QTreeWidgetItem
    def writeData(self, item, data):
        item.setExpanded(True)
        if type(data) is dict:
            for key, val in data.items():
                child = QTreeWidgetItem()
                child.setText(0, str(key))
                item.addChild(child)
                self.writeData(child, val)
        elif type(data) is list:
            for val in data:
                child = QTreeWidgetItem()
                item.addChild(child)
                if type(val) is dict:
                    child.setText(0, '[dict]')
                    self.writeData(child, val)
                elif type(val) is list:
                    child.setText(0, '[list]')
                    self.writeData(child, val)
                else:
                    child.setText(0, str(val))
                    child.setExpanded(True)
        else:
            child = QTreeWidgetItem()
            child.setText(0, str(data))
            item.addChild(child)
    
    # 
    def set_gps(self):
        if self.controller.get_image() is not None:
            gps = self.controller.get_gps()
            if gps is not None:
                url = "https://www.google.it/maps?q=" + gps
                print("URL",url) 
                webbrowser.open_new(url)
            else:
                QMessageBox.about(self, "Errore", "Informazioni GPS non presenti")
    
    def resizeEvent(self, ev):
        self.show_image()
        super().resizeEvent(ev)