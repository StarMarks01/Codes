import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv(r"C:\Users\Pavilion\Documents\Coding Languages\Artificial Intelligence\Excel and Csv\Fraud.csv")

df2 = df.copy()
TypeLE = LabelEncoder()
scaler = StandardScaler()
model = RandomForestRegressor(n_estimators = 150)
dtc = DecisionTreeClassifier()
logic = LogisticRegression()

df2 = df2.drop(columns = ['isFlaggedFraud','newbalanceOrig','newbalanceDest','nameOrig','nameDest'])

def Outliers(df,columns):
    for i in columns:
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1
        upperlimit = q3 + (1.5 * iqr)
        lowerlimit = q1 - (1.5 * iqr)
        df.loc[(df[i] > upperlimit),i] = upperlimit
        df.loc[(df[i] < lowerlimit),i] = lowerlimit
    return df
cols = ['oldbalanceDest','amount','step']
df2 = Outliers(df2,cols) 

TypeLE.fit(df2['type'])
df2['type'] = TypeLE.transform(df2['type'])

x = df2.drop(columns = 'isFraud')
y = df2['isFraud']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70, test_size = 0.3)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)

logic.fit(xtrainscaled,ytrain)
logic.score(xtestscaled,ytest)

dtc.fit(xtrainscaled,ytrain)
dtc.score(xtestscaled,ytest)

model.fit(xtrainscaled,ytrain)
model.score(xtestscaled,ytest)