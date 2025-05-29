import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

df = pd.read_csv(r'C:\Users\Administrator\Documents\Yagnesh\Indian Liver Patient Dataset.csv')

df2 = df.copy()
le = LabelEncoder()
logic = LogisticRegression()
dtc = DecisionTreeClassifier()
model = RandomForestClassifier(n_estimators = 150)
scaler = StandardScaler()

df2 = df2.drop(columns = 'Albumin_and_Globulin_Ratio')

df2['Gender'] = le.fit_transform(df2['Gender'])

def Outliers(df,columns):
    for i in columns:
        df[columns].astype(int)
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1
        upperlimit = q3 + (1.5 * iqr)
        lowerlimit = q1 - (1.5 * iqr)
        df.loc[(df[i]>upperlimit),i] = upperlimit
        df.loc[(df[i]<lowerlimit),i] = lowerlimit
    return df
cols = ['Direct_Bilirubin','Total_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens']
df2 = Outliers(df2,cols)

x = df2.drop(columns = 'Dataset')
y = df2['Dataset']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70,test_size = 30)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)

logic.fit(xtrainscaled,ytrain)
logics = logic.score(xtestscaled,ytest)

dtc.fit(xtrainscaled,ytrain)
dtcs = dtc.score(xtestscaled,ytest)

model.fit(xtrainscaled,ytrain)
rfcs = model.score(xtestscaled,ytest)

print("Classification Score:")
print("LogisticRegression:",logics)
print("DecisionTreeClassifier:",dtcs)
print("RandomForestClassifier:",rfcs)

dumpattr = {
    'model': model,
    'dtc': dtc,
    'logic': logic,
    'scaler': scaler,
    'GenderLE': le
}

dump(dumpattr,'Indian Liver Patient Dataset.joblib')