from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from importlib import reload
from pathlib import Path


from ui import main_tab_widget
reload(main_tab_widget)

 
class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__()

        #Making the window appear on top:
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Vik Sets')
        

        #Creating the tab widget:
        tab_widget = main_tab_widget.mainTabWidget()
        self.setCentralWidget(tab_widget)


        self.setGeometry(100,100,300,600)
        


        self.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI"; ''')




    

    