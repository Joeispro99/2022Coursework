from tkinter import *
from PIL import ImageTk, Image

root = Tk()

status = Label(root, text="lorem ipsum", bd=1, relief=SUNKEN,anchor=E).grid(row=0, column=0, sticky=W+E)
#pady in grid to add spacing
#sticky in grid to stretch throughout

root.mainloop()
