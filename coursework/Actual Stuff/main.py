# This is a sample Python script.
import random
from tkinter import *
from tkinter import ttk
from timetable import createTimetable, timetableLayout
import time
import threading
import random
from tips import tips
from PIL import ImageTk, Image
import firebase_admin
from firebase_admin import db
from datetime import datetime

cred_obj = firebase_admin.credentials.Certificate('courseworkchat-6e52c-firebase-adminsdk-q3nbz-f8e72a513c.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://courseworkchat-6e52c-default-rtdb.firebaseio.com/'
})

root = Tk()
root.title("Display Window")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(str(screen_width) + "x" + str(screen_height))

notebook = ttk.Notebook(root)
notebook.pack(ipadx=screen_width, ipady=screen_height)

frame1 = LabelFrame(notebook, text="Sections",  padx=5, pady=5)
timetableframe = LabelFrame(notebook, text="", width=screen_width, height=screen_height)
chatframe = LabelFrame(notebook, text="")

notebook.add(timetableframe, text="Timetable")
notebook.add(chatframe, text="Chat with Teachers")

tip = StringVar()


def tip_loop():
    while True:
        tip.set(tips[random.randint(0, len(tips) - 1)])
        time.sleep(5)


threading.Thread(target=tip_loop).start()
tiplabel = Label(timetableframe, textvariable=tip)
tiplabel.pack(anchor=S+E, side=BOTTOM)


def reloadTimetable():
    if timetableLayout == {'Monday': "", 'Tuesday': "", 'Wednesday': "", 'Thursday': "", 'Friday': "", 'Saturday': "", 'Sunday': ""}:
        label2 = Label(timetableframe, text="You have not created a schedule yet!")
        label2.pack()
        root.after(3000, label2.pack_forget)
    else:
        outputTimetable(timetableLayout)


def outputTimetable(ttb):
    for i in ttb:
        outputStr = ""
        counterA = 0
        counterB = 1
        print("\n"+i)
        tempList = ttb[i].strip().replace(" ","/").split("/")
        for i in range(int(len(tempList)/2)):
            if tempList[counterA] != "Breaktime":
                print("Subject: "+tempList[counterA]+" | Duration: "+tempList[counterB]+" mins")
            else:
                print("Take a short break for {} minutes! (You've earned it!)".format(tempList[counterB]))
            counterA += 2
            counterB += 2


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


signed_in = False

global ref
global username
global path

send_img = ImageTk.PhotoImage((Image.open("60525.png")).resize((20, 20)))

path = "/"
ref = db.reference("/")


def hide(widget, seconds):
    time.sleep(seconds)
    widget.pack_forget()


def sendToDatabase(message_text, teacher2):
    # /test/messages
    global current_frame
    if message_text == "":
        return
    ref2 = db.reference(path)
    data = {"sender": username, "recipient": teacher2, "message_text": message_text, "time": datetime.now().strftime("%H:%M:%S")}
    ref2.push(data)
    ref3 = db.reference("/" + teacher2 + "/messages/")
    ref3.push(data)
    wlist = current_frame.winfo_children()
    for i in wlist:
        i.destroy()
    generateFrame(teacher2)


clickedbeforearray = []


