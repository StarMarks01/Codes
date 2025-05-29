from tkinter import *
from db_controller import *

dbCtrl = DbController() # Instance (Object) of DbController
dbCtrl.createDatabase() # Create Database
dbCtrl.createTable()    # Create Table in Database

root=Tk()

root.geometry('700x600')

root.title("Make A Form Task")

dbCtrl.nameVar = StringVar()
dbCtrl.classVar = StringVar()
dbCtrl.phoneVar = StringVar()
dbCtrl.emailVar = StringVar()
dbCtrl.rollVar = StringVar()
dbCtrl.badmintonVar = IntVar()
dbCtrl.swimmingVar = IntVar()
dbCtrl.runningVar = IntVar()
dbCtrl.readingVar = IntVar()
dbCtrl.genderVar = IntVar()
dbCtrl.year = StringVar()
dbCtrl.country = StringVar()
dbCtrl.findVar = StringVar()

######################## NAME INPUT ########################
nameTitle=Label(root,text="Name:")
nameTitle.grid(column=0,row=0, padx=10, pady=10)

nameEntry=Entry(root, textvariable=dbCtrl.nameVar)
nameEntry.grid(column=1,row=0)

######################## CLASS INPUT ########################

classTitle=Label(root,text="Class")
classTitle.grid(column=0,row=1, padx=10, pady=10)

classEntry=Entry(root,textvariable=dbCtrl.classVar)
classEntry.grid(column=1,row=1)

######################## PHONE INPUT ########################

title4=Label(root,text="Phone Number:")
title4.grid(column=0,row=2, padx=10, pady=10)

phoneEntry=Entry(root,textvariable = dbCtrl.phoneVar)
phoneEntry.grid(column=1,row=2)

######################## EMAIL INPUT ########################

title5=Label(root,text="Email")
title5.grid(column=0,row=3, padx=10, pady=10)

emailEntry=Entry(root,textvariable=dbCtrl.emailVar)
emailEntry.grid(column=1,row=3)

######################## ROLL INPUT ########################

title6=Label(root,text="Roll Call:")
title6.grid(column=0,row=4, padx=10, pady=10)

rollEntry=Entry(root,textvariable=dbCtrl.rollVar)
rollEntry.grid(column=1,row=4)

######################## HOBBIES INPUT ########################

title8=Label(root,text="Hobbies:")
title8.grid(column=0,row=5, padx=10, pady=10)

# # # # # # # # # # # # BADMINTON INPUT # # # # # # # # # # # #

badmintonCheck=Checkbutton(root,text="Badminton",variable=dbCtrl.badmintonVar)
badmintonCheck.grid(column=0,row=6)

# # # # # # # # # # # # SWIMMING INPUT # # # # # # # # # # # #

swimmingCheck=Checkbutton(root,text="Swimming",variable=dbCtrl.swimmingVar)
swimmingCheck.grid(column=1,row=6)

# # # # # # # # # # # # RUNNING INPUT # # # # # # # # # # # #

runningCheck=Checkbutton(root,text="Running",variable=dbCtrl.runningVar)
runningCheck.grid(column=2,row=6)

# # # # # # # # # # # # READING INPUT # # # # # # # # # # # #

readingCheck=Checkbutton(root,text="Reading",variable=dbCtrl.readingVar)
readingCheck.grid(column=3,row=6)

######################## GENDER INPUT ########################

title9=Label(root,text="Gender")
title9.grid(column=0,row=7, padx=10, pady=10)

r1 = Radiobutton(root,text="Male",value=1,variable=dbCtrl.genderVar) 
r1.grid(column=0,row=8)

r2 = Radiobutton(root,text="Female",value=2,variable=dbCtrl.genderVar)
r2.grid(column=1,row=8)

######################## YEAR INPUT ########################

dbCtrl.year.set("What is your Birth Year?")

select1=OptionMenu(root,dbCtrl.year,*dbCtrl.years)
select1.grid(column=0,row=9, padx=10, pady=10)

######################## COUNTRY INPUT ########################

dbCtrl.country.set("Select Your Country:")

select2=OptionMenu(root,dbCtrl.country,*dbCtrl.countries)
select2.grid(column=0,row=10, padx=10, pady=10)

######################## FIND INPUT ########################

findEntry=Entry(root,textvariable=dbCtrl.findVar)
findEntry.grid(column=7,row=0)

button2=Button(root,text="Find",command=dbCtrl.findStudent)
button2.grid(column=8,row=0)

######################## SUBMIT BUTTON ########################

button1=Button(root,text="Submit",command=dbCtrl.addStudent)
button1.grid(column=0,row=11)

######################## UPDATE BUTTON ########################

update = Button(root,text="Update",command=dbCtrl.updateStudent)
update.grid(column=1,row=11)
update.configure(highlightthickness=0)

orr=Label(root,text="OR")
orr.grid(column=2,row=11,padx=2,pady=2)

######################## DELETE BUTTON ########################

delete = Button(root,text="Delete",command=dbCtrl.deleteStudent)
delete.grid(column=3,row=11)
delete.configure(highlightthickness=0)


root.mainloop()