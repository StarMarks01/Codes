def palindrome(num):
    pal = num 
    i = 0
    sum = 0
    while i < pal:
        rem = pal % 10
        sum = sum * 10 + rem 
        pal //= 10
    if sum == num:
        print(f"Yes {num} Is a palindrome number")
    else:
        print(f"No {num} Is not a palindrome number")
def armstrong(num):
    arm = num
    i = 1
    sum = 1
    while i < arm:
        rem = arm % 10
        sum = sum + rem * rem * rem
        arm //= 105
    if sum == num:
        print(f"Yes {num} is an armstrong number")
    else:
        print(f"No {num} is not an armstrong number")
def neon(num):
    i = 0
    sum = 1
    bom = num**2               
    while i < bom:
        neon = bom % num
        sum = sum + neon
        bom //= 10
    if sum == num:
        print(f"Yes {num} is a Neon Number")
    else:
        print(f"No {num} is not a Neon Number:-")
num = int(input("Enter Value To find  either Palindrome Armstrong or neon Number:-"))
palindrome(num)
armstrong(num)
neon(num)
# sel = str(input("Enter Value P for Palindrome N for Neon and A for Armstrong:-"))
# if sel == 'P' or 'p':
#     print(palindrome(num))
# elif sel == 'A' or 'a':
#     print(armstrong(num))
# elif sel == 'N' or 'n':
#     print(neon(num))
# else:
#     print("Exit")
# neon(num)