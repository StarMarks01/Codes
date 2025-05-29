def palindrome(num):    #creating function 1    
    n = num             #creating palindrome number identifier
    sum = 0             
    while(n>0):         
        rem = n % 10
        sum = sum + rem * rem * rem
        n //= 10
    return sum == num
    # if(sum == num):
    #     return True
    # else:
    #     return False
def printPalindrome(start, end):
    for i in range(start, end):
        # var = palindrome(i)
        if(palindrome(i)):
            print(i, end='\t')
printPalindrome(500, 1000)