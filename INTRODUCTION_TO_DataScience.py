import numpy as np


arr1 = np.array(['Onion','Kaleb','Vietnam','boogie','sog','penguinzz','Apple'], order='K')                                 #One Dimension

arr2 = np.array([[12,23],[45,67],[1,3]])      #Two Dimension

arr = np.array([[123, 456]])                 

def prints(a):
    print("Division Floors all elements in array",arr//2)    
    print("dimensions of array are:-",arr.ndim)        
    print("Delivers Datatype of array",arr1.dtype)                   
    print("dimensions of array1 are:- ",arr.ndim)          
    print("Delivers Matrix's rows and columns",arr.shape)                    
    print("Size Of array 2 is:-",arr2.size)
    print("Reshape array 1 is:- ",np.reshape(arr2,6))
    arr3 = np.zeros([4,4],dtype = int)    #creates array and fills it with zeroes
    arr4 = np.ones([2,2],dtype = int)     #Create array and fills it with ones
    print("creates array and fills it with zeroes",arr3)             
    print("Create array and fills it with ones",arr4)
    arr5 = np.empty([3,3],dtype = bool)    #creates array and fills it with random data
    print("creates array and fills it with random data",arr5)
    print("-----------------------------------------------the reshape of array 2-----------------------------------------------")
    print(np.reshape(arr2,6))
    print("-----------------------------------------------the transpose of array 2-----------------------------------------------")
    print(arr2.T)
    print("-----------------------------------------------The Vertically concatenation of array 2-----------------------------------------------")
    print(np.concatenate((arr2,arr),axis=None))            #axis 1 = Y         #axis 0 = X
    print("-----------------------------------------------The Horizontally concatenation of  array 2-----------------------------------------------")
    print(np.concatenate((arr2,arr),axis = 0))
    print("-----------------------------------------------The Split of array-----------------------------------------------")
    print(np.array(np.split(arr2,3)))
    print("-----------------------------------------------The delete of array elements-----------------------------------------------")
    print(np.array(np.delete(arr2,[1,3,4])))
    print("-----------------------------------------------The insert of array elements-----------------------------------------------")
    arr = np.array([1,2,3,4,5])
    print(np.array(np.insert(arr,1,123,axis=None)))
a = int(input("Enter 0 or 1 :-"))
if a == 1:
    print(prints(a))
else:
    print("exit")
