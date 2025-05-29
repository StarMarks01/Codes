class ClassA:
    def index():
        try:
            list1=[1,2,3,4,5]
            print(list1[6])
        except IndexError:
            print("Sorry Index Error")
        except TypeError:
            print("Sorry There Was A Type Error")
        finally:
            print("Code Is Complete")
ca=ClassA()
ca.index()