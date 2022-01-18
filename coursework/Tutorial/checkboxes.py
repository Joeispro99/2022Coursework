from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('yes')
root.geometry("400x400")

var = IntVar()

c = Checkbutton(root, text="Check1", variable=var)
#onvalue and offvalue for StrVar
c.deselect()
c.pack()

def show():
    myLabel = Label(root,text=var.get()).pack()
btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()
