import datetime as dt
file_name = open('C:/Users/user/Desktop/CSCI115/Assignments/note.txt', 'r')
checker = True
def addNote(file_name, message):
  file_name.write(dt.datetime.today().strftime("%d/%m/%Y: ")+ message + '\n')
def readDayNote(file_name, date):
    list_notes = []
    lines = file_name.readlines()
    for line in lines:
        if line[0:10] == date:
            new_line = line[12:(len(line)-1)]
            list_notes.append(new_line)
    if list_notes == []:
        raise ValueError("Sorry! No notes with such date")
    else:
        for mes in list_notes:
            print(date+": "+mes)
def readAllNotes(file_name):
    lines = file_name.readlines()
    for line in lines:
        print(line.rstrip())
def deleteNote(file_name, date):
    list_notes = []
    counter = 1
    lines = file_name.readlines()
    for line in lines:
        if line[0:10] == date:
            new_line = line[12:(len(line)-1)]
            list_notes.append(new_line)
    if list_notes == []:
        raise ValueError("Sorry! No notes with such date")
    else:
        for mes in list_notes:
            
            print(str(counter)+ ") "+ date+": "+mes)
            counter = counter + 1
        with open("C:/Users/user/Desktop/CSCI115/Assignments/note.txt", 'r+') as nt:
            lines = nt.readlines()
            nt.seek(0)
            nt.truncate()
            choose = int(input('The number of the line you want to delete from 1 to %d: '%len(list_notes)))
            for number, line in enumerate(lines):
                if number not in [choose-1, choose-1] :
                    nt.write(line)
while checker == True:
    try: 
        print("What do you want to do? (add note - a, read day note - r, all notes - s, delete note - d, to stop - end)")
        chooser = str(input("Enter your answer here: "))
        if chooser == "a":
            message = str(input("Enter the message: "))
            file_name = open('C:/Users/user/Desktop/CSCI115/Assignments/note.txt', 'a')
            addNote(file_name, message)
        if chooser == "r" :
            date = str(input("Enter the date: "))
            file_name = open('C:/Users/user/Desktop/CSCI115/Assignments/note.txt', 'r')
            readDayNote(file_name, date)
        if chooser == "s":
            file_name = open('C:/Users/user/Desktop/CSCI115/Assignments/note.txt', 'r')
            readAllNotes(file_name)
        if chooser == "d":
            date = str(input("Enter the date: "))
            file_name = open('C:/Users/user/Desktop/CSCI115/Assignments/note.txt', 'r+')
            deleteNote(file_name, date)
        if chooser == "end":
            break
    except ValueError:
        print("Sorry! No notes with such date!")