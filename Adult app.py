import joblib as jb
import streamlit as st
import pandas as pd

data = jb.load(r"C:\Users\Pavilion\Documents\Coding Languages\Artificial Intelligence\Codings\Adult Dataset Data.joblib")

OccupationLE = data['OccupationLE']
WorkClassLE = data['WorkClassLE']
RaceLE = data['RaceLE']
GenderLE = data['GenderLE']
EducationLE = data['EducationLE']
model = data['model']
scaler = data['scaler']
logic = data['logic']
dtc = data['dtc']
IncomeLE = data['IncomeLE']

st.title("Average Adult Salary Prediction")

Age = st.number_input("Age", min_value=0, max_value=75, value = 18)
Education = st.selectbox("Education",EducationLE.classes_)
Occupation = st.selectbox("Occupation",OccupationLE.classes_)
WorkClass = st.selectbox("Work Class",WorkClassLE.classes_)
Gender = st.selectbox("Gender",GenderLE.classes_)
Race = st.selectbox("Race",RaceLE.classes_)
HoursSpent = st.number_input("Work Hours Per Week",min_value = 0,max_value = 168,value = 48)

if st.button('Predict'):
    EducationEnc = EducationLE.transform([Education])[0]
    OccupationEnc = OccupationLE.transform([Occupation])[0]
    WorkClassEnc = WorkClassLE.transform([WorkClass])[0]
    GenderEnc = GenderLE.transform([Gender])[0]
    RaceEnc = RaceLE.transform([Race])[0]
    ipdata = pd.DataFrame({
        'age':[Age],
        'workclass': [WorkClassEnc],
        'education': [EducationEnc],
        'occupation': [OccupationEnc],
        'race': [RaceEnc],
        'gender': [GenderEnc],
        'hours-per-week': [HoursSpent]
    })
    st.write("Your Input Data")
    st.write(ipdata)
    datascaled = scaler.transform(ipdata)
    pred = model.predict(datascaled)
    st.write(f"Predicted Income: {IncomeLE.inverse_transform(pred)[0]}")