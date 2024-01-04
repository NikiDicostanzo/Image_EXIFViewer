# Import stuff
import sys
from PyQt5.QtWidgets import QApplication
from model import Model
from controller import Controller
from view import View

# Use a __main__ guard, you never know.
if __name__ == '__main__':
    # Create our application -- MUST be done first.
    app = QApplication(sys.argv)

    # MVC
    model = Model()
    controller = Controller(model)
    window = View(controller)
    
    # Show the main window and call main loop.
    window.show()
    sys.exit(app.exec_())