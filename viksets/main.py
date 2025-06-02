import sys
import pprint

from importlib import reload

sys.path.append("C:/User/Documents/viksets")

import sys
import pprint

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from ui import main_window
reload(main_window)



if __name__ == '__main__':

    if not QApplication.instance():
        app_start = 1
        app = QApplication(sys.argv) 

    else:
        app_start = 0
        app = QApplication.instance()

    window = main_window.MainWindow()
    window.show()

    if app_start: 
        sys.exit(app.exec_())