str1="Java"
str2="Python"
print("{} and {} both are programming languages".format(str1,str2))
str3="{1} And {0} both are programming languages".format(str1,str2)
print(str3)
val=10
print("Decimal: {0:d}".format(val))
print("Octal: {0:o}".format(val))
print("Binary: {0:b}".format(val))
print("Hexadecimal: {0:x}".format(val))
val2=100000000
print("Decimal: {:,}".format(val2))
print("Decimal: {:.2%}".format(10.123456789))