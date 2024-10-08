import arcpy 
from arcpy import env
from arcpy.sa import *
import os, sys

import arcpy.geoprocessing
import arcpy.sa

import tkinter as tk


root = tk.Tk()
print("Tkinter is installed and working!")
root.destroy()

env.workspace = r"C:\777p1" # Set the workspace

root = tk.Tk()

#creating a label widget
pgTitle = tk.Label(root, text="Spatial Analysis of Cancer Rates vs. Nitrate Concentrations in Wisconsin using Linear Regression")

#shoving it onto the screen
pgTitle.pack()

#create event loop
root.mainloop() 