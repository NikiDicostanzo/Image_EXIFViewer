""" Main function """

from PyQt5.QtWidgets import QMainWindow, QFileDialog

from view_ui import View_ui
from model import Model

## View of MVC
class View(QMainWindow):
   
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        # print("super: ", super().parent)
        self.ui = View_ui(self, self.controller)
      
        self.ui.actionApri.triggered.connect(self.addImage)


    def addImage(self):
        
        image = QFileDialog.getOpenFileName(self, caption='Open an image',
                                            filter='Image files (*.jpg *.jpeg *.png *.JPG *.PNG)')
        self.controller.set_image(image)