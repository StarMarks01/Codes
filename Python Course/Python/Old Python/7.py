list1=[1,2,5,34,32]
atuple=(2,31,546,34)
blist=[1,4,453,4,3,56,4]
clist=[6,7,2,2,1,6,7,34]
alist=list(atuple)
dlist=[3,5,8,365,7]
print(type(alist))
list1.pop()
print("Pop Function:",list1)
alist.remove(31)
print("Remove Function:",alist)
alist.insert(2,3)
print("Insert Function:",alist)
blist.sort()
print("Sort Function:",blist)
list1.append(blist)
print("Append Function:",list1)
blist.reverse()
print("Reverse Function:",blist)
clist.extend(blist)
print("Extend Function:",clist)

vv = dlist.count(365)    #Question
print("Count Function:",vv)
dlist.index(5)
print(dlist)
print("Minimum function:",min(blist))
print("Maximum Function:",max(blist))
print("Length Function:",len(blist))
print(alist)