def factorial(fact):
    if fact == 0:
        print("Factorial Cannot be 0")
    elif fact == 1:
        print("Factorial Cannot Be 1")
    else:
        for i in range(1,fact):
            fact = fact*i
        print(fact)
factorial(4)