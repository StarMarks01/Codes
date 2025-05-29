class ClassA:
    def fun1(palindrome):

        palindrome.pal = int(input("Enter The Value In PALINDROME number:-"))
        palindrome.sum = 0
        n = palindrome.pal

        while n > 0:
            rem = n % 10
            palindrome.sum = palindrome.sum * 10 + rem
            n //= 10

class ClassB:
    def fun2(inputs):

        inputs.a = int(input("Enter The Value In A:"))
        inputs.b = int(input("Enter The Value In B:"))

class Base (ClassA , ClassB):
    def fun3(self):

        if self.sum == self.pal:
            print(f"Yes , {self.sum} Is a palindrome Number")
        else:
            print(f"No , {self.sum} is not a palindrome Number")
        
        total=self.a % self.b
        print(f"The Mod Of {self.a} and {self.b} is:" , total)
ca=Base()
ca.fun1()
ca.fun2()
ca.fun3()