from joblib import load
import streamlit as st
import pandas as pd

data = load(r"C:\Users\Administrator\Documents\Yagnesh\Indian Liver Patient Dataset.joblib")

GenderLE = data['GenderLE']
model = data['model']
scaler = data['scaler']
dtc = data['dtc']
logic = data['logic']

st.title("Indian Liver Patient Prediction")

Age = st.number_input("Age", min_value=0, max_value=90, value = 18)
Gender = st.selectbox("Gender", GenderLE.classes_)
TotalBilirubin = st.number_input("Total Bilirubin", min_value=0, max_value = 6, value = 1)
DirectBilirubin = st.number_input("Direct Bilirubin",min_value = 0,max_value= 3, value = 1)
AlkalinePhosphotase = st.number_input("Alkaline Phosphotase",min_value = 63,max_value= 490, value = 70)
AlamineAminotransferase = st.number_input("Alamine Aminotransferase",min_value = 10,max_value= 116, value = 40)
AspartateAminotransferase = st.number_input("Aspartate Aminotransferase",min_value = 10,max_value= 180, value = 10)
TotalProtiens = st.number_input("Total Protiens",min_value = 3,max_value= 10, value = 4)
Albumin = st.number_input("Albumin",min_value = 0,max_value= 6, value = 1)

if st.button('Predict'):
    GenderEnc = GenderLE.transform([Gender])
    ipdata = pd.DataFrame({
        'Age':[Age],
        'Gender': [GenderEnc],
        'Total_Bilirubin': [TotalBilirubin],
        'Direct_Bilirubin': [DirectBilirubin],
        'Alkaline_Phosphotase': [AlkalinePhosphotase],
        'Alamine_Aminotransferase': [AlamineAminotransferase],
        'Aspartate_Aminotransferase': [AspartateAminotransferase],
        'Total_Protiens': [TotalProtiens],
        'Albumin': [Albumin],
    })
    st.write("Your Input Data")
    st.write(ipdata)
    datascaled = scaler.transform(ipdata)
    pred = model.predict(datascaled)
    st.write(f"Has Dataset?: {pred[0]}")