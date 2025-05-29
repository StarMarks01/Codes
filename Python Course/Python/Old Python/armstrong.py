arm = 153
n = arm
sum = 1
i = 0
while i < n:                        # 0<153                 #0<15                      #0<1
    rem = n % 10                    #rem = 153%10 = 3       #rem = 15%10 = 5           #rem = 1%10 = 0.1
    sum = sum  + rem*rem*rem            #sum = 1*10+3 =13       #sum = 13*10 + 5 = 135     #sum = 135*10 + 0.1
    n//=10                          #153//10 = 15           #15//=10 = 1
    i+=1
print(sum)
if arm == sum:
    print(f"Yes {arm} is an armstrong number")
else:
    print(f"No {arm} is not an armstrong number")
