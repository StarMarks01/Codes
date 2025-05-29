i=0                                         #starting point for loop
num=int(input("Enter he value In num:"))    #Number Of times it has to be repeated
ff = []                                     #Empty List
while i<num:                                #while 0 less than inputted value
    a=int(input("Enter Integer Number:"))   #enter a int value
    f={"Int":a}                             #automatically adds int and sting in  dictionary
    ff.append(f)                            #adds value in dictionary in list
    i+=1                                    #ends while loop
print(f)                                   #prints list