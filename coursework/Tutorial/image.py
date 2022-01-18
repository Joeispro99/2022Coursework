from tkinter import *
from PIL import ImageTk, Image

root = Tk()
#root.iconbitmap('directory')

my_img = ImageTk.PhotoImage(Image.open("bigbrain.png"))
img_label = Label(image=my_img)
img_label.pack()

'''
button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
'''

root.mainloop()
