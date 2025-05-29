days1={13,4,2,234}
days2={124,55,23}
days3={1,23,8,9}
num1={1,2,3,4,5}
num2={1,5,74,1,}
print("Union Method:",days1.union(num1))        #union Method
print("Union Short:",days1|num1)
print("Intersection Method:",days1.intersection(days3))    #intersection Method
print("Intersection Short",days1&days3)
print("Difference Method:",days1.difference(days3))         #difference Method
print("Difference Method:",days1-num1)
days1.add("January")         #Add Method
print("Add Method",days1)
days1.remove("January")      #Remove Method
print("Remove Method",days1)
days1.discard("Sunday")      #Discard Method
print("Discard Method",days1)
days1.pop()                  #POP Method
print("POP Method",days1)
days2.clear()                #Clear Method
print("Clear Method",days2)