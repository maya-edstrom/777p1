# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2024-10-07 15:00:46
"""
import arcpy
from arcpy.sa import *

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
    nitrate_IDW = "C:\\777p1\\nitrate_IDW"
    IDW = nitrate_IDW
    nitrate_IDW = arcpy.sa.Idw(well_nitrate_OG, "nitr_ran", "0.017616319278512", 2, "VARIABLE 12", "")
    nitrate_IDW.save(IDW)

    # Process: Zonal Statistics as Table (Zonal Statistics as Table) (sa)
    CancerZonalStats = "C:\\777p1\\CancerZonalStats"
    Output_Join_Layer = ""
    arcpy.sa.ZonalStatisticsAsTable(cancer_tracts_OG, "GEOID10", nitrate_IDW, CancerZonalStats, "DATA", "ALL", "CURRENT_SLICE", [90], "AUTO_DETECT", "ARITHMETIC", 360, Output_Join_Layer)

    # Process: Add Join (Add Join) (management)
    cancer_tracts_OG_2_ = arcpy.management.AddJoin(in_layer_or_view=cancer_tracts_OG_3_, in_field="GEOID10", join_table=CancerZonalStats, join_field="GEOID10")[0]

    # Process: Ordinary Least Squares (OLS) (Ordinary Least Squares (OLS)) (stats)
    OLS_fc_shp = "C:\\777p1\\OLS_fc.shp"
    Coefficient_Output_Table = ""
    Diagnostic_Output_Table = ""
    OLS_Report = "C:\\777p1\\OLS_Report.pdf"
    arcpy.stats.OrdinaryLeastSquares(Input_Feature_Class=cancer_tracts_OG_2_, Unique_ID_Field="CancerZonalStats.ZONE_CODE", Output_Feature_Class=OLS_fc_shp, Dependent_Variable="cancer_tracts_OG.canrate", Explanatory_Variables=["CancerZonalStats.MEAN"], Coefficient_Output_Table=Coefficient_Output_Table, Diagnostic_Output_Table=Diagnostic_Output_Table, Output_Report_File=OLS_Report)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb", workspace="C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb"):
        Model()
