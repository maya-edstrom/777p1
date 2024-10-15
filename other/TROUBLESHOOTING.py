import arcpy
from arcpy.sa import *
import tkinter as tk
from tkinter import messagebox
import os
import sys
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Linear Regression Analysis of Cancer Rates vs. Nitrate Concentrations in Wisconsin")


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def Model(kValue):  # Model
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb", workspace="C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb"):
        arcpy.env.workspace = "C:\\777p1\\ArcGISPro\\Geog777_P1\\Geog777_P1.gdb"

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
        nitrate_IDW = "nitrate_IDW"
        IDW = nitrate_IDW
        nitrate_IDW = arcpy.sa.Idw(well_nitrate_OG, "nitr_ran", "0.017616319278512", kValue, "VARIABLE 12", "")
        nitrate_IDW.save(IDW)

        # Process: Zonal Statistics as Table (Zonal Statistics as Table) (sa)
        CancerZonalStats = "CancerZonalStats"
        Output_Join_Layer = ""
        arcpy.sa.ZonalStatisticsAsTable(cancer_tracts_OG, "GEOID10", nitrate_IDW, CancerZonalStats, "DATA", "ALL", "CURRENT_SLICE", [90], "AUTO_DETECT", "ARITHMETIC", 360, Output_Join_Layer)

        # Process: Add Join (Add Join) (management)
        cancer_tracts_OG_2_ = arcpy.management.AddJoin(in_layer_or_view=cancer_tracts_OG_3_, in_field="GEOID10", join_table=CancerZonalStats, join_field="GEOID10")[0]

        # Process: Ordinary Least Squares (OLS) (Ordinary Least Squares (OLS)) (stats)
        OLS_fc_shp = "OLS_fc"
        Coefficient_Output_Table = ""
        Diagnostic_Output_Table = ""
        OLS_Report = "C:\\777p1\\OLS_Report.pdf"
        arcpy.stats.OrdinaryLeastSquares(Input_Feature_Class=cancer_tracts_OG_2_, Unique_ID_Field="CancerZonalStats.ZONE_CODE", Output_Feature_Class=OLS_fc_shp, Dependent_Variable="cancer_tracts_OG.canrate", Explanatory_Variables=["CancerZonalStats.MEAN"], Coefficient_Output_Table=Coefficient_Output_Table, Diagnostic_Output_Table=Diagnostic_Output_Table, Output_Report_File=OLS_Report)

        # Process: Save To Layer File (Save To Layer File) (management)
        OLS_fc_layer_lyrx = "C:\\777p1\\ArcGISPro\\Geog777_P1\\OLS_fc_layer.lyrx"
        print(f"Saving OLS_fc_shp to {OLS_fc_layer_lyrx}")
        if arcpy.Exists(OLS_fc_shp):
            print(f"Layer {OLS_fc_shp} exists.")
        else:
            print(f"Error: Layer {OLS_fc_shp} does not exist.")
            return

        try:
            arcpy.management.SaveToLayerFile(in_layer=OLS_fc_shp, out_layer=OLS_fc_layer_lyrx, is_relative_path="ABSOLUTE")
            print(f"Layer file {OLS_fc_layer_lyrx} created successfully.")
        except arcpy.ExecuteError:
            print(f"Failed to create layer file {OLS_fc_layer_lyrx}.")
            print(arcpy.GetMessages())
            return

        # Process: Make Raster Layer (Make Raster Layer) (management)
        IDW_Raster = "IDW_Raster"
        arcpy.management.MakeRasterLayer(in_raster=nitrate_IDW, out_rasterlayer=IDW_Raster)

        # Process: Save To Layer File (2) (Save To Layer File) (management)
        IDW_LayerFile_lyrx = "C:\\777p1\\ArcGISPro\\Geog777_P1\\IDW_LayerFile.lyrx"
        print(f"Saving IDW_Raster to {IDW_LayerFile_lyrx}")
        try:
            arcpy.management.SaveToLayerFile(in_layer=IDW_Raster, out_layer=IDW_LayerFile_lyrx, is_relative_path="ABSOLUTE")
            print(f"Layer file {IDW_LayerFile_lyrx} created successfully.")
        except arcpy.ExecuteError:
            print(f"Failed to create layer file {IDW_LayerFile_lyrx}.")
            print(arcpy.GetMessages())
            return


def userClick():
    userInputValue = userInput.get()
    global kValue
    try:
        kValue = int(userInputValue)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer value for K")
        return

    if kValue <= 0:
        messagebox.showerror("Invalid Input", "Please enter a value greater than 0")
        return

    # Call the Model function with kValue
    Model(kValue)


if __name__ == '__main__':
    # Creating a label widget
    pgTitle = tk.Label(root, text="Linear Regression Analysis of Cancer Rates \nvs. Nitrate Concentrations in Wisconsin", font=("Helvetica", 16))
    pgTitle.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Adding well image
    original_image1 = Image.open(r"C:\777p1\ArcGISPro\Geog777_P1\Well_JPG_2.jpg")
    resized_image1 = original_image1.resize((600, 450))  # Resize the image 
    well_image = ImageTk.PhotoImage(resized_image1)
    well_label = tk.Label(image=well_image)
    well_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Creating a label for the entry widget
    entryLabel = tk.Label(root, text="Enter a value K > 0", font=("Helvetica", 14, "bold"))
    entryLabel.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Creating entry widget
    userInput = tk.Entry(root, width=5, borderwidth=3)
    userInput.grid(row=3, column=0, columnspan=2,  padx=10, pady=10)
   
    # Creating a button widget
    myButton = tk.Button(root, text="Run IDW and OLS Analysis", command=userClick, bg="light green", font=("Helvetica", 12))
    myButton.grid(row=4, column=0, columnspan=2, padx=0, pady=10)

    # Creating restart button widget
    restartButton = tk.Button(root, text="Restart", command=restart_program, bg="red", font=("Helvetica", 12))
    restartButton.grid(row=5, column=0, columnspan=2, padx=0, pady=10)

    # Configure column weights for centering
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    # Create event loop
    root.mainloop()