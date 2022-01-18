
from tkinter import *

# Creating a window
root = Tk()

e = Entry(root, width=50, fg="blue")
e.pack()
e.insert(0, "Enter your name: ")

def clickedOne():
    myLabel = Label(root, text=e.get()).pack()

buttonOne = Button(root, text="Click Me!", padx=20, pady=20, command=clickedOne, fg="blue", highlightbackground="red").pack()

root.mainloop()
