f=int(input("Enter Value In F="))
list1=[1,2,3,4,5]
isContain = False
for i in list1:
    if i == f:
        isContain = True
        break
if(isContain):
    print(f"{f} Is In List")