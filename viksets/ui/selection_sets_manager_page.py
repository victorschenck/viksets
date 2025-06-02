
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from importlib import reload
from pathlib import Path
import json

from maya_scripts import selection_sets_maya_utils
reload(selection_sets_maya_utils)


class selectionSetsManagerPageWidget(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        #Page Title !!
        self.page_title = 'Sets'



        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)



        #User Selection List Widget:
        self.user_selection_list_widget = QListWidget(self)
        
        #User Selection Count Widget:
        self.user_selection_count_label = QLabel(self)
        self.user_selection_count_label.setText('Count:')
        self.user_selection_count_label.setStyleSheet('''font: 75 8pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 5px;''')
        
        #User export set name:
        self.user_export_set_name_line_edit = QLineEdit(self)
        self.user_export_set_name_line_edit.setHidden(True)
        self.user_export_set_name_line_edit.setPlaceholderText('Export selection set name')
        self.user_export_set_name_line_edit.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 5px;''')
        





        #Get User Selection Button:
        self.get_user_sel_button = QPushButton(self)
        self.get_user_sel_button.setText('Get Selection')
        self.get_user_sel_button.setStyleSheet('''font: 75 12pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 16px;''')


        #Import Set Button:
        self.import_set_button = QPushButton(self)
        self.import_set_button.setText('Import set')
        self.import_set_button.setStyleSheet('''font: 75 12pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 16px;''')
        

        #Export Set Button:
        self.export_set_button = QPushButton(self)
        self.export_set_button.setText('Export set')
        self.export_set_button.setStyleSheet('''font: 75 12pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 16px;''')
        self.export_set_button.setEnabled(False)
        
        #Separator:
        self.separator_1 = QFrame()
        self.separator_1.setFrameShape(QFrame.HLine)
        self.separator_1.setFrameShadow(QFrame.Sunken)


        #Suffix / Prefix:
        self.suffix_prefix_hlayout = QHBoxLayout()

        self.suffix_line_edit = QLineEdit(self)
        self.suffix_line_edit.setHidden(False)
        self.suffix_line_edit.setPlaceholderText('Suffix')
        self.suffix_line_edit.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 5px;''')
        
        self.prefix_line_edit = QLineEdit(self)
        self.prefix_line_edit.setHidden(False)
        self.prefix_line_edit.setPlaceholderText('Prefix')
        self.prefix_line_edit.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 5px;''')
        
        self.suffix_prefix_hlayout.addWidget(self.prefix_line_edit)
        self.suffix_prefix_hlayout.addWidget(self.suffix_line_edit)
        



        #Arrangment:
        self.main_layout.addWidget(self.user_selection_count_label)
        self.main_layout.addWidget(self.user_selection_list_widget)
        self.main_layout.addWidget(self.get_user_sel_button)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.import_set_button)
        self.main_layout.addLayout(self.suffix_prefix_hlayout)
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.export_set_button)
        self.main_layout.addWidget(self.user_export_set_name_line_edit)
        #self.main_layout.addStretch()

        #Connections:
        self.get_user_sel_button.clicked.connect(self.getUserSelectionButtonTriggered)
        self.import_set_button.clicked.connect(self.importSetButtonTriggered)
        self.export_set_button.clicked.connect(self.exportSetButtonTriggerted)










        """
        #Project & Template scene slots:
        self.file_edits_layout = QVBoxLayout()
        self.project_location_title_label = QLabel(self)
        self.project_location_title_label.setText('Project location')
        self.project_location_title_label.setStyleSheet('''font: 75 12pt "Microsoft YaHei UI"; font-weight: bold;''')

        self.project_location_line_edit = FileEdit(self)

        self.template_scene_location_title_label = QLabel(self)
        self.template_scene_location_title_label.setText('Template scene location')
        self.template_scene_location_title_label.setStyleSheet('''font: 75 12pt "Microsoft YaHei UI"; font-weight: bold;''')
        self.template_scene_location_line_edit = FileEdit(self)

        self.file_edits_layout.addWidget(self.project_location_title_label)
        self.file_edits_layout.addWidget(self.project_location_line_edit)

        self.file_edits_layout.addWidget(self.template_scene_location_title_label)
        self.file_edits_layout.addWidget(self.template_scene_location_line_edit)

        #Edit Template Button
        self.edit_template_button = QPushButton(self)
        self.edit_template_button.setText('Edit template')
        self.edit_template_button.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 16px;''')


        #Save Paths Button
        self.save_paths_button_layout = QHBoxLayout()
        self.save_paths_button = QPushButton(self)
        self.save_paths_button.setText('Save Paths')
        self.save_paths_button.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 16px;''')

        #Positionning the save paths button correctly in his own layout
        self.save_paths_button_layout.addStretch()
        self.save_paths_button_layout.addWidget(self.edit_template_button)
        self.save_paths_button_layout.addWidget(self.save_paths_button)

        #Adding everything together in the file edits layout
        self.file_edits_layout.addLayout(self.save_paths_button_layout)
        self.file_edits_layout.addStretch()


        self.build_button = QPushButton(self)
        self.build_button.setText('Build !')
        self.build_button.setStyleSheet('''font: 75 12pt "Microsoft YaHei UI";
                                        font-weight: bold;
                                        padding: 10px;
                                        background-color: #571157;
                                        border: 0px;
                                        border-radius: 16px;''')




        #Layout items:
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.file_edits_layout)
        self.main_layout.addWidget(self.build_button)


        #Connections:
        self.save_paths_button.clicked.connect(self.savePathsButtonTriggered)
        self.edit_template_button.clicked.connect(self.editTemplateButtonTriggered)
        self.build_button.clicked.connect(self.buildButtonTriggered)


        #Loading user data:
        self.loadSavedPathsFromUserData()
        """

    def getUserSelectionButtonTriggered(self):

        user_selection = selection_sets_maya_utils.getSelection()
        self.user_selection_list_widget.clear() #Clearing display list

        item_counter = 0

        #Adding elements
        for current_selected_item in user_selection:
            item_counter += 1
            current_list_item = QListWidgetItem()
            current_list_item.setText(current_selected_item)
            self.user_selection_list_widget.addItem(current_list_item)
        
        #Updating counter
        self.user_selection_count_label.setText(f'Count: {item_counter}')
        
        self.export_list = user_selection
        self.user_export_set_name_line_edit.setHidden(False)
        self.export_set_button.setEnabled(True)




    def importSetButtonTriggered(self):

        suffix = self.suffix_line_edit.text()
        prefix = self.prefix_line_edit.text()

        selection_sets_maya_utils.importSetsInScene(suffix=suffix, prefix=prefix)
        



    def exportSetButtonTriggerted(self):

        export_name = self.user_export_set_name_line_edit.text()
        selection_sets_maya_utils.exportSetsToJson(export_name, self.export_list)

        self.export_set_button.setEnabled(False)
        self.user_export_set_name_line_edit.setHidden(True)
    









class FileEdit(QLineEdit):

    def __init__( self, parent ):
        super(FileEdit, self).__init__(parent)
        self.setDragEnabled(True)

        self.setStyleSheet('''font: 75 10pt "Microsoft YaHei UI";
                                        padding: 5px;
                                        background-color: #1d0c4f;
                                        border: 0px;
                                        border-radius: 8px;''')


    def dragEnterEvent( self, event ):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            event.acceptProposedAction()

    def dragMoveEvent( self, event ):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            event.acceptProposedAction()

    def dropEvent( self, event ):
        data = event.mimeData()
        urls = data.urls()
        if ( urls and urls[0].scheme() == 'file' ):
            # for some reason, this doubles up the intro slash
            filepath = str(urls[0].path())[1:]
            self.setText(filepath)