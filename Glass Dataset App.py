from joblib import load
import pandas as pd
import streamlit as st

data = load(r"C:\Users\Administrator\Documents\Yagnesh\Glass Data.joblib")

model = data['model']
scaler = data['scaler']

st.title("Glass Type Prediction")

Na = st.number_input("Sodium",min_value = 11,max_value = 16,value = 15)
Mg = st.number_input("Magnesium",min_value = 0,max_value = 5,value = 1)
Al = st.number_input("Aluminum",min_value = 0,max_value = 3,value = 1)
Si = st.number_input("Silicon",min_value = 70,max_value = 100, value = 80)
K = st.number_input("Potassium",min_value = 0,max_value = 2, value = 1)
Ca = st.number_input("Calcium",min_value = 5,max_value = 10, value = 6)

if st.button("Predict"):
    ipdata = pd.DataFrame({
        'Na': [Na],
        'Mg': [Mg],
        'Al': [Al],
        'Si': [Si],
        'K': [K],
        'Ca': [Ca]
    })
    datascaled = scaler.transform(ipdata)
    pred = model.predict(datascaled)
    st.write(f"Glass Type: {pred[0]}")