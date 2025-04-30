import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from joblib import dump

df = pd.read_csv(r"C:\Users\Pavilion\Documents\Coding Languages\Artificial Intelligence\Excel and Csv\hotel bookings.csv")

df2 = df.copy()

pd.set_option('display.max_columns',None)

HotelLE = LabelEncoder()
Arrival_Date_MonthLE = LabelEncoder()
MealLE = LabelEncoder()
CountryLE = LabelEncoder()
Distribution_ChannelLE = LabelEncoder()
Deposit_TypeLE = LabelEncoder()
Customer_TypeLE = LabelEncoder()
Is_CancelledLE = LabelEncoder()
Reserved_Room_TypeLE = LabelEncoder()
scaler = StandardScaler()
model = RandomForestClassifier(n_estimators = 150)
dtc = DecisionTreeClassifier(criterion = 'entropy')
knn = KNeighborsClassifier(n_neighbors = 150)
logic = LogisticRegression()

df2 = df2.drop(columns = ['company','agent','assigned_room_type','market_segment','reservation_status','reservation_status_date','booking_changes'])

df2 = df2.fillna(df2['country'].mode()[0])

intvar = df2.select_dtypes(include = ['int','float'])
obvar = df2.select_dtypes(include = 'object')

intvar = intvar.drop(columns = 'is_canceled')

def Outliers(df,columns):
    for i in columns:
        q1 = df[i].quantile(0.25)
        q3 = df[i].quantile(0.75)
        iqr = q3 - q1
        upperlimit = q3 + (1.5 * iqr)
        lowerlimit = q1 - (1.5 * iqr)
        df.loc[(df[i] > upperlimit),i] = upperlimit
        df.loc[(df[i] < lowerlimit), i] = lowerlimit
    return df
df2 = Outliers(df2,intvar.columns)

df2['is_canceled'] = df2['is_canceled'].replace(1,'Yes')
df2['is_canceled'] = df2['is_canceled'].replace(0,'No')
df2['hotel'] = HotelLE.fit_transform(df2['hotel'])
df2['arrival_date_month'] = Arrival_Date_MonthLE.fit_transform(df2['arrival_date_month'])
df2['meal'] = MealLE.fit_transform(df2['meal'])
df2['country'] = CountryLE.fit_transform(df2['country'])
df2['distribution_channel'] = Distribution_ChannelLE.fit_transform(df2['distribution_channel'])
df2['deposit_type'] = Deposit_TypeLE.fit_transform(df2['deposit_type'])
df2['customer_type'] = Customer_TypeLE.fit_transform(df2['customer_type'])
df2['is_canceled'] = Is_CancelledLE.fit_transform(df2['is_canceled'])
df2['reserved_room_type'] = Reserved_Room_TypeLE.fit_transform(df2['reserved_room_type'])

df2['children'] = pd.to_numeric(df2['children'],errors = 'coerce')

df2['children'] = df2['children'].fillna(df2['children'].median())

x = df2.drop(columns = 'is_canceled')
y = df2['is_canceled']

xtrain,xtest,ytrain,ytest = train_test_split(x,y,random_state = 70, test_size = 0.3)

scaler.fit(xtrain)
xtrainscaled = scaler.transform(xtrain)
xtestscaled = scaler.transform(xtest)

logic.fit(xtrainscaled,ytrain)
LOGICS = logic.score(xtestscaled,ytest)

dtc.fit(xtrainscaled,ytrain)
DTCS = dtc.score(xtestscaled,ytest)

model.fit(xtrainscaled,ytrain)
RFCS = model.score(xtestscaled,ytest)

knn.fit(xtrainscaled,ytrain)
KNNS = knn.score(xtestscaled,ytest)

print("Classification Socres:")
print("Logistic Regression:",LOGICS)
print("Decision Tree Classifier:",DTCS)
print("Random Forest Classifier:",RFCS)
print("K-Nearest Neighbour Classifier:",KNNS)

HotelRes = {
    'HotelLE': HotelLE,
    'Arrival_Date_MonthLE':Arrival_Date_MonthLE,
    'MealLE' : MealLE,
    'CountryLE' : CountryLE,
    'Distribution_ChannelLE' : Distribution_ChannelLE,
    'Deposit_TypeLE': Deposit_TypeLE,
    'Customer_TypeLE': Customer_TypeLE,
    'Is_CancelledLE': Is_CancelledLE,
    'Reserved_Room_TypeLE': Reserved_Room_TypeLE,
    'scaler': scaler,
    'model': model,
    'dtc': dtc,
    'knn': knn,
    'logic': logic
}

dump(HotelRes,"Hotel Booking Resources.joblib")