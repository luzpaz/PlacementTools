# -*- codecs: utf-8 -*-
import FreeCAD,FreeCADGui

import inspect, os.path
filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))
#FreeCAD.Console.PrintMessage(path)

ICONPATH = path+'/Resources/icons/'

#ICONPATH = FreeCAD.getUserAppDataDir()+'Mod/PlacementTools/Resources/icons/'

def upperObject(obj):
	if obj.Module=="PartDesign":
		if obj.InList.__len__()>0:
			return upperObject(obj.InList[0])
		else:
			return obj
	else:
		return obj
def GetSelectedUpperObjectsNew():
	upperobjs=[]
	objs=FreeCADGui.Selection.getSelection() 
	for obj in objs:
		upperobjs.append(upperObject(obj))
	return upperobjs

def GetSelectedUpperObjects():
	upperobjs=[]
	objs=FreeCADGui.Selection.getSelection() 
	for obj in objs:
		if obj.Module=="PartDesign":
			if obj.TypeId=='PartDesign::Body':
				upperobjs.append(obj)
			else:
				upperobjs.append(obj.InList[0])
		else:
			upperobjs.append(obj)
	return upperobjs
