str1='abc'
str2="Creative"
str3="""12      687673  
                           421432    """
str4="Python 4 free"
str5="         " 
str6="WWHAT IS IT"         
str7="1.232423423423"
str8="12345678"
str9=":"
list1=['1','2','3','4']
print(type(str1))
print(type(str2))
print(type(str3))
cstring=str1.capitalize()
print(cstring)
cstring=str1.upper()
print(cstring)
cstring=str1.lower()
print(cstring)
cstring=str4.isalnum()
print(cstring)
cstring=str1.isalpha()
print(cstring)
cstring=str5.isspace()
print(cstring)
cstring=str2.swapcase()
print(cstring)
print(len(str3))
cstring=str1.islower()
print(cstring)
cstring=str6.isupper()
print(cstring)
cstring=str6.replace("WWHAT","WHAT")
print(cstring)
cstring=str6.isdecimal()
print(cstring)
cstring=str6.index("IT")
print(cstring)
cstring=str6.startswith("W")
print(cstring)
cstring=str7.endswith("3")
cstring=str6.casefold()
print(cstring)
cstring=str6.find("WHA")
print(cstring)
cstring=str7.isdecimal()                                        #str7="1.232423423423"
print(cstring)                                                  
cstring=str8.isdecimal()                                        #str8="12345678"
print(cstring)
cstring=str9.join(list1)
print(cstring)
cstring=str8.isdigit()
print(cstring)
cstring=str8.isnumeric()
print(cstring)
cstring=str3.isprintable()
print(cstring)
cstring=str4.format()
cstring=str6.count("IT")
print(cstring)
a="a"
b="b"
str1.format()
print("Format of {} and {} is".format(a,b))
print("Format of {0:o} and  is".format(10))