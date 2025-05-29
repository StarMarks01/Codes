#Q1-C ==> 7 Marks

dicta={1:'Black',2:"White",3:"Red",4:"Blue"}

d1=dicta.copy()

print("The Length Of Dictionary:-",len(d1))
print("The Copy of Dictionary:-",d1)

print("Items In Dictionary:-",d1.items())
print("Keys In Dictionary:-",d1.keys())
print("Values In Dictionary:-",d1.values())

print("Using Pop Method In Dictionary With Key",d1.pop(1))
print("Using Popitem in dictionary",d1.popitem())

#{2: 'White', 3: 'Red'} Remaining

print("Updating The Original Dictionary Using Update Function",dicta.update(d1))
print("Deleting All Data Using clear() Method:-",d1.clear())