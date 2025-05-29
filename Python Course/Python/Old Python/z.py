import tkinter as tk
from tkinter import *
import mysql.connector as db

mydb = db.connect(
host="localhost",
user="yagneshDB",
password="Yagnesh@123"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS yagneshdatabase")

mycursor.execute("CREATE TABLE IF NOT EXISTS yagneshdatabase.schooldata (name VARCHAR(100), class VARCHAR(100), phone VARCHAR(13), roll VARCHAR(100))")

root=tk.Tk()

root.geometry('700x600',)

root.title("Make A Form Task")

# menubar=Menu(root)
# root.config(menu=menubar)

nameTitle=Label(root,text="Name:")
nameTitle.grid(column=0,row=0, padx=10, pady=10)

nameEntry=Entry(root)
nameEntry.grid(column=1,row=0)

classTitle=Label(root,text="Class")
classTitle.grid(column=0,row=1, padx=10, pady=10)

classEntry=Entry(root)
classEntry.grid(column=1,row=1)

title4=Label(root,text="Phone Number:")
title4.grid(column=0,row=2, padx=10, pady=10)

phoneEntry=Entry(root)
phoneEntry.grid(column=1,row=2)

title6=Label(root,text="Roll Call:")
title6.grid(column=0,row=3, padx=10, pady=10)

rollEntry=Entry(root)
rollEntry.grid(column=1,row=3)

title8=Label(root,text="Hobbies:")
title8.grid(column=0,row=4, padx=10, pady=10)

badmintonVar = IntVar()
badmintonCheck=Checkbutton(root,text="Badminton",variable=badmintonVar)
badmintonCheck.grid(column=0,row=5)

swimmingVar = IntVar()
swimmingCheck=Checkbutton(root,text="Swimming",variable=swimmingVar)
swimmingCheck.grid(column=1,row=5)

runningVar = IntVar()
runningCheck=Checkbutton(root,text="Running",variable=runningVar)
runningCheck.grid(column=2,row=5)

readingVar = IntVar()
readingCheck=Checkbutton(root,text="Reading",variable=readingVar)
readingCheck.grid(column=3,row=5)

title9=Label(root,text="Gender")
title9.grid(column=0,row=6, padx=10, pady=10)

genderVar = IntVar()
r1 = Radiobutton(root,text="Male",value=1,variable=genderVar) 
r1.grid(column=0,row=7)

r2 = Radiobutton(root,text="Female",value=2,variable=genderVar)
r2.grid(column=1,row=7)


list1=[1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,
    1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,
    1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]

list1 = [x for x in range(1950, 2024)]

list2=['Afghanisthan', 'Albania', 'America', 'Dune', 
        'India', 'Indonesia', 'Japan', 'Mexico', 'New Gearsy',
        'Notrh Korea', 'Pakistan', 'South Korea', 'United Kingdom', 'Wano']

Var1=tk.StringVar()

Var1.set("What is your Birth Year?")

select1=tk.OptionMenu(root,Var1,*list1)
select1.grid(column=0,row=8, padx=10, pady=10)

Var2=tk.StringVar()
Var2.set("Select Your Country:")

select2=tk.OptionMenu(root,Var2,*list2)
select2.grid(column=0,row=9, padx=10, pady=10)
def register():
    name = nameEntry.get()
    classs = classEntry.get()
    phone = phoneEntry.get()
    rollCall = rollEntry.get()
    hobbiesTuple = ((badmintonVar,'Badminton'),
                    (swimmingVar,'Swimming'),
                    (runningVar,'Running'),
                    (readingVar,'Reading'))
    hobbie = [x[1] for x in hobbiesTuple if x[0].get()==1]
    gender = genderVar.get()
    birth_year = Var1.get()
    country = Var2.get()
    print('Name:',name)
    print('Class:',classs)
    print('Phone:',phone)
    print('Roll Call:',rollCall)
    print(hobbie)
    print(gender)
    print(birth_year)
    print(country)

button1=Button(root,text="Submit",command=register)
button1.grid(column=0,row=10, padx=10, pady=10)


root.mainloop()