def generateFrame(teacher):
    # create scroll bar again
    # messages come in as labels, grid left and right done
    # text field cling to bottom with send button on the right of it done
    # retrieve text with messages done

    global current_frame
    global button_dict_array_for_teachers
    if current_frame is not None:
        current_frame.pack_forget()
        for i in button_dict_array_for_teachers:
            if i['name'] == teacher:
                current_frame = i['teacherframe']
                break
    else:
        for i in button_dict_array_for_teachers:
            if i['name'] == teacher:
                current_frame = i['teacherframe']
                break
    teacher_messages = []

    label_array = []
    for i in db.reference(path).get():
        if db.reference(path + i).get()['recipient'] == teacher or db.reference(path + i).get()['sender'] == teacher:
            teacher_messages.append(db.reference(path+i).get())
    if teacher_messages is not None:
        for i in teacher_messages:
            if i['sender'] == username:
                j = Label(current_frame, text="{} sent {} at {}".format(i['sender'], i['message_text'], i['time']), justify=LEFT,width=50, anchor="s")
                label_array.append(j)
                j.grid(row=teacher_messages.index(i), column=0,sticky=S)
            else:
                j = Label(current_frame, text="{} sent {} at {}".format(i['sender'], i['message_text'], i['time']), justify=RIGHT,width=50, anchor="w")
                label_array.append(j)
                j.grid(row=teacher_messages.index(i), column=1,sticky=W)
    send_message_text_field = Entry(current_frame, width=100)
    send_message_text_field.grid(row=len(teacher_messages), column=0, columnspan=2, sticky="SE")
    send_button = Button(current_frame, image=send_img, command=lambda i=i: sendToDatabase(send_message_text_field.get(), teacher))
    send_button.grid(row=len(teacher_messages), column=2)
    current_frame.pack(expand=1, fill=BOTH, side=BOTTOM)
    # current_frame.grid(row=0,column=0)
    if teacher not in clickedbeforearray:
        threading.Thread(target=lambda teacher2=teacher: justCheckidrc(teacher2)).start()
        clickedbeforearray.append(teacher)


def justCheckidrc(teacher3, previous=None):
    if previous is None:
        previous = db.reference(username + "/messages/").get()
    else:
        if previous != db.reference(username + "/messages/").get():
            previous = db.reference(username + "/messages/").get()
            generateFrame(teacher3)
    time.sleep(5)
    justCheckidrc(teacher3, previous)


def continueOn():
    global ref
    global button_dict_array_for_teachers
    button_dict_array_for_teachers = []
    submit_button.destroy()
    contactsFrame = Frame(chatframe)
    contactsFrame.pack(side=LEFT, fill=Y, ipadx=50)

    canvasInTheContacts = Canvas(contactsFrame)
    canvasInTheContacts.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbarInTheCanvasInTheContacts = ttk.Scrollbar(contactsFrame, orient=VERTICAL, command=canvasInTheContacts.yview)
    scrollbarInTheCanvasInTheContacts.pack(side=RIGHT, fill=Y)

    canvasInTheContacts.configure(yscrollcommand=scrollbarInTheCanvasInTheContacts.set)
    canvasInTheContacts.bind('<Configure>', lambda e: canvasInTheContacts.configure(scrollregion=canvasInTheContacts.bbox("all")))

    frameInTheCanvasInTheContacts = Frame(canvasInTheContacts)

    canvasInTheContacts.create_window((0, 0), window=frameInTheCanvasInTheContacts, anchor=NW)

    # create new thread to check forever whether search bar is updated if yes display different values
    # create button to add new chat with teachers
    # for each teacher in the database, create new button

    # array of teachers
    # teachers is a dict
    # {name: "", messages: [], button: _, teacherframe: _}
    # config button command to when click then
    # frame has text field packed bottom fill x, labels to show chat messages
    # message example:
    # Joe sent Hi! at 00:00:00

    # create button for adding new contacts
    global current_frame
    global path
    global username
    current_frame = None
    path += "messages/"
    ref = db.reference(path)
    teacher_array = []
    if ref.get() is None:
        button_dict_array_for_teachers = []
    else:
        for message_temp in ref.get():
            modifiedPath = path + message_temp
            message = db.reference(modifiedPath).get()
            if message['recipient'] == username:
                if message['sender'] not in teacher_array:
                    teacher_array.append(message['sender'])
                    button_dict_array_for_teachers.append({"name": message['sender'], "messages": message['message_text'], "button": Button(frameInTheCanvasInTheContacts, text=message['sender'], height=5, width=20, command=lambda teacher=message['sender']: generateFrame(teacher)), "teacherframe": Frame(chatframe)})
            if message['sender'] == username:
                if message['recipient'] not in teacher_array:
                    teacher_array.append(message['recipient'])
                    button_dict_array_for_teachers.append({"name": message['recipient'], "messages": message['message_text'], "button": Button(frameInTheCanvasInTheContacts, text=message['recipient'], height=5, width=20, command=lambda teacher=message['recipient']: generateFrame(teacher)), "teacherframe": Frame(chatframe)})
    for i in button_dict_array_for_teachers:
        i['button'].pack(padx=10, pady=5)

    global createNewContactButton
    createNewContactButton = Button(frameInTheCanvasInTheContacts, text="Talk to new contact", command=lambda: createnewcontact(frameInTheCanvasInTheContacts))
    createNewContactButton.pack()


