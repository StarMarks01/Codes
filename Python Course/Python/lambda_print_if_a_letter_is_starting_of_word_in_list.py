list1=['ejk','oak','ked','omer','ejane']

a=list(filter(lambda n: n.startswith('e'),list1))

b=list(filter(lambda n: n.endswith('e'),list1))

print("Starts With",a)

print("Ends With",b)