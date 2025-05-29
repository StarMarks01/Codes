import numpy as np
import pandas as pd

df1 = pd.DataFrame()
# print(df1)

list1 = [2,32,4,54,76,72,23]
df1 = pd.DataFrame(list1)

# print('Print DataFrame Using List',df1)
dict = {'Name':['Yagnesh','Jeremy','Charlie','Mutahar'],'Debt':[100,12423423,5433,23123]}
df1 = pd.DataFrame(dict)
# print(df1)

dict = {'Name':pd.Series(['The Diddler','Drake','Chris Tyson','Dr.Disrespect'],index=['Pdf file 1','Pdf file 2','Pdf File 3','PDF file 4'])}
df1 = pd.DataFrame(dict)
# print(df1)

dict = {'Name':pd.Series(['Yagnesh','Tommy','Roxy','Keanu','Charles'],index=['Gujarat','Florida','Tampa','Taxes','Florida'])}
df1 = pd.DataFrame(dict)
# print(df1)

dict = {'Name':pd.Series(['Keanu Reeves','Penguinz0','Asmongold','Jackson Clarke','Agent 47'],index=['The Boogeyman','Charles White','Legend',"Boggie's Worst nightmare",'Hitman']),'Diddy':pd.Series(['Tom','Tommy','Bob','Bobby','Diddler'],index=['Timothy','Gta','Oggy','Googy','PDF File'])}
df1 = pd.DataFrame(dict)
# print(df1['Name'])

dict = {'Name':pd.Series(['Keanu Reeves','Penguinz0','Asmongold','Jackson Clarke','Agent 47'],index=['The Boogeyman','Charles White','Legend',"Boggie's Worst nightmare",'Hitman']),'Diddy':pd.Series(['Tom','Tommy','Bob','Bobby','Diddler'],index=['Timothy','Gta','Oggy','Googy','PDF File'])}
df1 = pd.DataFrame(dict)
# print(df1)
print('-----------------------')
df1['PDF File'] = pd.Series(['Keanu','Patel Jiger','MoistCr1tikal'],index=['John Wick','Big Moist','Penguinz0'])
# print(df1)

dict = {'Name':pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])}
df1 = pd.DataFrame(dict)
# print(df1)

print('-----------------------')

dict = {'Name':pd.Series([1,2,3],index=['a','b','c']),'android':pd.Series(['Mint','Oreo','Stake'],index=['11','8','20'])}
df1 = pd.DataFrame(dict)
df1['Maximus'] = pd.Series([4,5,6],index=[7,8,9])
# print(df1)

dict = {'School':pd.Series([1,2,3,4,5]),'android': pd.Series([10,11,12,6,8])}
df1 = pd.DataFrame(dict)

df1['pythoon'] = df1['School']+df1['android'] 

del df1['School']

df1.pop('android')

# print(df1)

dict = {'Design':pd.Series([1,2,3,4,5,6,7,8,9],index = ['a','b','c','d','e','f','g','h','i'])}
df1 = pd.DataFrame(dict)
df1['Malware'] = pd.Series([2,3,4,5,67,8,9,56,4],index = ['a','b','c','d','e','f','g','h','i'])
df1['PYTHON'] = df1['Malware'] + df1['Design']
# print(df1)
print(df1.loc['i']) 