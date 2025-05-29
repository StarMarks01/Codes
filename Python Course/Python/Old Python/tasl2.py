def PRIME():
    i = 2
    prime = 5
    while i<prime:
        if prime % i == 0:
            return False
        i+=1
    return True
print(PRIME())