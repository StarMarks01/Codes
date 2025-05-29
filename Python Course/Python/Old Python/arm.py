arm = 153
t = arm
sum = 0
while t>0:
    r = t % 10
    sum = sum + r*r*r
    t //= 10
if arm == sum:
    print("yes")
else:
    print("no")

