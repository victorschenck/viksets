from importlib import reload
import sys

from maya import cmds


def addProjectPathToSys(project_path):

    if project_path in sys.path:
        return
    
    sys.path.append(project_path)
    print('Building rig from:  ' + project_path)


def removeProjectPathFromSys(project_path):
    if project_path in sys.path:
        sys.path.remove(project_path)


def buildRig(project_path_str, template_scene_path_str):
    
    #Creating a new, empty scene
    cmds.file(new=True, f=True)

    if template_scene_path_str == '':
        pass
    else:
        #Import the template scene
        cmds.file(template_scene_path_str, i=True, f=True, dns=True)
        #dns flag stands for default namespace and imports everything without namespaces.

        



    addProjectPathToSys(project_path_str)
    import build_rig
    reload(build_rig)
    build_rig.run()

    removeProjectPathFromSys(project_path_str)


def openTemplateFile(template_scene_path_str):    
    cmds.file(template_scene_path_str, o=True, f=True)