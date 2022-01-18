from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import time

root = Tk()
root.title('First Window')


def opensecondwindow():
    global my_img
    top = Toplevel()
    top.title('Big Brain')
    my_img = ImageTk.PhotoImage(Image.open("a.png"))
    img_label = Label(top,image=my_img).pack()
    btn_2 = Button(top,text="Close Window",command=top.destroy).pack()


btn = Button(root,text="Open Second Window",command=opensecondwindow).pack()

root.mainloop()
