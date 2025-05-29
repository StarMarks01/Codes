#i=10
#while i<1001:
n=153
sum=0
while n>0:
        r = n % 10
        sum = sum+r*r*r
        n//=10
print(sum)