from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from importlib import reload
from pathlib import Path

from ui import selection_sets_manager_page
reload(selection_sets_manager_page)

class mainTabWidget(QTabWidget):
    def __init__(self, *args, **kwargs):
        QTabWidget.__init__(self, *args, **kwargs)


        #First Tab:
        self.second_tab_widget = selection_sets_manager_page.selectionSetsManagerPageWidget()
        self.addTab(self.second_tab_widget, self.second_tab_widget.page_title)



        ui_path = Path(__file__).parent
        background_file_path = Path(ui_path) / './bg.png'


        self.tile = QPixmap(str(background_file_path))

        self.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        font-weight: bold;
                                        background-color: transparent;''')
        
        #self.tabBar().self.setStyleSheet('''background-color: transparent;''') THIS CRASHES !!!!!

        


    def paintEvent(self, event):
        
        painter = QPainter(self)
        painter.drawTiledPixmap(self.rect(), self.tile)

        #super().paintEvent(event)