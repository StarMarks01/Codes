list1=[1,2,22,45,23,11,33]
i=0
while i<len(list1):
    if list1[i]>=20:
        list1[i]-=20
    i+=1
print(list1)