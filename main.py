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


def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("3D")
    arcpy.CheckOutExtension("spatial")
    arcpy.CheckOutExtension("ImageExt")
    arcpy.CheckOutExtension("ImageAnalyst")

    cancer_tracts_OG = "cancer_tracts_OG"
    well_nitrate_OG = "well_nitrate_OG"
    cancer_tracts_OG_3_ = "cancer_tracts_OG"

    # Process: IDW (IDW) (sa)
    nitrate_IDW = "C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb\\nitrate_IDW"
    IDW = nitrate_IDW
    nitrate_IDW = arcpy.sa.Idw(well_nitrate_OG, "nitr_ran", "0.017616319278512", 2, "VARIABLE 12", "")
    nitrate_IDW.save(IDW)


    # Process: Zonal Statistics as Table (Zonal Statistics as Table) (sa)
    CancerZonalStats = "C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb\\CancerZonalStats"
    Output_Join_Layer = ""
    arcpy.sa.ZonalStatisticsAsTable(cancer_tracts_OG, "GEOID10", nitrate_IDW, CancerZonalStats, "DATA", "ALL", "CURRENT_SLICE", [90], "AUTO_DETECT", "ARITHMETIC", 360, Output_Join_Layer)
    .save(Zonal_Statistics_as_Table)


    # Process: Add Join (Add Join) (management)
    cancer_tracts_OG_2_ = arcpy.management.AddJoin(in_layer_or_view=cancer_tracts_OG_3_, in_field="GEOID10", join_table=CancerZonalStats, join_field="GEOID10")[0]

    # Process: Ordinary Least Squares (OLS) (Ordinary Least Squares (OLS)) (stats)
    cancer_tracts_OG_OrdinaryLeastSquares = "C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb\\cancer_tracts_OG_OrdinaryLeastSquares"
    Coefficient_Output_Table = ""
    Diagnostic_Output_Table = ""
    OLS_Report = "C:\\777p1\\OLS_Report.pdf"
    arcpy.stats.OrdinaryLeastSquares(Input_Feature_Class=cancer_tracts_OG_2_, Unique_ID_Field="CancerZonalStats.ZONE_CODE", Output_Feature_Class=cancer_tracts_OG_OrdinaryLeastSquares, Dependent_Variable="cancer_tracts_OG.canrate", Explanatory_Variables=["CancerZonalStats.MEAN"], Coefficient_Output_Table=Coefficient_Output_Table, Diagnostic_Output_Table=Diagnostic_Output_Table, Output_Report_File=OLS_Report)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb", workspace="C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb"):
        Model()


root = tk.Tk()

#creating a label widget
pgTitle = tk.Label(root, text="Cancer Rates vs. Nitrate Concentrations")

#shoving it onto the screen
pgTitle.pack()

#create event loop
root.mainloop() 