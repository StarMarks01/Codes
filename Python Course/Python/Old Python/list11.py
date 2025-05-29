a=0
list1=[11,23,34,45,56]
i=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        if list1[i]==list1[j]:
            list1[-1]=a
        j+=1
    i+=1
print(list1)