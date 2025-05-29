list1 = []
i = 0
while True:
    num = int(input("Enter A Number:"))
    list1.append(num)
    exit = int(input("Done??:"))
    i+=1
    if exit == 1:
        print("Exitting...")
        break
print(list1)