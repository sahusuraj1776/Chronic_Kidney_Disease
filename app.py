import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/Sahu Suraj/OneDrive/Documents/SEM 6 MiniProject/Chronic_kidney.sav','rb'))  # Read Binary

def chronic_kidney_prediction(input_data):
    # input_data = (0,137,40,35,168,43.1,2.288,33)
    input_data_as_array = np.asarray(input_data)
    input_data_reshape = input_data_as_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)
    if prediction[0]==0:
        return 'The person has Chronic Kidney Disease'
    else:
        return 'The person doesn\'t have Chronic  Kidney Disease'

def main():
    # giving a title
    st.title('Chronic Kidney Prediction Web App') 
    
    # Getting the input data from users
    age = st.text_input('Age of the Person')
    blood_pressure = st.text_input('Blood Pressure [50-180]')
    specific_gravity = st.text_input('Specific Gravity [1.005-1.02]')
    albumin = st.text_input('Albumin [0-5]')
    sugar = st.text_input('Sugar [0-5]')
    red_blood_cells = st.text_input('Red Blood Cells [normal-1,abnormal-0]')
    pus_cell = st.text_input('Pus Cell [normal-1,abnormal-0]')
    pus_cell_clumps = st.text_input('pus_cell_clumps [present-1,not present-0]')
    bacteria = st.text_input('Bacteria [present-1,not present-0]')
    blood_glucose_random = st.text_input('Blood Glucose Random [22-490]')
    blood_urea = st.text_input('Blood Urea [1.5-391]')
    serum_creatinine = st.text_input('Serum Creatinine [0.4-76]')
    sodium = st.text_input('Sodium [4.5-163]')
    potassium = st.text_input('Potassium [2.5-47]')
    haemoglobin = st.text_input('Haemoglobin [3.1-17.8]')
    packed_cell_volume = st.text_input('Packed Cell Volume [9-54]')
    white_blood_cell_count = st.text_input('White Blood Cell Count [2200-26400]')
    red_blood_cell_count = st.text_input('Red Blood Cell Count [2.1-8] millions')
    hypertension = st.text_input('Hypertension [Yes-1,No-0]')
    diabetes_mellitus = st.text_input('Diabetes Mellitus [Yes-1,No-0]')
    coronary_artery_disease = st.text_input('Coronary Artery Disease [Yes-1,No-0]')
    appetite = st.text_input('Appetite [Good-0,Poor-1]')
    peda_edema = st.text_input('Peda Edema [Yes-1,No-0]')
    aanemia = st.text_input('Aanemia [Yes-1,No-0]')
    
    
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Chronic Kidney Test Result'):
        diagnosis = chronic_kidney_prediction([age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, 
              pus_cell,pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium,
              potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
              hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema,
              aanemia])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()