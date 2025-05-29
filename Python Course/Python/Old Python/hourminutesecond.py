h = int(input("Enter Hour:-"))
m = int(input("Enter Minute:-"))
s = int(input("Enter Second:-"))
while s>=60:
    s=s-60
    m+=1
while m>60:
    m-=60
    h+=1
print(f"The Hour is {h}")
print(f"the minute is {m}")
print(f"the second is {s}")
