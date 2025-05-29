list1=[1,2,3,4,4,5] #0,1,2,3,4,5
i=0 # Start->0
while i<len(list1):#print to length of list1 using indexing from 0 to 5 [1,2,3,3,4,5]
    j=i+1#starts from 1 after the starting point of i 
    while j<len(list1):#goes from 1 to 5 [2,3,3,4,5]
        if list1[i]==list1[j]:#makes a decision if [1,2,3,3,4,5] is equals to [2,3,3,4,5] indexing form:i=0,1,2,3,4,5 j=1,2,3,4,5
            k=j #stores value of j to k
            while k<len(list1)-1:#like j it increments the length of list1 from 2 and -1 so the extra variable is deleted
                list1[k]=list1[k+1]
                k+=1
            del list1[k-1]
        j+=1
    print(list1[i])
    i+=1
