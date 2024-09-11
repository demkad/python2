import tkinter as tk

############### VENSTER ############### 
# create window
window = tk.Tk()
# title window: 
window.title("Python developer les 2")
# size:
window.geometry("800x600")
############### VENSTER ############### 


############### FEATURES ############### 
# Knopje
knop = tk.Button(window) 
# Plaats knopje in venster
knop.place(x=100,y=100)

############### FEATURES ############### 







############### TEST ############### 
window.mainloop()
############### TEST ############### 
