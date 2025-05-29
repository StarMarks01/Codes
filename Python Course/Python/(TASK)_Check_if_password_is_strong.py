pas = "Hello@123"
def upper(pas):
    for i in pas:
        if i>='A' and i <='Z':
            return True
    return False
def digits(pas):
    for i in pas:
        if i>='1' and i <= '9':
            return True
    return False
def special(pas):
    for i in pas:
        if i == '@' or i == '$':
            return True
    return False
print(upper(pas))
print(digits(pas))
print(special(pas))