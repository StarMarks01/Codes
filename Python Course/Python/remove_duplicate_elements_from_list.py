list1 = []
nod = []
n = int(input("How many elements do you want to add in list1? :-"))
for i in range(1,n):
    num = int(input("Enter Value:-"))
    list1.append(num)
for i in list1:
    if i not in nod:
        nod.append(i)
print(nod)