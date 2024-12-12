import streamlit as st
import pickle
import numpy as np

with open('rf_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title('Breast Cancer Prediction App')
st.write('This is a simple app to predict if a patient has breast cancer based on some features')

st.header("Enter Patient Values:")
radius_mean = st.number_input("Radius Mean", min_value=0.0, value=14.0)
texture_mean = st.number_input("Texture Mean", min_value=0.0, value=20.0)
perimeter_mean = st.number_input("Perimeter Mean", min_value=0.0, value=80.0)
area_mean = st.number_input("Area Mean", min_value=0.0, value=600.0)
smoothness_mean = st.number_input("Smoothness Mean", min_value=0.0, value=0.1)
compactness_mean = st.number_input("Compactness Mean", min_value=0.0, value=0.2)
concavity_mean = st.number_input("Concavity Mean", min_value=0.0, value=0.3)
concave_points_mean = st.number_input("Concave Points Mean", min_value=0.0, value=0.1)
symmetry_mean = st.number_input("Symmetry Mean", min_value=0.0, value=0.2)
fractal_dimension_mean = st.number_input("Fractal Dimension Mean", min_value=0.0, value=0.05)
radius_se = st.number_input("Radius SE", min_value=0.0, value=1.5)
texture_se = st.number_input("Texture SE", min_value=0.0, value=1.5)
perimeter_se = st.number_input("Perimeter SE", min_value=0.0, value=1.5)
area_se = st.number_input("Area SE", min_value=0.0, value=150.0)
smoothness_se = st.number_input("Smoothness SE", min_value=0.0, value=0.01)
compactness_se = st.number_input("Compactness SE", min_value=0.0, value=0.02)
concavity_se = st.number_input("Concavity SE", min_value=0.0, value=0.02)
concave_points_se = st.number_input("Concave Points SE", min_value=0.0, value=0.01)
symmetry_se = st.number_input("Symmetry SE", min_value=0.0, value=0.02)
fractal_dimension_se = st.number_input("Fractal Dimension SE", min_value=0.0, value=0.004)
radius_worst = st.number_input("Radius Worst", min_value=0.0, value=16.0)
texture_worst = st.number_input("Texture Worst", min_value=0.0, value=25.0)
perimeter_worst = st.number_input("Perimeter Worst", min_value=0.0, value=100.0)
area_worst = st.number_input("Area Worst", min_value=0.0, value=800.0)
smoothness_worst = st.number_input("Smoothness Worst", min_value=0.0, value=0.12)
compactness_worst = st.number_input("Compactness Worst", min_value=0.0, value=0.3)
concavity_worst = st.number_input("Concavity Worst", min_value=0.0, value=0.4)
concave_points_worst = st.number_input("Concave Points Worst", min_value=0.0, value=0.15)
symmetry_worst = st.number_input("Symmetry Worst", min_value=0.0, value=0.3)
fractal_dimension_worst = st.number_input("Fractal Dimension Worst", min_value=0.0, value=0.07)

# Özellikleri birleştir
features = np.array([
    radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
    concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se,
    perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se,
    symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst,
    smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
    fractal_dimension_worst
]).reshape(1, -1)

if st.button("Make Prediction"):
    prediction = model.predict(features)[0]
    if prediction == 0:
        st.success("Result: (Benign)")
    else:
        st.error("Result: (Malignant)")