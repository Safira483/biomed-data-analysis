# src/dashboard.py
import streamlit as st
import pandas as pd
import joblib

st.title("BioPulse AI Dashboard")
st.write("Sistema de monitoreo de signos vitales con ML")

# Cargar modelo
model = joblib.load("src/pulse_model.pkl")

# Subir CSV de pulso
uploaded_file = st.file_uploader("Sube tus datos de pulso (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Datos cargados:")
    st.dataframe(df.head())
    
    # Predecir condición
    predictions = model.predict(df[['pulse','spo2']])
    df['prediction'] = predictions
    st.write("Predicciones:")
    st.dataframe(df)
    
    # Conteo de resultados
    st.write("Resumen de condiciones detectadas:")
    st.bar_chart(df['prediction'].value_counts())
