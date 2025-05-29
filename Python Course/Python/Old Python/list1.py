list1=[1,2,3,4,5]
n=list1[0]
m=0
for i in list1:
    if i<n:
        i=n
    if i>m:
        m=i
print(m)
print(n)