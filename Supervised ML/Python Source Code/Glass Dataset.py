import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import  RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from joblib import dump

df = pd.read_csv(r'C:/Users/Administrator/Documents/Yagnesh/Glass Dataset.csv')

df2 = df.copy()
scaler = StandardScaler()
logic = LogisticRegression()
dtc = DecisionTreeClassifier()
model = RandomForestClassifier(n_estimators = 150)

df2 = df2.drop(columns = ['Ba','Fe','RI'])

def Outliers(df,columns):
    for i in columns:
        df[i].astype(int)
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1
        upperlimit = q3 + (1.5 * iqr)
        lowerlimit = q1 - (1.5 * iqr)
        df.loc[(df[i] > upperlimit), i] = upperlimit
        df.loc[(df[i] < lowerlimit), i] = lowerlimit
    return df
cols = ['Na','Mg','Al','Si','K','Ca','Type']
df2 = Outliers(df2,cols)

x = df2.drop(columns = 'Type')
y = df2['Type']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70, test_size = 0.3)

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
print("Logistic Regression Score",logics)
print("Decision Tree Classifier Score",dtcs)
print("Random Forest Classifier Score",rfcs)

dumpattr = {
    'model': model,
    'dtc': dtc,
    'logic': logic,
    'scaler': scaler
}

dump(dumpattr,'Glass Data.joblib')

print(df2.describe())
print(df2)