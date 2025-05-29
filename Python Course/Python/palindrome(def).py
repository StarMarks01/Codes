def pal(s, e):
    s=500
    e=1000
    sum=0
    while s<=e:
        pal=s
        n=pal
        rem = n % 10
        sum = sum + rem
        n //= 10
        print(sum)
        s+=1
pal(500,1000)

