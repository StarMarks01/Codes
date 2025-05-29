pal=int(input("Enter The Value In Palindrome Number:"))     #lets take palindrome as 123
n = pal                                                     #now n=123
while(n>0):                                                 #is 123>0?          #is 12>0?               #is 1>0?
    rem = n % 10                                            #reminder=123%10=3  #remainder=12%10=2      #remainder=1%10=1
    sum = sum*10 + rem                                      #sum=0*10+3=3       #sum=3*10+2=32          #sum=32*10+1=321
    n //= 10                                                #n=123//10=12       #n=12//10=1             #n=1//10=0
sum = 0                                                     
print(sum)                                                  #print 321
if pal==sum:                                                #is 123==321?
    print("it is a plaindrome number")
else:
    print("it is not a palindrome number")                  #prints this            