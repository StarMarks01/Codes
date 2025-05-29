class BASE:
    def funA(inputs):
        inputs.input1 = int(input("Enter The Value for armstrong number:"))
        inputs.input2 = int(input("Enter The Value for palindrome number:-"))
        inputs.suma = 0
        inputs.sumb = 0
        inputs.a = int(input("Enter The Value In A:"))
        inputs.b = int(input("Enter The Value In B:"))
        inputs.c = int(input("Enter The Value In C:"))
        inputs.d = int(input("Enter The Value In D:"))
        inputs.arm = inputs.input1
        inputs.pal = inputs.input1 
class FordA(BASE):
    def funB(arm):

        while arm.arm > 0:
            rem = arm.arm % 10
            arm.suma = arm.suma + rem * rem * rem
            arm.arm //= 10

            arm.f=arm.suma
        #print(arm.suma)
        arm.fuf = arm.a + arm.b + arm.c + arm.d
        
class FordB(BASE):
    def funC(palindrome):

        while palindrome.pal > 0:
            rem = palindrome.pal % 10
            palindrome.sumb = palindrome.sumb * 10 + rem
            palindrome.pal //= 10

        #print(palindrome.sumb)
        
        palindrome.max = palindrome.a + palindrome.b + palindrome.c + palindrome.d / 4

class FOUNDATION(FordA, FordB):
    def funD(total):
        
        if total.suma == total.input1:
            print(f"Yes, {total.input1} is an armstrong number")
        else:
            print(f"No , {total.input1} is Not an armstrong number")

        if total.sumb == total.input2:
            print(f"Yes, {total.input2} is palindrome number")
        else:
            print(f"No , {total.input2} is Not a palindrome number")

        print(f"The Average Of {total.a} , {total.b} , {total.c} and {total.d} :" , total.max)
        print(f"The SUM Of {total.a} , {total.b} , {total.c} and {total.d} :" , total.fuf)
        
ca=FOUNDATION()
ca.funA()
ca.funB()
ca.funC()
ca.funD()