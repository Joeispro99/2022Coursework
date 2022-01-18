from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()

def popup():
    response = messagebox.askyesno(title="This is my popup", message="Hello World", icon="info")
    Label(root, text="Yes" if response == 1 else "No").pack()

    #showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
    #askquestion returns the answer as 1 0 while askyesno returns yes no
    #ok button returns ok
    #cancel button returns cancel

Button(root, text="Popup", command=popup).pack()

root.mainloop()
