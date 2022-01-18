
from tkinter import *

# Creating a window
root = Tk()

# Creating a label widget
labelOne = Label(root, text="Hello, World!").grid(row=0,column=0)
labelTwo = Label(root, text="Goodbye, World!").grid(row=1,column=0)

#On the same column but different row

root.mainloop()
