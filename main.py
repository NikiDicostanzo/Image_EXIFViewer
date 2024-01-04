import sys
from PyQt5.QtWidgets import QApplication
from model import Model
from controller import Controller
from view import View

if __name__ == '__main__':
    # Create our application 
    app = QApplication(sys.argv)

    # MVC
    model = Model()
    controller = Controller(model)
    window = View(controller)
    
    # Show the main window and call main loop.
    window.show()
    sys.exit(app.exec_())