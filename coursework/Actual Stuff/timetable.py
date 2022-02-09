from tkinter import *
import threading
import time

timetableLayout = {'Monday': "", 'Tuesday': "", 'Wednesday': "", 'Thursday': "", 'Friday': "", 'Saturday': "",
                   'Sunday': ""}

'''

dictionaryOfSubjectsAndPriority = {}
# dictionaryOfStudyTimeEveryDayInMinutes = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}



# DUMMY DATA
dictionaryOfSubjectsAndPriority = {'English': 2, 'Chinese': 1, 'Chemistry': 3, 'Computing': 4}
# 4 is highest priority, 1 is lowest priority
dictionaryOfStudyTimeEveryDayInMinutes = {'Monday': 60, 'Tuesday': 50, 'Wednesday': 40, 'Thursday': 10, 'Friday': 100,
                                          'Saturday': 60, 'Sunday': 90}

'''
# how it works:
# if time have > studytimepersession, no rest L
# first study session shld be most priority then second then til last then repeat
# i.e. current dummy data has 41 min every session
# Monday spends 41 min on Computing and 19 min on Chemistry
# Tuesday spends 22 min of Chemistry and 28 min of English

def timeRounder(studyHours):
    studyHoursList = []
    breakTime = 0
    studyHours = int(studyHours)
    if studyHours < 10:
        studyHours = 0
        breakTime = breakTime + studyHours
    else:
        studyHours = studyHours - studyHours % 5
        breakTime = breakTime + studyHours % 5
    studyHoursList.append(studyHours)
    studyHoursList.append(breakTime)
    return studyHoursList


def zeroRemover(schdWithZero):
    zeroCounter = 0
    for values in schdWithZero:
        if values == '0':
            schdWithZero.pop(zeroCounter - 1)
            schdWithZero.pop(zeroCounter - 1)
        zeroCounter = zeroCounter + 1
    return schdWithZero


def breakTimeGiver(schdNoBreak, studyTimeToday):
    formattedSchedule = ""
    subjectCount = totalStudyTimeToday = 0
    for subjAndTime in schdNoBreak:
        if not subjAndTime.isdigit():
            formattedSchedule = formattedSchedule + subjAndTime + "/"
            subjectCount += 1
        else:
            formattedSchedule = formattedSchedule + subjAndTime + " "
            totalStudyTimeToday += int(subjAndTime)
    if subjectCount - 1 > 0:
        breaktimeCalculation = (studyTimeToday - totalStudyTimeToday) / (subjectCount - 1)
    else:
        breaktimeCalculation = 1
    formattedSchedule = formattedSchedule.strip()
    formattedSchedule = formattedSchedule.replace(" ", " Breaktime/{} ".format(int(breaktimeCalculation)))
    return (formattedSchedule)


def factorial_add(n):
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total


def applyItAll(dictionaryOfSubjectsAndPriority, dictionaryOfStudyTimeEveryDayInMinutes, asianValue):
    studyTimeDict = dictionaryOfStudyTimeEveryDayInMinutes.copy()
    sumOfSessions = 0
    for i in dictionaryOfSubjectsAndPriority:
        sumOfSessions += dictionaryOfSubjectsAndPriority[i]
    totalStudyTime = 0
    for i in dictionaryOfStudyTimeEveryDayInMinutes:
        totalStudyTime += dictionaryOfStudyTimeEveryDayInMinutes[i]
    studyTimePerSession = totalStudyTime / sumOfSessions
    studyTimePerSession = int(studyTimePerSession)
    # round down to nearest 5 to give rest time
    # if < 10 get rid and do another day
    # tell them there's rest time
    # split rest time into break time during subjects
    # if rest break < 5 or subjects < 1
    # if rest break < 5, add break if option to not be rigid ticked
    # Asian Mode: no rest break, no rounding down
    # MARK: additional feature:
    # multiple scheudles stored:
    # home schedule, holiday schedule
    # dark mode
    prioritySort = [""] * len(dictionaryOfSubjectsAndPriority)
    maxPriority = minPriority = 0
    for i in dictionaryOfSubjectsAndPriority:
        prioritySort[dictionaryOfSubjectsAndPriority[i] - 1] = i
    prioritySort = prioritySort[::-1]
    prioritySort2 = []
    maxPriority = len(prioritySort)
    for i in range(maxPriority):
        prioritySort2 += prioritySort
        prioritySort.pop(-1)
    # LayoutFormat: Subject/Duration, Subject/Duration
    excessTime = 0
    remainingTime = 0
    # if excess time > studyTimePerSession, remainingTime = studyTimePerSession - excessTime
    for i in dictionaryOfStudyTimeEveryDayInMinutes:
        while dictionaryOfStudyTimeEveryDayInMinutes[i] > 0:
            if remainingTime > dictionaryOfStudyTimeEveryDayInMinutes[i]:
                timetableLayout[i] += prioritySort2[0] + "/" + str(dictionaryOfStudyTimeEveryDayInMinutes[i]) + " "
                remainingTime -= dictionaryOfStudyTimeEveryDayInMinutes[i]
                dictionaryOfStudyTimeEveryDayInMinutes[i] = 0
                break
            if remainingTime > 0:
                dictionaryOfStudyTimeEveryDayInMinutes[i] = dictionaryOfStudyTimeEveryDayInMinutes[i] - remainingTime
                timetableLayout[i] += prioritySort2[0] + "/" + str(remainingTime) + " "
                remainingTime = 0
                prioritySort2.pop(0) # source of error
            if prioritySort2 == []:
                break
            if dictionaryOfStudyTimeEveryDayInMinutes[i] < studyTimePerSession:
                remainingTime = studyTimePerSession - dictionaryOfStudyTimeEveryDayInMinutes[i]
                timetableLayout[i] += prioritySort2[0] + "/" + str(dictionaryOfStudyTimeEveryDayInMinutes[i]) + " "
                dictionaryOfStudyTimeEveryDayInMinutes[i] = 0
            else:
                dictionaryOfStudyTimeEveryDayInMinutes[i] = dictionaryOfStudyTimeEveryDayInMinutes[i] - studyTimePerSession
                timetableLayout[i] += prioritySort2[0] + "/" + str(studyTimePerSession) + " "
                prioritySort2.pop(0) # another source
    if not asianValue:
        for days in timetableLayout:
            counter = 1
            tempSchedule = timetableLayout[days]
            tempSchedule = tempSchedule.replace("/", " ")
            tempSchedule = tempSchedule.split()
            for studyTime in tempSchedule:
                if studyTime.isdigit() == True:
                    studyTime = timeRounder(studyTime)[0]
                    tempSchedule[counter] = str(studyTime)
                    counter += 2
            timetableLayout[days] = (breakTimeGiver(zeroRemover(tempSchedule), studyTimeDict[days]))
    # note:
    # most priority goes to most time
    returnToHome()
    return timetableLayout


