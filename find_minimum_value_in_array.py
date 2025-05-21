import numpy as np
arry1 = np.array([21,2,32,33,43])
m = arry1[0]
i=1
while i < len(arry1):
    if m < arry1[i]:
        m = arry1[i]
    i+=1
print(m)