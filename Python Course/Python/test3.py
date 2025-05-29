file = 'input.txt'
try:
    f = open(file,'r')
    words = []

    for line in f:
        w = line.split()
        for i in w:
            if i.lower not in words:
                words.append(i)
    words.sort()
    print(words)
    f.close()
except FileNotFoundError:
    f = open(file,'w')
    f.close()
    print('File not found!')
