from tkinter import *
from PIL import ImageTk, Image

root = Tk()

frame = LabelFrame(root, text="This is my frame!",padx=5,pady=5)
frame.pack(padx=10,pady=10)
#padx in pack changes the horizontal distance away from the frame/window

b = Button(frame, text="Don't click here!")
b.pack()

root.mainloop()
