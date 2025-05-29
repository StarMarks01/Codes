def armstrong(arm):
    t=arm
    sum=0
    while t>0:
        rem = t % 10
        sum = sum + rem * rem * rem
        t //= 10
    print(sum)
armstrong(153)