def createTimetable():
    global top
    top = Toplevel()
    top.title = "Create Timetable"
    top.geometry("400x400")

    #applyItAll(dictionaryOfSubjectsAndPriority, dictionaryOfStudyTimeEveryDayInMinutes, False)

    # inputs:
    # slider how many subject
    # for loop to iterate through subjects
    # text field - Subject
    # text field - Priority
    # button - Submit
    # slider - Study Time for each Study Session
    # slider - Rest Time for each Study Session
    # pack_forget to hide and pack to show

    def timeTableInputs():
        sliderLabel = Label(top, text="Use the slider to select the number of subjects!")
        sliderLabel.pack()
        subjectSlider = Scale(top, from_=1, to=10, orient=HORIZONTAL)
        subjectSlider.pack()
        submitButton = Button(top, text="Submit Subjects", command=lambda: submitSlider(subjectSlider.get()))
        submitButton.pack()

        def submitSlider(value):
            sliderLabel.pack_forget()
            submitButton.pack_forget()
            subjectSlider.pack_forget()

            sliderLabel2 = Label(top, text="Use the label to enter the name of the subjects!")
            sliderLabel2.pack()

            text_field_array = []
            for i in range(value):
                e = Entry(top, width=50)
                e.insert(0, "Enter Subject " + str(i + 1) + ": ")
                text_field_array.append(e)
                e.pack()

            def submitSubjectsAndPriority():
                sliderLabel2.pack_forget()
                dictOfSubjectsAndPriority = {}

                sliderLabel3 = Label(top, text="Use the label to enter the priority of the subjects!\n\nThe priority should be an integer,\n the higher the priority, the more sessions given for that subject.\n\nExample: English: 1, Chinese: 2\nChinese has more priority and more time is allocated for Chinese")
                sliderLabel3.pack()

                for i in text_field_array:
                    dictOfSubjectsAndPriority[(i.get().split(":")[-1][1:])] = ""
                for i in text_field_array:
                    j = i.get().split(":")[-1][1:]
                    i.delete(0, 'end')
                    i.insert(0, "Enter Priority for Subject " + j + ": ")
                submitButton2.pack_forget()

                def submitSubjectsAndPriorityAgain():
                    sliderLabel3.pack_forget()
                    for j in dictOfSubjectsAndPriority:
                        dictOfSubjectsAndPriority[j] = int((text_field_array[list(dictOfSubjectsAndPriority.keys()).index(j)].get().split(":")[-1][1:]))
                    submitButton3.pack_forget()
                    for i in text_field_array:
                        i.pack_forget()

                    dayArray = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                    textFieldArray = []
                    for i in dayArray:
                        e = Entry(top, width=50)
                        e.insert(0, "Time available for " + i + ": ")
                        textFieldArray.append(e)
                        e.pack()


                    asianValueAsAnInt = IntVar()
                    asianmode = Checkbutton(top, text="ASIAN MODE ACTIVATE?!", variable=asianValueAsAnInt)
                    asianmode.pack()

                    def TimeEveryDay():
                        #studyTimePerSession = studyTextField.get()
                        dictOfStudyTimeEveryDayInMinutes = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
                        asianValue = asianValueAsAnInt.get() == 1
                        for i in range(len(textFieldArray)):
                            dictOfStudyTimeEveryDayInMinutes[dayArray[i]] = int((textFieldArray[i].get()).split(":")[-1][1:])
                        asianmode.pack_forget()
                        for i in textFieldArray:
                            i.pack_forget()
                        submitButton4.pack_forget()
                        applyItAll(dictOfSubjectsAndPriority, dictOfStudyTimeEveryDayInMinutes, asianValue)

                    submitButton4 = Button(top, text="Submit Study Time and Asian Mode!!!!", command=TimeEveryDay)
                    submitButton4.pack()


                submitButton3 = Button(top, text="Submit Priority", command=submitSubjectsAndPriorityAgain)
                submitButton3.pack()

            submitButton2 = Button(top, text="Submit All Subjects", command=submitSubjectsAndPriority)
            submitButton2.pack()

    timeTableInputs()


def returnToHome():
    byeLabel = Label(top, text="This window will be closed in 3")
    byeLabel.pack()
    def slowlyDisappear():
        for i in range(1,5):
            byeLabel.config(text="This window will be closed in " + str(4-i))
            time.sleep(1)
        top.destroy()
    threading.Thread(target=slowlyDisappear).start()


