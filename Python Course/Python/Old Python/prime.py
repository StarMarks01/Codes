def prime(num):
    i=2
    while i<num:
        if num%i==0:
            return False
        i+=1
    return True
def full(start,end):
    for i in range(start , end):
        if prime(i):
            print(i,end="\t")
full(10,500)

