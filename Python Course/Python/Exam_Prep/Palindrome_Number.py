pal = 101
n = pal
i = 0
sum = 0
while i<n:
    rem = n % 10
    sum = sum * 10 + rem
    n //= 10
if pal == sum:
    print(f"Yes {pal} is a plaindrome number")
else:
    print(f"No {pal} is not a plaindrome number")
