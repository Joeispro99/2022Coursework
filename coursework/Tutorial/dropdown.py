from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('yes')
root.geometry("400x400")

options = [
    "Monday",
    "Tuesday",
    "Wedenesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

def show():
    label = Label(root, text=clicked.get()).pack()

btn = Button(root, text="What day is it?", command=show).pack()


root.mainloop()
