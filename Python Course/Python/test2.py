from lambda_print_if_a_letter_is_starting_of_word_in_list import list1 as ll
li = [13,42,53,45,84,6,6]

# li = [i+10 for i in li]

li = [i for i in li if i<=50]

print(li)

x = lambda n: n+10

print(x(5))


li = [32,34,45,6,7,89,5,0]

# ll = [i+10 for i in li ]

def add(n):
    return n+10

plus = lambda n:n+10

ll = list(map(lambda n:n<50, li))

print(ll)

def ff(n):
    return n<50

a = list(filter(lambda n : n<50,li))

print(a)

import datetime as dt

d=dt.datetime.now()

print('data=',d)

try:
    print(10/0)
    a =20
except ZeroDivisionError:
    print('Error')
    a=0
except NameError:
    print('=======')
finally:
    print('Done ',a)
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
# Constructor is special method --> init
# auto call when we create its object
class ClassA:
    def __init__(self,a):
        print('=======',a)
    
cc = ClassA(12)