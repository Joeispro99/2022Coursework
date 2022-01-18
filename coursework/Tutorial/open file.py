from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('yes')

def openimg():
    global my_img
    top = Toplevel()
    root.filename = filedialog.askopenfilename(initialdir="/Users/joewong/Desktop/coursework/Tutorial",title="Select Image", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_label = Label(top, image=my_img).pack()

my_btn = Button(root, text="Open File", command=openimg).pack()

root.mainloop()
