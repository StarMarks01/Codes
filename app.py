import streamlit as st
import joblib as jb
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

scriptdir = os.path.dirname(os.path.abspath(__file__))
pklpath = os.path.join(scriptdir, "Price Prediction.pkl")
jb.dump({'Price Prediction.pkl'}, pklpath)

data = jb.load('Price Prediction.pkl')
model = data['model']
AirlineLE = data['AirlineLE']
SourceLe = data['SourceLE']
DestinationLE = data['DestinationLE']
Dep_Day_TimeLE = data['Dep_Day_TimeLE']
Arrival_Day_TimeLE = data['Arrival_Day_TimeLE']
Additional_InfoLE = data['Additional_InfoLE']
scaler = data['scaler']

st.title("Flight Price Prediction")

Airline = st.selectbox("Airline", AirlineLE.classes_)
Source = st.selectbox("Source", SourceLe.classes_)
Destination = st.selectbox("Destination", DestinationLE.classes_)
Total_Stops = st.number_input("Total Stops", min_value=0, max_value=4, value=1)
Additional_Info = st.selectbox("Additional_Info",Additional_InfoLE.classes_)
Dep_Day_Time = st.selectbox("Departure Day Time", Dep_Day_TimeLE.classes_)
Arrival_Day_time = st.selectbox("Arrival Day Time", Arrival_Day_TimeLE.classes_)
Departure_Time = st.number_input("Departure Time", min_value=0, max_value=1440, value=720)

if st.button("Predict"):
    AirlineEnc = AirlineLE.transform([Airline])[0]
    SourceEnc = SourceLe.transform([Source])[0]
    DestinationEnc = DestinationLE.transform([Destination])[0]
    Additional_InfoEnc = Additional_InfoLE.transform([Additional_Info])[0]
    Dep_Day_TimeEnc = Dep_Day_TimeLE.transform([Dep_Day_Time])[0]
    Arrival_Day_timeEnc = Arrival_Day_TimeLE.transform([Arrival_Day_time])[0]
    ipdata = pd.DataFrame({
        'Airline': [AirlineEnc],
        'Source': [SourceEnc],
        'Destination': [DestinationEnc],
        'Total_Stops': [Total_Stops],
        'Additional_Info': [Additional_InfoEnc],
        'Departure_Day_Time': [Dep_Day_TimeEnc],
        'Arrival_Day_time': [Arrival_Day_timeEnc],
        'Departure_Time': [Departure_Time]
    })
    st.write("Your Input Data:")
    st.write(ipdata)
    datascaled = scaler.transform(ipdata)
    pred = model.predict(datascaled)
    st.write(f"Predicted Price: {pred[0]:.2f} INR")