import tkinter as tk
from tkinter import *

root=tk.Tk()

root.geometry('700x600',)

root.title("Make A Form Task")

title0=Label(root,text="Name:")
title0.grid(column=0,row=0, padx=10, pady=10)

title1=Entry(root)
title1.grid(column=1,row=0)

title2=Label(root,text="Class")
title2.grid(column=0,row=1, padx=10, pady=10)

title3=Entry(root)
title3.grid(column=1,row=1)

title4=Label(root,text="Phone Number:")
title4.grid(column=0,row=2, padx=10, pady=10)

title5=Entry(root)
title5.grid(column=1,row=2)

title6=Label(root,text="Roll Call:")
title6.grid(column=0,row=3, padx=10, pady=10)

title7=Entry(root)
title7.grid(column=1,row=3)

title7=Label(root,text="Roll Call:")
title7.grid(column=0,row=3, padx=10, pady=10)

title8=Label(root,text="Hobbies:")
title8.grid(column=0,row=4, padx=10, pady=10)

ch1=Checkbutton(root,text="Badminton")
ch1.grid(column=0,row=5)

title7=Checkbutton(root,text="Swimming")
title7.grid(column=1,row=5)


title7=Checkbutton(root,text="Running")
title7.grid(column=2,row=5)


title7=Checkbutton(root,text="Reading")
title7.grid(column=3,row=5)

title9=Label(root,text="Gender")
title9.grid(column=0,row=6, padx=10, pady=10)

r1 = Radiobutton(root,text="Male",value=1) 
r1.grid(column=0,row=7)

r2 = Radiobutton(root,text="Female",value=2)
r2.grid(column=1,row=7)


# list1=[1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,
#     1974,1975,1976,1977,1978,1979,1980,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,
#     1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]

list1 = [x for x in range(1950, 2024)]

list2=['Afghanisthan', 'Albania', 'America', 'Dune', 
        'India', 'Indonesia', 'Japan', 'Mexico', 'New Gearsy',
        'Notrh Korea', 'Pakistan', 'South Korea', 'United Kingdom', 'Wano']

Var1=tk.StringVar()

v=StringVar()

Var1.set("What is your Birth Year?")

def get_optionMenu_selection(variable):
    print(variable.get())

select1=tk.OptionMenu(root,Var1,*list1)
select1.grid(column=0,row=8, padx=10, pady=10)

Var2=tk.StringVar()
Var2.set("Select Your Country:")

select2=tk.OptionMenu(root,Var2,*list2)
select2.grid(column=0,row=9, padx=10, pady=10)

button1=Button(root,text="Submit",command=root.quit)
button1.grid(column=0,row=10, padx=10, pady=10)

root.mainloop()
