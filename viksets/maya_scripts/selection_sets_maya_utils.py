from maya import cmds
import json
from pathlib import Path


def getSelection(*args):

    sel = cmds.ls(sl=True)
    return sel



def exportSetsToJson(set_name, export_list, *args):

    export_dict = {}
    export_dict['name'] = set_name
    export_dict['set'] = export_list

    multipleFilters = "json (*.json);;All Files (*.*)"
    export_path = cmds.fileDialog2(ff = multipleFilters, ds=1)[0]


    print(f'EXPORTING TO : {export_path}')

    out_file = open(export_path, "w") 
    
    json.dump(export_dict, out_file, indent = 6) 
    
    out_file.close()

 



def importSetsInScene(*args, prefix, suffix) :

    multipleFilters = "json (*.json);;All Files (*.*)"
    import_path = cmds.fileDialog2(ff = multipleFilters, fm=1, ds=1)[0]

    print(f'READING FROM : {import_path}')


    with open(import_path, 'r') as openfile:
 
        # Reading from json file
        imported_dict = json.load(openfile)

    imported_list = imported_dict['set']
    imported_name = imported_dict['name']


    if imported_name == '':
        set_name = 'IMPORTED SET'
    else:
        set_name = imported_name



    renamed_list = []

    for current_item in imported_list :
            
            new_name = prefix + current_item + suffix
            renamed_list.append(new_name)
    
    cmds.sets(renamed_list, n=set_name)

    """if prefix and not suffix:
        for x in imported_list :

            new_name = prefix + x
            renamed_list.append(new_name)
            cmds.sets(renamed_list, n=set_name)

    elif suffix and not prefix:
        for y in imported_list :
            
            new_name = y + suffix
            renamed_list.append(new_name)
            cmds.sets(renamed_list, n=set_name)

    else:
        cmds.sets(imported_list, n=set_name)"""

