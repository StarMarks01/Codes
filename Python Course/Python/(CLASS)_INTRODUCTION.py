#oop
#class and objects
#what is class?
#class is a collection of objects
#class is collection of Variables and methods
#class is a blue print of variables

#class

class ClassA:
    a=14
    b=25
    def fun(ss, var:int)->int:
        ss.a = 2
        print("Hello --->",var)
        return 111
def ff(var:int)->int:
    print("+++>",var)
    return 112
var = 123
bp1= ClassA()
bp2=ClassA()
v=ClassA().fun(var)
f=ff(var)
print(ClassA().a)
print("___________}",v)
print("======>",f)
