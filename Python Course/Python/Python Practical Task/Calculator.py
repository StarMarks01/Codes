while True:
    print("1:Addition")
    print("2:Subtraction")
    print("3:Multiplication")
    print("4:Division")
    print("5:Modulo")
    print("6:Exit")

    op = int(input("Enter The Operator:"))
    a = int(input("Enter the 1st Operand:"))
    b = int(input("Enter The 2nd Operand"))

    if op == 1:
        c = a + b
        print("Addition",c)
    elif op == 2:
        c = a - b
        print("Subtraction",c)
    elif op == 3:
        c = a * b
        print("Multiplication",c)
    elif op == 4:
        if b == 0:
            print("Error: Division By Zero Exception")
        else:
            c = a / b
            print(c)
    elif op == 5:
        c = a % b
        print(c)
    elif op == 6:
        print("Exiting...")
        break
    else:
        print("Invalid Operator")