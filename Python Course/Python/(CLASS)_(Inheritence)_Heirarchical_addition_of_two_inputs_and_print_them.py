class ClassA:
    def inputs(self):
        self.a=int(input("Enter The Value In A:"))
        self.b=int(input("Enter The Value In B:"))
class ClassB(ClassA):
    def sum(self):
        t = self.a + self.b
        print(f"Sum Of {self.a} And {self.b}:", t)
class ClassC(ClassA):
    def mul(self):
        t = self.a * self.b
        print(f"Sum Of {self.a} And {self.b}:", t)
ca=ClassB()
ca.inputs()
ca.sum()
ca1=ClassC()
ca1.inputs()
ca1.mul()
