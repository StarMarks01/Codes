days1={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}
days2={253,645,8,5214,124,6,}
days3={2124,14,124,54,2}
num1={1,2,3,4,5,6,7,8,9,10}
num2={1,5,74,1,65,45,34,34}
print(days1)
print(num1)
print(type(days1))
print(type(num1))
print("Union Method:",days1.union(num1))        #union Method
print("Union Short:",days1|num1)
print("Intersection Method:",days1.intersection(days3))    #intersection Method
print("Intersection Short",days1&days3)
print("Difference Method:",days1.difference(days3))         #difference Method
print("Difference Method:",days1-num1)