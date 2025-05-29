#next aim :- replace 1st index with a new number
list1=[13,123,132,312]
i=0
l = len(list1)
j=-1
while i < l/2:

    t = list1[i]
    list1[i]=list1[j]
    list1[j]=t 
    i+=1
    j-=1
print(list1)       