import arcpy
from arcpy.sa import *

import tkinter as tk

root = tk.Tk()
root.title("Linear Regression Analysis of Cancer Rates vs. Nitrate Concentrations in Wisconsin")

def userClick():
    userInputValue = userInput.get()
    print(userInputValue)
        

# Creating a label widget
pgTitle = tk.Label(root, text="Linear Regression Analysis of Cancer Rates \nvs. Nitrate Concentrations in Wisconsin", font=("Helvetica", 16))
pgTitle.pack()

# Creating a label for the entry widget
entryLabel = tk.Label(root, text="Enter a value K > 0", font=("Helvetica", 12))
entryLabel.pack(anchor='center', padx=10)

# Creating entry widget
userInput = tk.Entry(root, borderwidth=3)
userInput.pack()
userInput.insert(2, "2")
kValue = (userInput.get())
print(kValue)

# Creating a button widget
myButton = tk.Button(root, text="Run IDW", command=userClick)
myButton.pack()

# Create event loop
root.mainloop()

