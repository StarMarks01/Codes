import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,StandardScaler,PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from joblib import dump, load
import os

scriptdir = os.path.split(os.path.realpath(__file__))[0]
filepath = os.path.join(scriptdir, "Data Train.xlsx")
df = pd.read_excel(r"C:\Users\Yagnesh Narola\Documents\Coding Languages\Artificial Intelligence\Excel_and_CSV\Data Train.xlsx")

df.isnull().sum()

df2 = df.copy()
le = LabelEncoder()
dtr = DecisionTreeRegressor()
scaler = StandardScaler()
model = LinearRegression()
model2 = LinearRegression()
rd = Ridge()
ls = Lasso()
poly = PolynomialFeatures(degree = 2)
rfr = RandomForestRegressor(n_estimators = 150)

AirlineLE = LabelEncoder()
SourceLE = LabelEncoder()
DestinationLE = LabelEncoder()
Dep_Day_TimeLE = LabelEncoder()
Arrival_Day_timeLE = LabelEncoder()
Additional_InfoLE = LabelEncoder()
Total_StopsLE = LabelEncoder()

df2 = df2.drop(columns = ['Route','Duration'])

df2['Additional_Info'] = df2['Additional_Info'].str.replace('No info', 'No Info')
df2['Additional_Info'] = df2['Additional_Info'].str.lower().str.strip()

df2['Date_of_Journey'] = pd.to_datetime(df2['Date_of_Journey'], format='%d/%m/%Y')

df2['month'] = df2['Date_of_Journey'].dt.month
df2['date'] = df2['Date_of_Journey'].dt.day
df2['year'] = df2['Date_of_Journey'].dt.year

df2 = df2.drop(columns = 'Date_of_Journey')

df2['Dep_Time'] = pd.to_datetime(df2['Dep_Time'], format='%H:%M')
df2['Departure_Hour'] = df2['Dep_Time'].dt.hour
df2['Departure_Minute'] = df2['Dep_Time'].dt.minute

df2['Arrival_Time'] = df2['Arrival_Time'].str.split().apply(lambda x: x[0])
df2['Arrival_Time'] = pd.to_datetime(df2['Arrival_Time'], format='%H:%M')
df2['Arrival_Hour'] = df2['Arrival_Time'].dt.hour
df2['Arrival_Minute'] = df2['Arrival_Time'].dt.minute

df2.drop(columns=['Dep_Time', 'Arrival_Time'], inplace=True)

def DayTime(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'
df2['Dep_Day_Time'] = df2['Departure_Hour'].apply(DayTime)
df2['Arrival_Day_Time'] = df2['Arrival_Hour'].apply(DayTime)

AirlineLE.fit(df2['Airline'])
SourceLE.fit(df2['Source'])
DestinationLE.fit(df2['Destination'])
Total_StopsLE.fit(df2['Total_Stops'])
Additional_InfoLE.fit(df2['Additional_Info'])
Dep_Day_TimeLE.fit(df2['Dep_Day_Time'])
Arrival_Day_timeLE.fit(df2['Arrival_Day_Time'])

df2['Airline'] = AirlineLE.fit_transform(df2['Airline'])
df2['Source'] = SourceLE.fit_transform(df2['Source'])
df2['Destination'] = DestinationLE.fit_transform(df2['Destination'])
df2['Total_Stops'] = Total_StopsLE.fit_transform(df2['Total_Stops'])
df2['Additional_Info'] = Additional_InfoLE.fit_transform(df2['Additional_Info'])
df2['Dep_Day_Time'] = Dep_Day_TimeLE.fit_transform(df2['Dep_Day_Time'])
df2['Arrival_Day_Time'] = Arrival_Day_timeLE.fit_transform(df2['Arrival_Day_Time'])

def Outliers(df,columns):
    q1 = df[columns].quantile(0.25)
    q3 = df[columns].quantile(0.75)
    iqr = q3 - q1
    upperlimit = q3 + (1.5 * iqr)
    lowerlimit = q1 - (1.5 * iqr)
    df.loc[(df[columns] > upperlimit),columns] = upperlimit
    df.loc[(df[columns] < lowerlimit),columns] = lowerlimit
    return df

df2 = Outliers(df2,'Price')

df2['Departure_Time'] = df2['Departure_Hour'] * 60 + df2['Departure_Minute']
df2['Departure_Time'] = df2['Arrival_Hour'] * 60 + df2['Arrival_Minute']

df2 = df2.drop(columns=['year', 'month', 'date','Arrival_Hour','Arrival_Minute','Departure_Hour','Departure_Minute'])

x = df2.drop(columns = 'Price')
y = df2['Price']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70,test_size = 0.3)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)
model.fit(xtrainscaled,ytrain)
linears = model.score(xtestscaled,ytest)

poly.fit(xtrain)
xtrainpoly = poly.transform(xtrain)
xtestpoly = poly.transform(xtest)
model2.fit(xtrainpoly,ytrain)
polys = model2.score(xtestpoly,ytest)

dtr.fit(xtrainscaled,ytrain)
dtrs = dtr.score(xtestscaled,ytest)

rd.fit(xtrainscaled,ytrain)
ridge = rd.score(xtestscaled,ytest)

ls.fit(xtrainscaled,ytrain)
lasso = ls.score(xtestscaled,ytest)

rfr.fit(xtrainscaled,ytrain)
rfrs = rfr.score(xtestscaled,ytest) 

print("Regression Score:")
print("Linear Regression:",linears)
print("Lasso Regression:",lasso)
print("Decision Tree Regressor:",dtrs)
print("Ridge Regression:",ridge)
print("Polynomial Feature Regression:",polys)
print("Random Forest Regressor:",rfrs)

dump({
    'model': rfr,
    'AirlineLE': AirlineLE,
    'SourceLE': SourceLE,
    'DestinationLE': DestinationLE,
    'Dep_Day_TimeLE': Dep_Day_TimeLE,
    'Arrival_Day_TimeLE': Arrival_Day_timeLE,
    'Additional_InfoLE': Additional_InfoLE,
   'scaler': scaler
 
}, 'Price Prediction.pkl')