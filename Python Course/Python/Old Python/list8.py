list1=[22,77,83,2,44]
i=0
j=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        if list1[j]<=list1[i]:
            temp = list1[i]
            list1[i]  = list1[j]
            list1[j] = temp 
        j+=1
    i+=1