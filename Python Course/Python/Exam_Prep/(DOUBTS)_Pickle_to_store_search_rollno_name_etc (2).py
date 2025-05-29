import pickle as p
student = []
f=open('students.txt','wb')
ans = 'Y'
while ans.lower()=='y'or ans == 'Y':
    roll=int(input("Enter The Roll Number:-"))
    student.append(roll)
    name=input("Enter The Name:-")
    student.append(name)
    ans=input("Add More? (Y/N):-")
p.dump(student,f)
f.close()
f=open('students.txt','rb')
student = []
student = p.load(f)
# print(student)
ans='Y'
while ans.lower()=='y' or ans == 'Y':
    found=False
    r=input("Enter rollno to search:-")
    for s in student:
        if s[roll]==r:
            print('Name:-',s[1])
            found=True
            break
        if not found:
            print('no match found sorry :<')
    ans=input("Search Roll no again (Y/N)? :-")
    print('End of program')
f.close()