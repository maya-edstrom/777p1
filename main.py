import arcpy 
from arcpy import env
from arcpy.sa import *
import os, sys

import arcpy.geoprocessing
import arcpy.sa

arcpy.env.overwriteOutput = True # Allow the overwriting of the output files
outFolder = r"C:\777p1\output" # Set the output folder

env.workspace = r"C:\777p1\data" # Set the workspace
  
#step 1: interpolating nitrate values to census blocks using IDW tool using different user inputs for k value

inPoint = "well_nitrate.shp" # Set the input point feature class to the well nitrate shapefile
zField = "nitr_ran"
power = 2 #will need to get user input eventually
    
# Execute IDW
outIDW = Idw(inPoint, zField, power) # Perform the IDW interpolation using the input point feature class, the field to interpolate, and the power value

# Save output
IDW_OUT= os.path.join(outFolder, '{}.tif'.format)
outIDW.save(IDW_OUT)
print("IDW interpolation complete") # Print that the interpolation is complete

