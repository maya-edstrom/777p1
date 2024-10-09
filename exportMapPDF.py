#import arcpy
#from arcpy.sa import *

#aprx = arcpy.mp.ArcGISProject(r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.aprx")
#aprx.defaultGeodatabase = r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.gdb"
#print(aprx.filePath)

#m = aprx.listMaps("Map")[0]
#lyrFile = arcpy.mp.LayerFile(r"C:\777p1\ArcGISPro\Geog777_P1\OLS_fc_SaveToLayerFile.lyrx")
#m.addLayer(lyrFile, "TOP")

import arcpy
from arcpy.sa import *

try:
    # Load the ArcGIS Project
    aprx = arcpy.mp.ArcGISProject(r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.aprx")
    aprx.defaultGeodatabase = r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.gdb"
    print(f"Project file path: {aprx.filePath}")

    # Check if the map exists
    maps = aprx.listMaps("Map")
    if not maps:
        raise ValueError("Map named 'Map' not found in the project.")
    
    m = maps[0]

    # Check if the layer file exists
    layer_file_path = r"C:\777p1\ArcGISPro\Geog777_P1\OLS_fc_SaveToLayerFile.lyrx"
    if not arcpy.Exists(layer_file_path):
        raise ValueError(f"Layer file not found at {layer_file_path}")

    # Add the layer file to the map
    lyrFile = arcpy.mp.LayerFile(layer_file_path)
    m.addLayer(lyrFile, "TOP")
    print("Layer added successfully.")

except Exception as e:
    print(f"An error occurred: {e}")