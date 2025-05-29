h=int(input("Enter The Value In Hour:"))
m=int(input("Enter The Value In Minutes:"))
s=int(input("Enter The Value In Seconds:"))
while s>60:
    m+=1
    s-=60
while m>60:
    h+=1
    m-=60 
print(f"{h}:{m}:{s}")