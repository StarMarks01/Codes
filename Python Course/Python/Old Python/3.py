list1=[1,66,44,22,33,76]
i=0
while i<len(list1):
    j=i+1
    while j<len(list1):
        list1[j]+20
        j+=1
    i+=1
    print(list1[i])