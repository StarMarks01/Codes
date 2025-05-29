a=int(input("Enter The Value Of A="))
b=int(input("Enter The Value Of B="))
c=int(input("Enter The Value Of C="))
total=a+b+c
percentage=total/3
print(f"The students total is {total} and percentage is {percentage}")
if(percentage>100):
    print("Invalid Input")
elif(percentage>90):
    print("A+")
elif(percentage>80):
    print("A")
elif(percentage>70):
    print("A-")
elif(percentage>60):
    print("B+")
elif(percentage>50):
    print("B-")
elif(percentage>40):
    print("C+")
elif(a>=33 and b>=33 and c>=33):
    print("Pass only")
else:
    print("Fail in One Or Multiple Subjects")
