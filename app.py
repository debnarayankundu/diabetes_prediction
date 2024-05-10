import numpy as np
import pandas as pd
import pickle
import streamlit as st
from PIL import Image

model=pickle.load(open('C:/Users/Debnarayan Kundu/projects/diabetes_prediction/diabetes_model.sav','rb'))



def main():
    st.title("Diabetes Prediction")
    
    # Input fields
    Pregnancies = st.text_input("No of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("BloodPressure")
    SkinThickness = st.text_input("SkinThickness")
    Insulin = st.text_input("Insulin")
    BMI = st.text_input("BMI")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction")
    Age = st.text_input("Age")

    diab_diagnosis=''
    
    # Prediction
    if st.button('Diabetes Test result'):
        # Convert input values to float
        input_data = [float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness), 
                      float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)]
        
        diab_prediction = model.predict([input_data])
        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is diabetic"
        else:
            diab_diagnosis = "The person is not diabetic"
    
    st.success(diab_diagnosis)

if __name__ == '__main__':
    main()
