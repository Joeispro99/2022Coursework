
from tkinter import *

# Creating a window
root = Tk()

def clickedOne():
    myLabel = Label(root, text="You clicked me! <3").pack()

buttonOne = Button(root, text="Click Me!", padx=20, pady=20, command=clickedOne, fg="blue", highlightbackground="red").pack()

root.mainloop()
