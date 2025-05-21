from numpy import random
def numpy():
    # print("Randint of Random function is:-",random.randint(1,100))
    # print("The rand function of numpy is:-",random.rand(1,2))
    print("The Randint function that makes a random array is:-\n",random.randint(100,size=(3,3)))
    print("The rand function for three dmentional array is:-\n",random.rand(2,2,2))
    print("The randint function for three dmentional array is:-\n",random.randint(100, size = (3,1,2)))
    print("The rand function for two dmentional array is:-\n",random.rand(2,2))
    print("The Choice in random function is :-",random.choice([1,21,123,32]))
    print("The Choice in random function is :-",random.choice([2,32,6],size=(3,2)))
numpy()