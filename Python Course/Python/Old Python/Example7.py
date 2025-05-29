list1=[12,3,123,132]
i=0
a=123
while i<len(list1):
    if a not in list1[i]:
        list1.append(2)
    i+=1    
print(list1)