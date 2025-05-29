days1={1,32,4234}
days2={12,3,4,523}
days3={1,23,6,8,9}
num1={1,25,8,10}
num2={1,5,74,34}
a=days1.issubset(days3)       #***********************QUESTION*************************#
print("issubset",a)
b=days1.copy()        #***********************QUESTION*************************#
print("Copy",b)
c=days3.update(days2)
print("Update",c)
d=days1.symmetric_difference(days2)
print("Symetric Differnce",days1)
e=days1.symmetric_difference_update(d)
print("Symetric Differene Update",e)
f=days1.intersection_update(days3)    #***********************Question*******************#
print("intersection update",f)
g=days2.isdisjoint(days3)
print("Is Disjoint",g)