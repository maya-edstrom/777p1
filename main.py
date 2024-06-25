import arcpy 
from arcpy import env
from arcpy.sa import *
import os, sys

import arcpy.geoprocessing
import arcpy.sa

arcpy.env.overwriteOutput = True # Allow the overwriting of the output files

env.workspace = "C:\777p1\data" # Set the workspace
  
#step 1: interpolating nitrate values to census blocks using IDW tool using different user inputs for k value

    power = 2 #will need to get user input eventually
    inPoint = "well.nitrate.shp" # Set the input point feature class to the well nitrate shapefile
    zField = "nitr_ran"
    outLayer = "IDW" # Set the output layer to IDW
    
    # Execute IDW
    outIDW = arcpy.sa.Idw(inPoint, zField, power) # Perform the IDW interpolation using the input point feature class, the field to interpolate, and the power value
    # Save the output 
    outIDW.save("C:/sapyexamples/output/idwout02")

    print("IDW interpolation complete") # Print that the interpolation is complete

