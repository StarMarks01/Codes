import numpy as np
# a = np.array([[1,2],[3,4],[5,6]])
# print ("array a is :\n", a)
# #changing the shape of array from 2D to 1D
# print ("reshape array a is:",np.reshape(a,6))

# print(a.T.T)

# x = np.array([[1,2], [3,4]])
# y = np.array([[5,6]])
# print(np.concatenate((x,y),axis=0))


# 1 2
# 3 4

# 5
# 6

arr = np.array([1,2,3,4,5,6,7,8,9])

print(np.array(np.split(arr,3)))

a = np.array([[1,2,3],[1,2,3]])
print ("array a is :", a)
#deleting elements
print ("after deletion:", np.delete(a,[1,2,3],axis = 0))
