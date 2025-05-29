try:
    a=str(input("Enter Minimum Of 10 Characters:-"))
    if len(a)<10:
        raise Exception("There Are Less Than 10 Characters")
except:
    print("There Are Less Than 10 Characters!")
else:
     print("There Are More Or Equal To 10 characters")
# finally:
#     print(str)