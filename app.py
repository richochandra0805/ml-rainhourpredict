import pandas as pd
import streamlit as st
import joblib
import os

@st.cache_data
def load_data():
    path = "data/Data_Rain_Manual1998-2025.xlsx"
    df = pd.read_excel(path)

    if 'Tanggal' not in df.columns:
        st.error("Kolom 'Tanggal' tidak ditemukan.")
        st.stop()

    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    df = df.dropna()
    df['dayofyear'] = df['Tanggal'].dt.dayofyear
    df['month'] = df['Tanggal'].dt.month
    return df

@st.cache_resource
def load_model():
    return joblib.load("model_rainhour_best_rf.pkl")

df = load_data()
model = load_model()

# Tambahkan UI untuk prediksi dll...