def createnewcontact(frame):
    global createNewContactButton
    global button_dict_array_for_teachers
    top = Toplevel()
    top.geometry("400x400")
    top.title("Create New Contact")
    e = Entry(top, width=50)
    e.insert(0, "Name of contact: ")
    e.pack()

    def submitContact():
        button_dict_array_for_teachers.append({"name": e.get().split(": ")[-1], "messages": "", "button": Button(frame, text=e.get().split(": ")[-1], height=5, width=20, command=lambda teacher=e.get().split(": ")[-1]: generateFrame(teacher)), "teacherframe": Frame(chatframe)})
        button_dict_array_for_teachers[-1]["button"].pack()
        createNewContactButton.pack_forget()
        createNewContactButton.pack(padx=10,pady=5)
        top.destroy()

    submitButton = Button(top, text="Submit Contact Name", command=submitContact)
    submitButton.pack()


def check(username2, password2):
    global ref
    global path
    global username
    ref = db.reference("/passwords/")
    tempref = ref.get()
    haveaccount = False
    for i in ref.get():
        if username2.get() != i:
            continue
        else:
            if password2.get() != tempref[i]:
                wrongpasswordlabel = Label(chatframe, text="Incorrect password!")
                wrongpasswordlabel.pack()
                threading.Thread(target=hide, args=[wrongpasswordlabel, 3]).start()
                haveaccount = True
                break
            else:
                loginlabel = Label(chatframe, text="User logged in!")
                loginlabel.pack()
                threading.Thread(target=hide, args=[loginlabel, 3]).start()
                ref = db.reference("/" + username2.get() + "/")
                path = "/" + username2.get() + "/"
                haveaccount = True
                signed_in = True
                username = username2.get()
                break
    if not haveaccount:
        noaccountlabel = Label(chatframe, text="No account registered with this username!")
        registeredaccountlabel = Label(chatframe, text="Account is now registered with this username and password!")
        noaccountlabel.pack()
        registeredaccountlabel.pack()
        threading.Thread(target=hide, args=[noaccountlabel, 3]).start()
        threading.Thread(target=hide, args=[registeredaccountlabel, 3]).start()
        ref = db.reference("/passwords/" + username2.get() + "/")
        ref.set(password2.get())
        ref = db.reference("/" + username2.get() + "/")
        path = "/" + username2.get() + "/"
        username = username2.get()

    if signed_in:
        username2.destroy()
        password2.destroy()
        continueOn()


def startChat():
    '''
    ref = db.reference("test/messages/")
    ref.push({"sender": "Mr Johari", "recipient": "test", "message_text": "Hey Test!", "time": "00:00:01"})
    '''
    if signed_in:
        pass
    else:
        username_text_field = Entry(chatframe, width=50)
        username_text_field.pack()
        password_text_field = Entry(chatframe, width=50)
        password_text_field.pack()

        global submit_button
        submit_button = Button(chatframe, text="Sign in", command=lambda: check(username_text_field, password_text_field))
        submit_button.pack()


startChat()

root.mainloop()
