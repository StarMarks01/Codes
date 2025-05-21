import matplotlib.pyplot as mp
import csv
import seaborn as sn
import numpy as np
import pandas as pd

label = ['Work Hours','Sleep Hours','Excercise Hours','Learning Hours']

work = [1,2,8,3,3.5]
sleep = [1,2,3,6,17]
gym = [1,2,3,4,4.5]
study = [1.1,2.5,3.3,4.1,5.4]

x = [1, 2, 3, 4]
y = [4,2,1,1.5,3]
x2 = [2,4,6,8,10,12]
y2 = [4,5,7,8,9,10]

m = [34,64,53,42,12,32,44,55,64,23]
f = [10,20,30,40,50,60,70,80,90,100]

age = [54,66,34,76,78,34,43,23,21,33,12,45,32,34,11,12,9,7,8,97,100]
bin = [0,10,20,30,40,50,60,70,80,90,100]

mp.title("This Is A Python Project :)")
mp.ylabel("This Is Y Axis")
mp.xlabel("This Is X Axis")
mp.plot(x,y)
mp.show()

x = [1,3,5,7,9,11]
y = [3,5,7,9,11,12]
mp.plot(x,y,label="Line 1",color = "black")
mp.plot(x2,y2,label="Line 2",color = "red")
mp.title("AGI")
mp.xlabel("This Is X-Axis")
mp.ylabel("This Is Y-Axis")
mp.legend()
mp.show()

mp.bar(x,y,label="line 1",color="black")
mp.bar(x2,y2,label="line 2",color="red")
mp.title("This Is Part Of Data Analysist Course")
mp.xlabel("X Axis")
mp.ylabel("Y Axis")
mp.legend()
mp.show()

mp.bar(x,y,label="Bar - 1")
mp.bar(x2,y2,  label = "Bar - 2", color = "red")
mp.legend()
mp.show()


mp.plot(x,y,label = "Store A")
mp.plot(x2,y2,label = "Store B")
mp.xlabel("Months")
mp.ylabel("Sales")
mp.show()

mp.hist(age,bin,histtype="bar",color="red",label="The A ge Difference",rwidth=0.7)
mp.legend()
mp.ylabel("Population")
mp.xlabel("Age")
mp.title("Matplotlib Histogram :)")
mp.show()

mp.title("This Is A Scatter Chart :)")
mp.scatter(m,f,label = "Scatter 1")
mp.xlabel("Age")
mp.ylabel("Measurement")
mp.legend()
mp.show()

mp.title("This Is A Scatter")
mp.scatter(m,f,color = "red", marker="*")
mp.xlabel("Age")
mp.ylabel("Measurement")
mp.legend()
mp.show()


mp.stackplot(work,sleep,gym,study,labels=['Work Hours','Sleep Hours','Excercise Hours','Learning Hours'])
mp.legend()
mp.show()

mp.pie(x,labels=label)
mp.show()

x = []
y = []
with open('data.txt','r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))
mp.plot(x,y)
mp.xlabel("X - Axis")
mp.ylabel("Y - Axis")
mp.title("Loading Data From File")
mp.show()