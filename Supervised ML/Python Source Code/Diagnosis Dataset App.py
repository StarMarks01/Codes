from joblib import load
import pandas as pd
import streamlit as st

data = load(r"C:\Users\Administrator\Documents\Yagnesh\Diagnosis Data.joblib")

model = data['model']
logic = data['logic']
dtc = data['dtc']
scaler = data['scaler']
DiagnosisLE = data['DiagnosisLE']

st.title("Diagnosis Prediction")

radius_mean = st.number_input("Radius Mean", min_value = 7, max_value = 22, value = 14)
texture_mean = st.number_input("Texture Mean", min_value = 10, max_value = 30, value = 19)
smoothness_mean = st.number_input("Smoothness Mean", min_value = 0, max_value = 1, value = 0)
symmetry_mean = st.number_input("Symmetry Mean", min_value = 0, max_value = 1, value = 0)
fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value = 0, max_value = 1, value = 0)
radius_se = st.number_input("Radius Standard Error", min_value = 0, max_value = 1, value = 0)
texture_se = st.number_input("Texture Standard Error", min_value = 0, max_value = 2, value = 1)
perimeter_se = st.number_input("Perimeter Standard Error", min_value = 1, max_value = 6, value = 3)
area_se = st.number_input("Area Standard Error", min_value = 7, max_value = 86, value = 35)
smoothness_se = st.number_input("Smoothness Standard Error", min_value = 0, max_value = 1, value = 0)
compactness_se = st.number_input("Compactness Standard Error", min_value = 0, max_value = 1, value = 0)
concavity_se = st.number_input("Concavity Standard Error", min_value = 0, max_value = 1, value = 0)
concave_points_se = st.number_input("Concave Points Standard Error", min_value = 0, max_value = 1, value = 0)
symmetry_se = st.number_input("Symmetry Standard Error", min_value = 0, max_value = 1, value = 0)
fractal_dimension_se = st.number_input("Fractal Dimension Standard Error", min_value = 0, max_value = 1, value = 0)
radius_worst = st.number_input("Radius Worst", min_value = 8, max_value = 27, value = 16)
texture_worst = st.number_input("Texture Worst", min_value = 12, max_value = 43, value = 26)
smoothness_worst = st.number_input("Smoothness Worst", min_value = 0, max_value = 1, value = 0)
symmetry_worst = st.number_input("Symmetry Worst", min_value = 0, max_value = 1, value = 0)
fractal_dimension_worst = st.number_input("Fractal Dimension Worst", min_value = 0, max_value = 1, value = 0)

if st.button("Predict"):
    ipdata = pd.DataFrame({
    'radius_mean': [radius_mean],
    'texture_mean': [texture_mean],
    'smoothness_mean': [smoothness_mean],
    'symmetry_mean': [symmetry_mean],
    'fractal_dimension_mean': [fractal_dimension_mean],
    'radius_se': [radius_se],
    'texture_se': [texture_se],
    'perimeter_se': [perimeter_se],
    'area_se': [area_se],
    'smoothness_se': [smoothness_se],
    'compactness_se': [compactness_se],
    'concavity_se': [concavity_se],
    'concave points_se': [concave_points_se],
    'symmetry_se': [symmetry_se],
    'fractal_dimension_se': [fractal_dimension_se],
    'radius_worst': [radius_worst],  # Added missing column
    'texture_worst': [texture_worst],
    'smoothness_worst': [smoothness_worst],
    'symmetry_worst': [symmetry_worst],
    'fractal_dimension_worst': [fractal_dimension_worst]
    })
    datascaled = scaler.transform(ipdata)
    pred = model.predict(datascaled)
    pred = pred.astype(int)
    OriginLE = DiagnosisLE.inverse_transform(pred)
    st.write(f"Dataset Prediction: {OriginLE[0]}")