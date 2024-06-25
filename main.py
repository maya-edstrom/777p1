import arcpy 
import os, sys

arcpy.env.overwriteOutput = True # Allow the overwriting of the output files

try:
    arcpy.env.workspace = "C:\777p1\data" # Set the workspace
except:
    print('Failed to establish workspace')
    sys.exit()

#step 1: saving shapefiles to variables
try: 
    cancer_tracts = "cancer.tracts.shp" # Open the cancer tracts shapefile and store in variable
except:
    print('Failed to open shapefile')
    sys.exit()

try: 
    well_nitrate = "well.nitrate.shp" # Open the well nitrate shapefile and store in variable
except:
    print('Failed to open shapefile')
    sys.exit()

try:
    census_blocks = "WI_CensusTL_BlockGroups_2020.shp" # Open the census blocks shapefile and store in variable

except: 
    print('Failed to open shapefile')
    sys.exit()

#step 2: interpolating nitrate values to census blocks using IDW tool using different user inputs for k value
k = input("Enter a value for k: ") # Ask the user to input a value for k

if k == 1: # If the user inputs 1 for k value
    outIDW = arcpy.sa.Idw(well_nitrate, "nitr_ran", 1000, 2, "SQUARE", "CELLSIZE", 0.0001) # Use the IDW tool to interpolate nitrate values to census blocks using the well nitrate shapefile and the nitrate range field
    outIDW.save("IDW_1.shp") # Save the output to a new shapefile

elif k == 2: # If the user inputs 2 for k value
    outIDW = arcpy.sa.Idw(well_nitrate, "nitr_ran", 1000, 2, "SQUARE", "CELLSIZE", 0.0001) # Use the IDW tool to interpolate nitrate values to census blocks using the well nitrate shapefile and the nitrate range field
    outIDW.save("IDW_2.shp")

elif k < 3: # If the user inputs 3 for k value




