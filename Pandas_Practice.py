# arry1 = pd.array([23,54,645,32,74,76,23])
# arry2 = pd.array([1,1,1,1,1,1,1])

# arry3 = arry1 + arry2

# maths = np.random.randint(1,100)
# science = np.random.randint(1,100)
# english = np.random.randint(1,100)
# socialscience = np.random.randint(1,100)

# pt = np.random.randint(1,100)
# marks = pd.Series([maths,science,english,socialscience,pt],index=['Mathematics','Science','English','Social Science','Practical Test']


import numpy as np
import pandas as pd
ch = np.random.choice([
    "Alice Johnson", "Bob Smith", "Charlie Brown", "David Lee", "Eva White", "Frank Harris", 
    "Grace Clark", "Hannah Lewis", "Ian Walker", "Jack Hall", "Katherine Allen", "Leo Young", 
    "Mia King", "Nina Wright", "Oliver Scott", "Paul Green", "Quinn Adams", "Rachel Baker", 
    "Sam Nelson", "Tina Carter", "Ursula Turner", "Victor Evans", "Wendy Mitchell", "Xander Cooper", 
    "Yara Ross", "Zach Morris", "Ava Thompson", "Brian Robinson", "Catherine Hall", "Daniel Turner", 
    "Emma Martinez", "Fiona Garcia", "George Lopez", "Holly Wilson", "Isaac Davis", "Jasmine Miller", 
    "Kevin Anderson", "Liam Thomas", "Monica Martinez", "Nathan Brown", "Olivia Jackson", 
    "Peter Hernandez", "Quincy Moore", "Rita Taylor", "Sophie Wilson", "Tom Robinson", "Una Adams", 
    "Vera Parker", "Walter Bennett", "Xena Carter", "Yvonne Hughes", "Zane Foster", "Amber Young", 
    "Blake Harris", "Chloe Adams", "Derek Phillips", "Ella Murphy", "Felix Richardson", "Grace Lee", 
    "Harrison Gray", "Ivy Carter", "James Walker", "Kimberly Hall"
])


i = 0

sel = str(input("Input M For Mathematics, S For Science, E For English, SS For Science and pt For Practical Test and a for all in one:-"))

maths = np.random.randint(1,100)
science = np.random.randint(1,100)
english = np.random.randint(1,100)
socialscience = np.random.randint(1,100)
pt = np.random.randint(1,100)
marks = pd.Series([maths,science,english,socialscience,pt],index=['Mathematics','Science','English','Social Science','Practical Test'])
if sel == 'M' or 'm':
    print(f"The Marks Of {ch} of Mathematics Is:-",marks['Mathematics'])
elif sel == 'S' or 's':
    print(f"The Marks Of {ch} of Science Is:-",marks["Your Marks On Mathematics Is:-",'Science'])
elif sel == 'E' or 'e':
    print(f"The Marks Of {ch} of English Is:-",marks['English'])
elif sel == 'SS' or 'ss':
    print(f"The Marks Of {ch} of Social Science Is:-",marks['Social Science'])
elif sel == 'PT' or 'pt':
    print(f"The Marks Of {ch} of Practical Test Is:-",marks['Practical Test'])
elif sel == 'a' or 'A':
    print(f"The Marks of {ch} of All Subjects Of All is:-",marks)

sum = maths + science + english + socialscience + pt
avg  = sum / 5

print(f"{ch} Your Total Marks are:- {sum} and your average marks are {avg}")

if avg < 33:
    print(f'Sorry! {ch} You Have Failed Your Exam')
else:
    print(f'Congratulations! {ch} You Have Passed This Exam')