#Aim:- make use of random function in numpy make 5 ruppee variables and add them all and store the answer in another variable user's variableusv
from numpy import *
rs1 = 100
rs2 = 100
rs3 = 100
rs4 = 100
rs5 = 100
usv = 0
arry1 = array(random.randint([rs1,rs2,rs3,rs4,rs5]))
sum = 0
i = 0
while i<len(arry1):
    sum = sum + arry1[i]
    i+=1
print(f"The Random Rupees that will go to user is :- {arry1}")
print(f"The Sum Of Rupees in Random is:- {sum}")