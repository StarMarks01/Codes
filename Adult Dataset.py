import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from joblib import dump

df = pd.read_csv(r"C:\Users\Pavilion\Documents\Coding Languages\Artificial Intelligence\Excel and Csv\Adult.csv")

OccupationLE = LabelEncoder()
WorkClassLE = LabelEncoder()
RaceLE = LabelEncoder()
GenderLE = LabelEncoder()
IncomeLE = LabelEncoder()
EducationLE = LabelEncoder()

scaler = StandardScaler()
model = RandomForestClassifier(n_estimators = 100)
dtc = DecisionTreeClassifier()
logic = LogisticRegression()

df2 = df.copy()

df2 = df2.drop(columns = ['educational-num','marital-status','native-country','relationship','fnlwgt'])

df2 = df2.replace('?',pd.NA)
df2 = df2.dropna()

df2['income'] = df2['income'].str.replace('<=50K','More Than OR Equal To 50K')
df2['income'] = df2['income'].str.replace('>50K','Less Than 50K')

OccupationLE.fit(df2['occupation'])
WorkClassLE.fit(df2['workclass'])
RaceLE.fit(df2['race'])
GenderLE.fit(df2['gender'])
IncomeLE.fit(df2['income'])
EducationLE.fit(df2['education'])

df2['occupation'] = OccupationLE.transform(df2['occupation'])
df2['workclass'] = WorkClassLE.transform(df2['workclass'])
df2['race'] = RaceLE.transform(df2['race'])
df2['gender'] = GenderLE.transform(df2['gender'])
df2['income'] = IncomeLE.transform(df2['income'])
df2['education'] = EducationLE.transform(df2['education'])

def Outliers(df,columns):
    df[columns].astype(float)
    q1 = df[columns].quantile(0.25)
    q3 = df[columns].quantile(0.75)
    iqr = q3 - q1
    upperlimit = q3 + (1.5 * iqr)
    lowerlimit = q1 - (1.5 * iqr)
    df[columns] = df[columns].clip(lower=lowerlimit, upper=upperlimit)
    return df[columns]
cols = ['age','capital-gain','capital-loss','hours-per-week']
for i in cols:
    df2[i] = Outliers(df2,i)

df2['age'] = df2['age'].astype(int)
df2['hours-per-week'] = df2['hours-per-week'].astype(int)

constcols = [col for col in df2.columns if df2[col].nunique() == 1]
df2 = df2.drop(columns = constcols)

x = df2.drop(columns = 'income')
y = df2['income']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70, test_size = 30)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)

logic.fit(xtrainscaled,ytrain)
logics = logic.score(xtestscaled,ytest)

dtc.fit(xtrainscaled,ytrain)
dtcs = dtc.score(xtestscaled,ytest)

model.fit(xtrainscaled,ytrain)
rfcs = model.score(xtestscaled,ytest)

print("Classification Scores:")
print("LogisticRegression:",logics)
print("DecisionTreeClassifier",dtcs)
print("RandomForestClassifier:",rfcs)

deployattr = {
    'OccupationLE': OccupationLE,
    'WorkClassLE': WorkClassLE,
    'RaceLE': RaceLE,
    'GenderLE': GenderLE,
    'IncomeLE': IncomeLE,
    'EducationLE': EducationLE,
    'model': model,
    'scaler': scaler,
    'logic' : logic,
    'dtc': dtc
}
dump(deployattr, 'Adult Dataset Data.joblib')