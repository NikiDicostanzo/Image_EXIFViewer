""" Main function """

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5.QtGui import  QPixmap, QTransform

from PyQt5.QtCore import Qt, QSize

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
        self.angle=0

        self.ui.actionApri.triggered.connect(self.add_image)


    def add_image(self):
        
        image = QFileDialog.getOpenFileName(self, caption='Open an image',
                                            filter='Image files (*.jpg *.jpeg *.png *.JPG *.PNG)')
        if image[0] != '': # Se non aggiungo immagine
            self.controller.add_image(image)
            self.index = self.controller.get_length() # last image
            self.show_image()

        self.controller.set_image(image) # update image
        ###
        self.controller.set_info()
        self.controller.set_exif()
           
    
    def show_image(self):
        if  self.angle==0:
            self.qpix_image = QPixmap(self.controller.get_image())
            pixmap_resized = self.qpix_image.scaled(500, 500, Qt.KeepAspectRatio) #Resize image
            self.ui.label_image.setPixmap(pixmap_resized)# show image
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
                print('qui',self.controller.get_image())

                ###
                self.controller.set_info()
                self.controller.set_exif()
                        

    def right(self):
        print("dx", self.index)
        if self.index < self.controller.get_length() :
                self.index += 1
                self.controller.get_image_index(self.index-1) #parto da 0
                self.show_image()

                ###
                self.controller.set_info()
                self.controller.set_exif()


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