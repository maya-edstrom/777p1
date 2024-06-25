import arcpy 
from arcpy import env
from arcpy.sa import *
import os, sys

import arcpy.geoprocessing
import arcpy.sa

arcpy.env.overwriteOutput = True # Allow the overwriting of the output files

env.workspace = r"C:\777p1\data" # Set the workspace
  
#step 1: interpolating nitrate values to census blocks using IDW tool using different user inputs for k value

inPointFeatures = "well_nitrate.shp" # Set the input point feature class to the well nitrate shapefile
cellSize = 2000.0
zField = "TARGET_FIELD"
power = 2 #will need to get user input eventually
searchRadius = RadiusVariable
    
# Execute IDW
outIDW = Idw(inPointFeatures, zField, cellSize, power, searchRadius)

# Save the output 
outIDW.save(r"C:\777p1\data\output")