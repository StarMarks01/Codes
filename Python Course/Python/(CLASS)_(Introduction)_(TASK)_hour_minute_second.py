class classA:
    def inputs(self):
        self.h=int(input("Enter The Value In Hour:"))
        self.m=int(input("Enter The Value In Minute:"))
        self.s=int(input("Enter The Value In Seconds:"))
    def time(t,ca):
        while ca.s>60:
            ca.m+=1
            ca.s-=60
        while ca.m>60:
            ca.h+=1
            ca.m-=60
        print(f"{ca.h}:{ca.m}:{ca.s}")
ca = classA()
ca.inputs()
ca1 = classA()
ca1.time(ca)    