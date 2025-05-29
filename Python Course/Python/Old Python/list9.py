list1=[1,2,3,45,2345]#declare the list
a=4#add the duplicate value
i=0#starting point of for loop
istrue=False
while i<len(list1):
    if list1[i]==a:
       istrue=True
    i+=1
if not istrue:
    list1.append(4)
print(list1)