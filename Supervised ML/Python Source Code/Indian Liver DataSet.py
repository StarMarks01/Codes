import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score,precision_score,f1_score,recall_score,confusion_matrix

df = pd.read_csv(r"c:\Users\Yagnesh Narola\Documents\Coding Languages\Artificial Intelligence\Excel_and_CSV\indian liver patient.csv")
print(df)

le = LabelEncoder()
scaler = StandardScaler()
model = LogisticRegression()
dt = DecisionTreeClassifier(criterion = 'entropy',random_state = 42)

print(df.isnull().sum())
print(df.info())
print(df.shape)

df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(df['Albumin_and_Globulin_Ratio'].mean())

# for i in df.columns:
#     print(sns.boxplot(df[i]))
#     mp.show()

print(df.describe())

df2 = df.copy()
df2['Gender'] = le.fit_transform(df2['Gender'])

def Outliers(df,columns):
    for i in columns:
        df[i] = df[i].astype(float)
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1
        upperlimit = q3 + (1.5 * iqr)
        lowerlimit = q1 - (1.5 * iqr)
        print(f"\nColumn: {i}")
        print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")
        print(f"Lower Limit: {lowerlimit}, Upper Limit: {upperlimit}")
        print(f"Values above upper limit: {(df[i] > upperlimit).sum()}")
        print(f"Values below lower limit: {(df[i] < lowerlimit).sum()}")

        df[i] = df[i].mask(df[i] > upperlimit, upperlimit)
        df[i] = df[i].mask(df[i] < lowerlimit, lowerlimit)
        return df
cols = ['Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Aspartate_Aminotransferase','Total_Protiens','Albumin_and_Globulin_Ratio']
df2 = Outliers(df2,cols)

print(df2,df.shape)

x = df2.drop(columns = 'Dataset')
y = df2['Dataset']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70,test_size = 0.3)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)
model.fit(xtrainscaled,ytrain)
logic = model.score(xtestscaled,ytest)

dt.fit(xtrainscaled,ytrain)
decision = dt.score(xtestscaled,ytest)

print("LogisticRegression Score",logic)
print("DecisionTreeClassifier Score",decision)

df3 = pd.read_csv(r"C:\Users\Yagnesh Narola\Documents\Coding Languages\Artificial Intelligence\Codings\Adult.csv")

df3 = df3.drop(columns=['fnlwgt', 'education', 'relationship', 'native-country', 'race','capital-gain','capital-loss'])

cols = ['age','hours-per-week','capital-gain','capital-loss']

def Outliers(df, columns):
    for col in columns:
        if col in df.select_dtypes(include=['number']).columns:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            upperlimit = q3 + (1.5 * iqr)
            lowerlimit = q1 - (1.5 * iqr)
            df[col] = df[col].clip(lower=lowerlimit, upper=upperlimit)
    return df
df3 = Outliers(df3, cols)

df3["income"] = le.fit_transform(df3['income'])
df3['workclass'] = le.fit_transform(df3['workclass'])
df3['marital-status'] = le.fit_transform(df3['marital-status'])
df3['occupation'] = le.fit_transform(df3['occupation'])
df3['gender'] = le.fit_transform(df3['gender'])

x = df3.drop(columns = "income")
y = df3["income"]

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70, test_size = 0.3)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)
model.fit(xtrainscaled,ytrain)
logic = model.score(xtestscaled,ytest)

dt.fit(xtrainscaled,ytrain)
dcs = dt.score(xtestscaled,ytest)

print("Logistic Regression",logic)
print("DecisionTree Classifier",dcs)