a=0
list1=[11,23,34,45,56]
i=0
l=len(list1)
j=0
while i<l:
    j=i+1
    while j<len(list1):
        temp=list1[i]
        list1[i]=list1[j]
        list1[j]=temp
        j+=1
    i+=1
print(list1)