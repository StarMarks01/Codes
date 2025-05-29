print("***********************Example1***************************")
tuple1=(1,1,23,4,5)
count=0
for i in tuple1:
    print("Tuple1:",count,i)
    count=count+1
print("***********************Example2***************************")
tuple2=tuple(input("Enter Value In Tuple2:"))
print(tuple2)
counter=0
for j in tuple2:
    print("tuple2:",counter,j)
    counter=counter+1
print("***********************Example4***************************")    
t1=1,2,3,4,5
t2=2,3,4,5,6
print("Concatation",t1+t2)
print("Repetation",t1*3)
print("Membership",t1 in t2)
print("*Iteration*")
for b in t1:
    print(b)
print("Length:",len(t1))
print("Minimum:",min(t1))
print("Maximum:",max(t1))