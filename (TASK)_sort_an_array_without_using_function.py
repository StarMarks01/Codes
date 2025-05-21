from numpy import *
arry1 = array([112,45,54,756,322,2,1323])
i = 0
m = arry1[0]
while i < len(arry1):
    j = i
    while j < len(arry1):
        if arry1[i]>arry1[j]:
            arry1[i] = m
            arry1[i] = arry1[j]
            arry1[j] = m
        j+=1
    i+=1
print(arry1)