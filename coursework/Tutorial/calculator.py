
from tkinter import *

# Creating a window
root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5, fg="blue")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "add":
        e.insert(0,str(fnum + int(second_number)))
    elif math == "subtract":
        e.insert(0,str(fnum - int(second_number)))
    elif math == "multiply":
        e.insert(0,str(fnum * int(second_number)))
    elif math == "divide":
        e.insert(0,str(fnum / int(second_number)))

def operation(a):
    first_number = e.get()
    global fnum
    global math
    math = a
    fnum = int(first_number)
    e.delete(0,END)


button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_add(1)).grid(row=1,column=0)
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_add(2)).grid(row=1,column=1)
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_add(3)).grid(row=1,column=2)
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_add(4)).grid(row=2,column=0)
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_add(5)).grid(row=2,column=1)
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_add(6)).grid(row=2,column=2)
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_add(7)).grid(row=3,column=0)
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_add(8)).grid(row=3,column=1)
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_add(9)).grid(row=3,column=2)
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_add(0)).grid(row=4,column=0)

buttonequal = Button(root, text="=", padx=160, pady=20, command=button_equal).grid(row=6,column=0,columnspan=3)
buttonclear = Button(root, text="C", padx=40, pady=20, command=button_clear).grid(row=5,column=0,columnspan=1)

buttonadd = Button(root, text="+", padx=40, pady=20, command=lambda:operation("add")).grid(row=4,column=1)
buttonsubtract = Button(root, text="-", padx=40, pady=20, command=lambda:operation("subtract")).grid(row=4,column=2)
buttonmultiply = Button(root, text="*", padx=40, pady=20, command=lambda:operation("multiply")).grid(row=5,column=1)
buttondivide = Button(root, text="/", padx=40, pady=20, command=lambda:operation("divide")).grid(row=5,column=2)


root.mainloop()
