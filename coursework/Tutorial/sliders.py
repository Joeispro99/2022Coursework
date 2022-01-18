from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('yes')
root.geometry("400x400")

Vertical = Scale(root, from_=0, to=200)
Vertical.pack()

Horizontal = Scale(root, from_=0, to=200, orient=HORIZONTAL)
Horizontal.pack()

def show():
    a = Label(root, text=Vertical.get()).pack()
    root.geometry(str(Horizontal.get()) + "x" + str(Vertical.get()))
btn = Button(root, text="Click me", command=show).pack()

root.mainloop()
