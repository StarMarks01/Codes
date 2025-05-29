# import tkinter as tk
# root = tk.Tk()
# title = tk.Label(root,text='This is a Test')
# title.pack()
# tk.mainloop()

# from tkinter import *
# root = Tk() # Frame Created

# title = Label(root,text='This is a Test') # label Created
# title.pack() # add into Frame

# button = Button(root,text='Submit')
# button.pack()
# mainloop()
from tkinter import *
root = Tk() # Frame Created
root.geometry('200x300')
title = Label(root,text='This is a Test') # label Created
title.grid(row=0,column=0) # add into Frame

button = Button(root,text='Submit')
button.grid(row=1,column=0)

name = Entry(root)
name.grid(row=2,column=0)

ch1 = Checkbutton(root)
ch1.grid(row=3)

r1 = Radiobutton()
r1.grid(row=4)




mainloop()