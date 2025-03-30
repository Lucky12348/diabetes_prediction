"""contains the code for the web application user interface"""

import streamlit as st
from app.model_loader import load_model, load_scaler
from app.predictor import DiabetesPredictor

def encode_bmi_category(bmi):
    if bmi < 18.5:
        return 0  # Underweight
    elif bmi < 25:
        return 1  # Normal weight
    elif bmi < 30:
        return 2  # Overweight
    elif bmi < 35:
        return 3  # Obese
    else:
        return 4  # Severely obese

def run_ui():

    st.set_page_config(page_title="Predicting Diabetes",layout="centered")
    st.title("Predicting Diabetes")

    # load model
    model = load_model()
    scaler = load_scaler()
    predictor = DiabetesPredictor(model,scaler)

    # form in 2 columns & input
    with st.form("diabetes_form"):
        col1, col2 = st.columns(2)

        with col1:
            pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
            glucose = st.number_input("Plasma Glucose", min_value=0)
            pressure = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=0)
            thickness = st.number_input("Triceps Skin Fold Thickness (mm)", min_value=0)

        with col2:
            insulin = st.number_input("2-Hour Serum Insulin (mu U/ml)", min_value=0)
            bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0)
            pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0)
            age = st.number_input("Age", min_value=0, step=1)

        submitted = st.form_submit_button("Predict Risk")

    if submitted:
        bmi_category = encode_bmi_category(bmi)
        
        input_data = {
            "Pregnancies": pregnancies,
            "PlasmaGlucose": glucose,
            "DiastolicBloodPressure": pressure,
            "TricepsThickness": thickness,
            "SerumInsulin": insulin,
            "BMI": bmi,
            "DiabetesPedigree": pedigree,
            "Age": age,
            "bmi_category": bmi_category
        }

        if sum(input_data.values()) == 0:
            st.warning("Enter patient informations") # make sure some data is entered
        else: # make prediction
            prediction = predictor.predict(input_data)
            if prediction == 1:
                st.error("diabetic")
            else:
                st.success("non-diabetic")
