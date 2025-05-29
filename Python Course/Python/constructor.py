# Constructor is special method --> init
# auto call when we create its object
class ClassA:
    def __init__(self,a):
        print('=======',a)
    
cc = ClassA(12)