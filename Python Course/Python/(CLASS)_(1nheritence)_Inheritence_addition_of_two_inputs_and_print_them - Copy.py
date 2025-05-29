class ClassA:
    def inputs(s):
        s.a=int(input("Enter The Value In A:"))
        s.b=int(input("Enter The Value In B:"))
class ClassB(ClassA):
    def outputs(t):
        t.t = t.a + t.b
        print(f"Addition Of {t.a} And {t.b} is {t.t}")
ca=ClassB()
ca.inputs()
ca.outputs()