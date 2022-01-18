from tkinter import *
from PIL import ImageTk, Image

root = Tk()

r = IntVar()
#when variable changes, will get the variable value
# StrVar() exists

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
    ]

pizza = StringVar()
pizza.set("Pepperoni")

for i, j in MODES:
    Radiobutton(root,text=i,variable=pizza,value=j).pack(anchor=W)
myButton = Button(root,text="Ordeer!", command=lambda:clicked(pizza.get())).pack()

def clicked(value):
    myLabel = Label(root, text=value).pack()
'''
Radiobutton(root, text="Option 1", variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r,value=2,command=lambda:clicked(r.get())).pack()
'''
root.mainloop()
