n = 9
i=0
sum = 0 
num = n**2          #81
while i<num:        # 0<81                  #0<8
    neon = num%n    #neon = 81%9 = 1        #8%10 = 8
    sum=sum+neon    #sum = 0 + 1 =1         #1+8 =9
    num=num//10     #num = 81//10 = 8       #8/10 = 0
if sum == n:
    print(f"Yes{num} Is a Neon Number") 
else:
    print(f"No {num} Is not a Neon Number")   
