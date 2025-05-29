f=open('inputs.txt','w')
lines=['Hello python\n','How are you?\n','My name is Yagnesh']
f.writelines(lines)
f.close()
f=open('inputs.txt','r')
unique = []
for line in f:
    words=line.split()
    for i in words:
        if i.lower() not in unique:
            unique.append(i)
unique.sort()
print(unique)
f.close()