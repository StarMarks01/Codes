pal=123
n = pal
sum = 0
while(n>0):
    rem = n % 10
    sum = sum*10 + rem
    n //= 10
if sum==pal:
    print(sum)
else:
    print("Exit")