from tkinter import *

dictionaryOfSubjectsAndPriority = {}
dictionaryOfStudyTimeEveryDayInMinutes = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}

timetableLayout = {'Monday': "", 'Tuesday': "", 'Wednesday': "", 'Thursday': "", 'Friday': "", 'Saturday': "", 'Sunday': ""}

#DUMMY DATA
dictionaryOfSubjectsAndPriority = {'English': 2, 'Chinese': 1, 'Chemistry': 3, 'Computing': 4}
# 4 is highest priority, 1 is lowest priority
dictionaryOfStudyTimeEveryDayInMinutes = {'Monday': 60, 'Tuesday': 50, 'Wednesday': 40, 'Thursday': 10, 'Friday': 100, 'Saturday': 60, 'Sunday': 90}

#how it works:
#if time have > studytimepersession, no rest L
#first study session shld be most priority then second then til last then repeat
#i.e. current dummy data has 41 min every session
#Monday spends 41 min on Computing and 19 min on Chemistry
#Tuesday spends 22 min of Chemistry and 28 min of English

def factorial_add(n):
    total = 0
    while n>0:
        total += n
        n-=1
    return total

def createTimetable():
    top = Toplevel()
    top.title = "Create Timetable"
    top.geometry("400x400")
    #inputs:
    #slider how many subject
    #for loop to iterate through subjects
    #text field - Subject
    #text field - Priority
    #button - Submit
    #slider - Study Time for each Study Session
    #slider - Rest Time for each Study Session
    #pack_forget to hide and pack to show
    asianmode = False
    sumOfSessions = 0
    for i in dictionaryOfSubjectsAndPriority:
        sumOfSessions += dictionaryOfSubjectsAndPriority[i]
    totalStudyTime = 0
    for i in dictionaryOfStudyTimeEveryDayInMinutes:
        totalStudyTime += dictionaryOfStudyTimeEveryDayInMinutes[i]
    studyTimePerSession = totalStudyTime/sumOfSessions
    studyTimePerSession = int(studyTimePerSession)
    # round down to nearest 5 to give rest time
    # if < 10 get rid and do another day
    # tell them there's rest time
    # split rest time into break time during subjects
    # if rest break < 5 or subjects < 1
    # if rest break < 5, add break if option to not be rigid ticked
    # Asian Mode: no rest break, no rounding down
    # additional feature:
    # multiple scheudles stored:
    # home schedule, holiday schedule
    # dark mode
    prioritySort = [""] * len(dictionaryOfSubjectsAndPriority)
    maxPriority = minPriority = 0
    for i in dictionaryOfSubjectsAndPriority:
        prioritySort[dictionaryOfSubjectsAndPriority[i]-1] = i
    prioritySort = prioritySort[::-1]
    prioritySort2 = []
    maxPriority = len(prioritySort)
    for i in range(maxPriority):
        prioritySort2 += prioritySort
        prioritySort.pop(-1)
    #LayoutFormat: Subject/Duration, Subject/Duration
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
                prioritySort2.pop(0)
            if dictionaryOfStudyTimeEveryDayInMinutes[i] < studyTimePerSession:
                remainingTime = studyTimePerSession - dictionaryOfStudyTimeEveryDayInMinutes[i]
                timetableLayout[i] += prioritySort2[0] + "/" + str(dictionaryOfStudyTimeEveryDayInMinutes[i]) + " "
                dictionaryOfStudyTimeEveryDayInMinutes[i] = 0
            else:
                dictionaryOfStudyTimeEveryDayInMinutes[i] = dictionaryOfStudyTimeEveryDayInMinutes[i] - studyTimePerSession
                timetableLayout[i] += prioritySort2[0] + "/" + str(studyTimePerSession) + " "
                prioritySort2.pop(0)
        if not asianmode:
            for i in timetableLayout:
                scheduleForTheDay = timetableLayout[i].split(" ")
                for i in scheduleForTheDay:
                    print(scheduleForTheDay.split("/"))
    # note:
    # most priority goes to most time
    print(timetableLayout)
