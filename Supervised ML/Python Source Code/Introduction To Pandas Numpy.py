import pandas as pd
import numpy as np

arry1 = np.array(['North Korea','Afghanisthan','Russia','China','Pakistan','=terorist'])
arry2 = pd.Series(data=[7,5,43,5,7,9],index=['Beta','Alpha','Gamma','Delta','LOOSER','Chat'])
arry3 = pd.Series({'apple':'Red','Mango':'Yellow','BlueBerry':'Blue','Watermelon':'Green/Red','Grapes':'Parrot','Banana':'Yellow'},index=['Beta','Alpha','Gamma','Delta','LOOSER','Chat'])

sr1 = pd.Series(arry1)

sr2 = pd.Series(arry1,index=['Beta','Alpha','Gamma','Delta','LOOSER','Chat'])

sr3 = pd.Series(4,index=['Beta','Alpha','Gamma','Delta','LOOSER','Chat'])

arry1 = np.array([])
sr4 = pd.Series(arry1).empty

s5 = pd.Series(data=[2,5,3,9,6,34]).shape

s6 = pd.Series(data=[1.2,3.5,2.7,4.6,2.3,1.2],index=['Beta','Alpha','Gamma','Delta','LOOSER','Chat']).dtype

s7 = pd.Series(data=[65,45,23,12,57,45],index=['Beta','Alpha','Gamma','Delta','LOOSER','Chat']).dtype

s8 = arry3.index

s9 = arry1.nbytes

s10 = arry2.nbytes

s11 = arry3.nbytes

print(sr1)
print(sr2)
print(sr2['Beta'])
print(sr3)
print(sr4)
print(s5)
print(s6)
print(s7)
print(s8)
print(s9)
print(s10)
print(s11)