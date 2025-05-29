class ClassA:
    def index(self):
        try:
            self.list1=[1,2,3,4,5]
            print(self.list1[6])
        except IndexError:
            print("Sorry Index Error")
        except TypeError:
            print("Sorry There Was A Type Error")
        finally:
            print("Code Is Complete")
# inheritance
class ClassB(ClassA):
    def fun(self):
        self.index()

cb = ClassB()
cb.fun()