"""
Similar to subnetCalculator.py but in this file I will make it where you can see
the results in a UI window 
"""

import tkinter
from tkinter import Tk
from tkinter import ttk


root = Tk()
root.geometry("500x500")


frame = ttk.Frame(root, padding=100)
frame.grid()

label = ttk.Label(frame, text = "hello World").grid(column = 0, row = 0)

quitButton = ttk.Button(frame, text= "Quit", command=root.destroy).grid(column= 1, row = 0)
numButton = ttk.Button(frame,text = "Add 1").grid(column= 1 , row=1)


textBox = tkinter.Text(root, height= 3, width= 20)
textBox.grid(column=0, row=1)
box = """Whats up"""

textBox.insert(tkinter.END, box)


root.mainloop()