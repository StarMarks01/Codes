class ClassA:
    def funA (inputs):
        inputs.a = int(input("Enter The Value In A:"))
        inputs.b = int(input("Enter The Value In B:"))
class ClassB (ClassA):
    def funB (self):
        self.c = int(input("Enter The Value In C:"))
        self.d = int(input("Enter The Value In D:"))
        total = self.a + self.b
        print(f"Additon of {self.a} and {self.b} : ", total)
class ClassC (ClassB):
    def funC(pets):
        total = pets.a + pets.b + pets.c + pets.d
        print(f"Addition of {pets.a} , {pets.b} , {pets.c} & {pets.d} :",total)
ca=ClassC()
ca.funA()
ca.funB()
ca.funC()