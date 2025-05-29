list1 = ["Yello","Green","Yelp","Yes"]
i = 0
list = []
val = 'Y'
for i in range (0, len(list1)):
    if val in list1[i][0]:
        list.append(list1[i])
    else:
        pass
print(list)