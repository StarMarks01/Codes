while True:
    n = int(input("Enter A Number:"))
    i = 1
    while i<10:
        print(n,"*",i,"=",n*i)
        i = i+1
    exit = int(input("Enter 1 To Exit:"))
    if exit == 1:
        print("Exitting...")
        break
    else:
        print("Going Back!")