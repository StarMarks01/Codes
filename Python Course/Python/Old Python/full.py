i=10
while i<=1000:
    n=i
    sum = 0
    while(n>0):                                           
        rem = n % 10 
        sum = sum*10 + rem
        n //= 10
    if(sum == i):
        print(i,end="\t")
    i+=1