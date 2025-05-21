list1 = [32,321,43,54,65]
list2 = []
m = list1[0]
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        if(list1[i]<list1[j]):
            m=list1[i]
            list1[i]=list1[j]
            list1[j]=m
print(list1)