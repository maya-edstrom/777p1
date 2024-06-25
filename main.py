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
try:

    k = int(input("Please enter a value between 0 and 2 for k: ")) # Ask the user to input a value for k

except:
    print('Failed to input value, please try again. Enter a value between 0 and 2.')
    sys.exit()

IDW = arcpy.analysis.IDW(well_nitrate, "IDW.shp", "RASTERVALU", k) # Use the IDW tool to interpolate nitrate values to census blocks    


