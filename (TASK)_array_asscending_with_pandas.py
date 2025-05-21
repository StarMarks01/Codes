import numpy as np
import pandas as pd
arry1 = np.array([5,4,72,43,52])
for i in range(len(arry1)):
    for j in range(len(arry1)):
        if arry1[i]<arry1[j]:
            temp = arry1[i]
            arry1[i]=arry1[j]
            arry1[j] = temp
arry2 = pd.Series(arry1,index = ['Lowest','Low','Average','High','Highest'])
print(arry2)