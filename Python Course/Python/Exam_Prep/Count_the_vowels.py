try:
    f = open("inputs.txt",'r')
    v = 0 
    vowel = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
    for line in f:
        for i in line:
            if i in vowel:
                v+=1
    print("Vowel Count:-",v)
except:
    print("File not found")
                