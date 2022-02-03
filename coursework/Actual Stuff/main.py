# This is a sample Python script.
import random
from tkinter import *
from tkinter import ttk
from timetable import createTimetable, timetableLayout
import random
from tips import tips
from PIL import ImageTk, Image

root = Tk()
root.title("Display Window")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(str(screen_width) + "x" + str(screen_height))

notebook = ttk.Notebook(root)
notebook.pack(ipadx=screen_width,ipady=screen_height)

frame1 = LabelFrame(notebook, text="Sections",padx=5,pady=5)
timetableframe = LabelFrame(notebook, text="",width=screen_width,height=screen_height)
chatframe = LabelFrame(notebook, text="")

notebook.add(timetableframe, text="Sections")
notebook.add(chatframe, text="Chat with Teachers")

tip = StringVar()
def tip_loop():
    tip.set(tips[random.randint(0,len(tips)-1)])
    root.after(5000, tip_loop)
tip_loop()
tiplabel = Label(timetableframe, textvariable=tip)
tiplabel.pack(anchor=S+E, side=BOTTOM)

def reloadTimetable():
    if timetableLayout == {'Monday': "", 'Tuesday': "", 'Wednesday': "", 'Thursday': "", 'Friday': "", 'Saturday': "", 'Sunday': ""}:
        label2 = Label(timetableframe, text="You have not created a schedule yet!")
        label2.pack()
        root.after(3000, label2.pack_forget)

if timetableLayout == {'Monday': "", 'Tuesday': "", 'Wednesday': "", 'Thursday': "", 'Friday': "", 'Saturday': "", 'Sunday': ""}:
    nolabel = Label(timetableframe, text="You have not created a schedule")
    nolabel.pack()
    createbtn = Button(timetableframe, text="Create Schedule", command=lambda: createTimetable())
    createbtn.pack()
    reloadbtn = Button(timetableframe, text="Reload Schedule", command=reloadTimetable)
    reloadbtn.pack()
else:
    label1 = Label(timetableframe, text="Timetable")
    label1.pack()

root.mainloop()
