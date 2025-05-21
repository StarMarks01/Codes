list1 = [1,2,3,4,5]
num = 1.5
index = list1[0]
for i in range(1,len(list1)):
    if list1[i]<num:
        index+=1
    else:
        list1[index]+num
print(list1)