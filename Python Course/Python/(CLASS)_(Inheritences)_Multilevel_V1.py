class ClassA:
    def inputs(s):
        s.a=int(input("Enter The Value In A:"))
        s.b=int(input("Enter The Value In B:"))
class ClassB(ClassA):
    def outputs(t):
        t.t = t.a + t.b
class ClassC(ClassB):
    def prints(p):
        print(f"Addition Of {p.a} and {p.b} is {p.t}")
a=ClassC()
a.inputs()
a.outputs()
a.prints()