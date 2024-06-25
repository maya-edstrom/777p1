import arcpy 
import os, sys

arcpy.env.overwriteOutput = True # Allow the overwriting of the output files

try:
    arcpy.env.workspace = "C:\777p1\data" # Set the workspace
except:
    print('Failed to establish workspace')
  

#step 1: saving shapefiles to variables
try: 
    cancer_tracts = "cancer.tracts.shp" # Open the cancer tracts shapefile and store in variable
except:
    print('Failed to open shapefile')


try: 
    well_nitrate = "well.nitrate.shp" # Open the well nitrate shapefile and store in variable
except:
    print('Failed to open shapefile')
   
try:
    census_blocks = "WI_CensusTL_BlockGroups_2020.shp" # Open the census blocks shapefile and store in variable

except: 
    print('Failed to open shapefile')
 

#step 2: interpolating nitrate values to census blocks using IDW tool using different user inputs for k value

    k = 2 #will need to get user input eventually
        
    inPoint = "well.nitrate.shp" # Set the input point feature class to the well nitrate shapefile
    zField = "nitr_ran"
    outLayer = "IDW" # Set the output layer to IDW
    
    # Execute IDW
    outIDW = Idw(inPointFeatures, zField, cellSize, power, searchRadius)

    # Save the output 
    outIDW.save("C:/sapyexamples/output/idwout02")

    print("IDW interpolation complete") # Print that the interpolation is complete

