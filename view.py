""" Main function """

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import  QPixmap

from PyQt5.QtCore import Qt

from view_ui import View_ui
from model import Model

## View of MVC
class View(QMainWindow):
   
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # print("super: ", super().parent)
        self.ui = View_ui(self, self.controller)
        self.index = 0
      
        self.ui.actionApri.triggered.connect(self.add_image)


    def add_image(self):
        
        image = QFileDialog.getOpenFileName(self, caption='Open an image',
                                            filter='Image files (*.jpg *.jpeg *.png *.JPG *.PNG)')
        if image[0] != '': # Se non aggiungo immagine
            self.controller.add_image(image)
            self.index = self.controller.get_length() # last image
            self.show_image()
    
    def show_image(self):
            self.qpix_image = QPixmap(self.controller.get_image())
            pixmap_resized = self.qpix_image.scaled(500, 500, Qt.KeepAspectRatio) #Resize image
            self.ui.label_image.setPixmap(pixmap_resized)# show image
       

    def left(self):
        print("sx", self.index)
        if self.index > 1:
                self.index -= 1
                self.controller.get_image_index(self.index-1) #parto da 0
                self.show_image()
                print('qui',self.controller.get_image())
                
                
    def right(self):
        print("dx", self.index)
        if self.index < self.controller.get_length() :
                self.index += 1
                self.controller.get_image_index(self.index-1) #parto da 0
                self.show_image()