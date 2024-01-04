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
        self.ui = View_ui(self, self.controller)

        self.index = 0
        self.angle = 0

    # Open and add new image
    def add_image(self):
        image = QFileDialog.getOpenFileName(self, caption='Open an image',
                                            filter='Image files (*.jpg *.jpeg *.png *.JPG *.PNG)')
        if image[0] != '': # Se aggiungo immagine
            self.controller.add_image(image)
            self.index = self.controller.get_length()-1 # last image
            self.show_image()
         
    def show_image(self):
        if self.controller.get_image() != None: 
            if  self.angle==0: # if not rotate image 
                self.qpix_image = QPixmap(self.controller.get_image())
                pixmap_resized = self.qpix_image.scaled(QSize(min(self.ui.label_image.size().width(), 512), min(self.ui.label_image.size().height(), 512)),
                                                Qt.KeepAspectRatio, Qt.FastTransformation) #Resize image (max 512x512)
                self.ui.label_image.setPixmap(pixmap_resized)# Show image in label 
                #Set all data
                self.controller.set_info() 
                self.controller.set_exif()
                self.tab_data() # Show tab data
            else:
                self.ui.label_image.setPixmap(self.qpix_image.scaled(QSize(min(self.size().width(), 512), min(self.size().height(), 512)),
                                                Qt.KeepAspectRatio, Qt.FastTransformation))                     
                self.angle=0 # reset angle

    ### Action ###   
    def left(self): # previous image
        if self.index >= 1:
                self.index -= 1
                self.controller.get_image_index(self.index) 
                self.show_image()
                
    def right(self): # next image
        if self.index < self.controller.get_length()-1:
                self.index += 1
                self.controller.get_image_index(self.index) 
                self.show_image()

    def rotate_left(self): # left rotate image
        if self.controller.get_image() is not None:
            self.angle -= 90
            transform = QTransform().rotate(self.angle)
            self.qpix_image = self.qpix_image.transformed(transform, Qt.SmoothTransformation)
            self.show_image()
    
    def rotate_right(self): # right rotate image
        if self.controller.get_image() is not None:
            self.angle += 90
            transform = QTransform().rotate(self.angle)
            self.qpix_image = self.qpix_image.transformed(transform, Qt.SmoothTransformation)
            self.show_image()
    
    ### TAB ###
    def tab_data(self): 
        info = self.controller.get_info()
        exif = self.controller.get_exif()
        self.updateInfo(info)
        self.tab_exif_ui(exif)

    ### Write general information ###    
    def updateInfo(self, info):
        self.ui.tabWidgetInf.clear() #delete old
        tab =  QWidget() 
        if info is not None:
            layout = QVBoxLayout()
            if len(info): # write info
                infoTree = QTreeWidget()
                infoTree.setStyleSheet('background: rgb(237, 255, 254)')
                self.write_tab(infoTree, info)
                infoTree.setHeaderLabel('Dettagli:')
            else: # info not available
                infoTree = QLabel()
                infoTree.setAlignment(Qt.AlignCenter)
                infoTree.setStyleSheet('QLabel{background: rgb(237, 255, 254); border: 1px solid; ; font:italic 20px ;}')
                infoTree.setText('Informazioni generali non disponibili')
            layout.addWidget(infoTree)
            tab.setLayout(layout)    
        self.ui.tabWidgetInf.addTab(tab, "Generali")

    ### Write exif data ###
    def tab_exif_ui(self, exif):        
        tab_exif =  QWidget() 
        if exif is not None and len(exif): # Write exif
            exifTree = QTreeWidget()
            exifTree.setStyleSheet('background: rgb(237, 255, 254)')
            data_exif = exif
            del data_exif['GPSInfo'] # don't show gps in tab
            self.write_tab(exifTree, data_exif) 
            exifTree.setHeaderLabel('Dettagli:')
        else: # Exif not available
            exifTree = QLabel()
            exifTree.setAlignment(Qt.AlignCenter)
            exifTree.setStyleSheet('QLabel{background: rgb(237, 255, 254); border: 1px solid; font: italic 20px;}')
            exifTree.setText('Dati EXIF non disponibili')

        layout = QVBoxLayout()
        layout.addWidget(exifTree) #
        tab_exif.setLayout(layout)
        self.ui.tabWidgetInf.addTab(tab_exif, "Exif")

    def write_tab(self, widget, data): 
        self.widget = widget
        self.widget.clear()
        self.writeData(self.widget.invisibleRootItem(), data) 

    ## QTreeWidgetItem
    def writeData(self, item, data): # Create tree of data in recursive way 
        item.setExpanded(True) # Expand item of tree
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
    
    # Create url for gps
    def set_gps(self):
        if self.controller.get_image() is not None:
            gps = self.controller.get_gps()
            if gps is not None:
                url = "https://www.google.it/maps?q=" + gps
                print("URL",url) 
                webbrowser.open_new(url)
            else:
                QMessageBox.about(self, "Errore", "Informazioni GPS non presenti")
    
    # Resize image, if resize window
    def resizeEvent(self, ev):
        self.show_image()
        super().resizeEvent(ev)