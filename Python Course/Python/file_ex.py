try:
    ff = open("a.txt",'r')
    # ff.write("Hello World")
    # print(ff.readline())
    # print(ff.readline())
    # print(ff.readlines())
    vv=ff.readable()
    if(vv):
        print(ff.read())
except FileNotFoundError:
    print('File not exist')

# ff = open('image.png','rb')
# cc = open('copy.png','wb')

# cc.write(ff.read())
