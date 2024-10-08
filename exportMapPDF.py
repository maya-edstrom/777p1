import arcpy
from arcpy.sa import *

aprx = arcpy.mp.ArcGISProject(r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.aprx")
aprx.defaultGeodatabase = r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.gdb"
print(aprx.filePath)

m = aprx.listMaps("Map")[0]
lyrFile = arcpy.mp.LayerFile(r"C:\777p1\ArcGISPro\Geog777_P1\Geog777_P1.gdb\OLS_fc.lyrx")
m.addLayer(lyrFile, "TOP")