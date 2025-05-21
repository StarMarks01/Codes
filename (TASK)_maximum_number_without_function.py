import numpy as np
arry1 = np.array([312,3123,313,142,355])
# print(arry1)
max = 0
for i in range(1,len(arry1)):
    if arry1[max] < arry1[i]:
        max = i
print(arry1[max])