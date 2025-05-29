def fact():
    factorial = 4
    if factorial <= 0:
        print("There Was An Error Please Input The Value Again")
    else:
        for i in range(1 , factorial):
            factorial = factorial * i
        print( factorial )
fact()