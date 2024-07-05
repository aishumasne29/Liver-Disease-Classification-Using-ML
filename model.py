import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import LabelEncoder

# Load the model
model = pickle.load(open('liver.pkl', 'rb'))

with st.sidebar:
    selected = option_menu("", ['Liver_Disease_Symptoms', 'Liver_Disease_Classification'])

# Liver Disease Symptoms Page
if selected == 'Liver_Disease_Symptoms':
    st.title('Liver Disease Symptoms')

    # Add image
    st.image('liversymptoms.jpg', caption='Liver Disease Symptoms',use_column_width=True)

# Liver Disease Classification Page
if selected == 'Liver_Disease_Classification':
    st.title('Liver Disease Classification using Machine Learning')

    # Input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input('Age', 0, 100)
        Gender = st.number_input('Gender', 0, 1)
        Total_Bilirubin = st.number_input('Total Bilirubin', 0.0, 20.0, value=0.0,format="%.1f")
        Direct_Bilirubin = st.number_input('Direct Bilirubin', 0.0, 20.0, value=0.0,format="%.1f")

    with col2:
        Alkaline_Phosphotase = st.number_input('Alkaline Phosphotase', 0, 1000)
        Alamine_Aminotransferase = st.number_input('Alamine Aminotransferase', 0, 100)
        Aspartate_Aminotransferase = st.number_input('Aspartate Aminotransferase', 0, 100)
        Total_Protiens = st.number_input('Total Proteins', 0.0, 10.0, value=0.0,format="%.1f") 

    with col3:
        Albumin = st.number_input('Albumin', 0.0, 10.0, value=0.0,format="%.1f")
        Albumin_and_Globulin_Ratio = st.number_input('Albumin and Globulin Ratio', 0.0, 10.0, value=0.0)

    # Prediction
    if st.button('Prediction'):
        input_data = [[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]]
        prediction = model.predict(input_data)[0]
        
        if prediction == 1:
            st.write('Patient has a Liver Disease')
        else:
            st.write('Patient does not have Liver Disease')