# This is a sample Python script.
from tkinter import *
from tkinter import ttk
from timetable import createTimetable, timetableImage
import time
from PIL import ImageTk, Image

root = Tk()
root.title("Display Window")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(str(screen_width) + "x" + str(screen_height))

timetableset = False
notebook = ttk.Notebook(root)
notebook.pack(ipadx=screen_width,ipady=screen_height)

frame1 = LabelFrame(notebook, text="Sections",padx=5,pady=5)
timetableframe = LabelFrame(notebook, text="",width=screen_width,height=screen_height)
chatframe = LabelFrame(notebook, text="")

notebook.add(timetableframe, text="Sections")
notebook.add(chatframe, text="Chat with Teachers")

def reloadTimetable():
    print(timetableImage)
    if timetableImage == None:
        label2 = Label(timetableframe, text="You have not created a schedule yet!")
        label2.pack()
        root.after(3000, label2.pack_forget)

if not timetableset:
    nolabel = Label(timetableframe, text="You have not created a schedule")
    nolabel.pack()
    createbtn = Button(timetableframe, text="Create Schedule", command=createTimetable)
    createbtn.pack()
    reloadbtn = Button(timetableframe, text="Reload Schedule", command=reloadTimetable)
    reloadbtn.pack()
else:
    label1 = Label(timetableframe, text="Timetable")
    label1.pack()

root.mainloop()
