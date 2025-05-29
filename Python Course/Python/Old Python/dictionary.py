names = []
roll = []
classes = []
n = 4
i = 0
while i < n:
    name = str(input("Enter Your name:-"))
    rollno = int(input("Enter Your Roll Number:-"))
    classno = int(input("Enter Your Class Number:-"))
    names.append(name)
    roll.append(rollno)
    classes.append(classno)
    i+=1
dicta = {"name":names,"rollno":roll,"class":classes}
print(names)
print(roll)
print(classes)
print(dicta)
