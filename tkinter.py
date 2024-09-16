import arcpy 
from arcpy import env
from arcpy.sa import *
import os, sys

import arcpy.geoprocessing
import arcpy.sa

from tkinter import *
env.workspace = r"C:\777p1" # Set the workspace

root = Tk()

#creating a label widget
pgTitle = Label(root, text="Cancer Rates vs. Nitrate Concentrations")

#shoving it onto the screen
pgTitle.pack()

#create event loop
root.mainloop() 