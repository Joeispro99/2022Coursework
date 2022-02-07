import firebase_admin
from firebase_admin import db
import json
from datetime import datetime
from tkinter import *
from main import chatframe

cred_obj = firebase_admin.credentials.Certificate('courseworkchat-6e52c-firebase-adminsdk-q3nbz-f8e72a513c.json')
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://courseworkchat-6e52c-default-rtdb.firebaseio.com/'
})

signed_in = False

def check(username,password):
    ref = db.reference("/passwords/")
    for i in ref.get():
        if username != i:
            Label(chatframe, text="No account registered with this username!")
        elif password != ref.get()[i]:
            Label(chatframe, text="Incorrect password!")

print("nani")
check()

if signed_in:
    pass
else:
    username_text_field = Entry(chatframe, width=50)
    username_text_field.pack()
    password_text_field = Entry(chatframe, width=50)
    password_text_field.pack()
    submit_button = Button(chatframe, text="Sign in", command=check)

'''
username = input("What is your name?\n")
teacher=input("Which teacher would you like to send your message to?\n")
ref = db.reference(("/" + teacher + "-" + username))

data = {
    'messages' : [
    ]
}

json_string = json.dumps(data)
with open('book_info.json', 'w') as outfile:
    outfile.write(json_string)

with open("book_info.json", "r") as f:
	file_contents = json.load(f)
ref.set(file_contents)

while True:
    userinput = input()
    if userinput == "send":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        message = input("What message would you like to send?\n")
        data['messages'].append({'time': current_time, 'message_text': message, 'sender': username})

        json_string = json.dumps(data)
        with open('book_info.json', 'w') as outfile:
            outfile.write(json_string)

        with open("book_info.json", "r") as f:
            file_contents = json.load(f)
        ref.set(file_contents)

    elif userinput == "read":
        data2 = ref.get()
        data3 = data2['messages']
        for i in data3:
            print("{} sent {} at {}".format(i['sender'], i['message_text'], i['time']))



'''
'''
path is under teacher

parameters for message

- time
- message_text
- sender

'''

#db.reference()