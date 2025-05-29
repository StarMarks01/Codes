while True:
    marks = int(input("enter Student Marks:"))

    if marks >= 90:
        print("A+")
    elif marks >= 80:
        print("A-")
    elif marks >= 70:
        print("B+")
    elif marks >= 60:
        print("B-")
    elif marks >= 50:
        print("C+")
    elif marks < 50:
        print("FF")
    
    exit = int(input("Exit?\nPress: 1 To Exit:"))

    if exit == 1:
        print("Exitting")
        break
    else:
        print("Going Back!")