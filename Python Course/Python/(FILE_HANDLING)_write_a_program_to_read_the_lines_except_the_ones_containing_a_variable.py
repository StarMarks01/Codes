#write a Python program to read the content of file line by line and write it to another file except
#for the lines containing "a" letter in it
f=open("inputs.txt",'r')
# ff=open("inputs1.txt",'w')
# data = ["Hello Everyone\n","How are you\n", "Welcome\n"]
# f.writelines(data)
# f.seek(0), tell, pickle
# f.seek(1)
# for i in data:
#     if "a" not in i.lower():
#         ff.write(i)

print(f.readline())
print(f.tell())
print(f.readline())
f.close()

# import pickle as p
# data = {'A':123,'B':456}
# pp = p.dumps(data)
# dd = p.loads(pp)
# print(dd)