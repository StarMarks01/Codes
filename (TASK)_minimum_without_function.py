i = 0
list = [281,152,432,321,253]
m = list[0]
while i < len(list):
    if list[i] < m:
        m = list[i]
    i+=1
print(m)