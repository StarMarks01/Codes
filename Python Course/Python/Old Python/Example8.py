min1=60
h=int(input("Enter The Value In Hour:"))
m=int(input("Enter The Value In Minutes:"))
s=int(input("Enter The Value In Seconds:"))
while s>min1:                
    s = s-60 
    m+=1
while m>60:
    m=m-60
    h=h+1
if s and m < 60:
    print("Hour:",h)
    print("Minute:",m)
    print("Second:",s)