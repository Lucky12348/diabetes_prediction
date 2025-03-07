import streamlit as st
import numpy as np
import joblib

# Caricare il modello salvato
model = joblib.load('model.pkl')

# Titolo dell'App
st.title("🔬 Diabetes Prediction App")
st.write("Inserisci i valori per ottenere una previsione.")

# Form per input utente
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
glucose = st.number_input("Plasma Glucose", min_value=50, max_value=250, value=100)
bp = st.number_input("Diastolic Blood Pressure", min_value=30, max_value=130, value=80)
insulin = st.number_input("Serum Insulin", min_value=0, max_value=500, value=79)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, format="%.1f")
pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, format="%.2f")
age = st.number_input("Age", min_value=18, max_value=100, value=30)
triceps = st.number_input("Triceps Thickness", min_value=0, max_value=100, value=20)

# Quando l'utente clicca sul bottone
if st.button("🔍 Predict"):
    # Creiamo l'array dei valori inputati
    input_data = np.array([[pregnancies, glucose, bp, triceps, insulin, bmi, pedigree, age]])

    # Fare la previsione
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[:, 1]

    # Mostrare il risultato
    if prediction[0] == 1:
        st.error(f"⚠️ High Risk of Diabetes! (Probability: {probability[0]:.2f})")
    else:
        st.success(f"✅ Low Risk of Diabetes (Probability: {probability[0]:.2f})")
