import numpy as np
import pickle
import streamlit as st

rfc_loaded_model = pickle.load(open('Random_forest_Chronic_kidney.sav','rb'))
gbc_loaded_model = pickle.load(open('Gradient_Boosting_Chronic_kidney.sav','rb'))
sgbc_loaded_model = pickle.load(open('Stochastic_Gradient_Boosting_Chronic_kidney.sav','rb'))
xgb_loaded_model = pickle.load(open('XgBoost_Chronic_kidney.sav','rb'))
cat_loaded_model = pickle.load(open('Cat_Boost_Chronic_kidney.sav','rb'))
etc_loaded_model = pickle.load(open('Extra_Trees_Classifier_Chronic_kidney.sav','rb'))
ada_loaded_model = pickle.load(open('Ada_Boost_Classifier_Chronic_kidney.sav','rb'))
dtc_loaded_model = pickle.load(open('Decision_Tree_Classifier_Chronic_kidney.sav','rb'))
knn_loaded_model = pickle.load(open('KNN_Chronic_kidney.sav','rb'))
svm_loaded_model = pickle.load(open('Support_Vector_Machine_Chronic_kidney.sav','rb'))
lr_loaded_model = pickle.load(open('Logistic_Regression_Chronic_kidney.sav','rb'))
all_models = [rfc_loaded_model,gbc_loaded_model,sgbc_loaded_model,xgb_loaded_model,cat_loaded_model,etc_loaded_model,ada_loaded_model,dtc_loaded_model,knn_loaded_model,svm_loaded_model,lr_loaded_model]


def chronic_kidney_prediction(input_data):
    # input_data = (0,137,40,35,168,43.1,2.288,33)
    input_data_as_array = np.asarray(input_data)
    input_data_reshape = input_data_as_array.reshape(1,-1)
    ckd = 0
    not_ckd = 0
    for model in all_models:
        prediction = model.predict(input_data_reshape) # this is where the prediction happens
        if prediction[0] == 0:
            ckd += 1
            print('The person have Chronic Kidney Disease with '+str(model))
        else:
            not_ckd += 1
            print('The person doesn\'t have Chronic Kidney Disease with '+str(model))
    print('Chronic Kidney Disease Count:',ckd)
    print('Chronic Kidney doesn\'t have count:' ,not_ckd)
    if(ckd > not_ckd):
        return "The person have Chronic Kidney Disease"
    else:
        return "The person doesn\'t have Chronic Kidney Disease"
    
    # print(prediction)
    # if prediction[0]==0:
    #     return 'The person has Chronic Kidney Disease'
    # else:
    #     return 'The person doesn\'t have Chronic  Kidney Disease'

def main():
    # giving a title
    st.title('Chronic Kidney Prediction Web App') 
    
    # Getting the input data from users
    age = st.number_input('Age of the Person',value=None,placeholder="Type a number...")
    blood_pressure = st.number_input('Blood Pressure [50-180]',value=None,placeholder="Type a number...")
    specific_gravity = st.number_input('Specific Gravity [1.005-1.02]',value=None,placeholder="Type a number...")
    albumin = st.number_input('Albumin [0-5]',value=None,placeholder="Type a number...")
    sugar = st.number_input('Sugar [0-5]',value=None,placeholder="Type a number...")
    red_blood_cells = st.number_input('Red Blood Cells [normal-1,abnormal-0]',value=None,placeholder="Type a number...")
    pus_cell = st.number_input('Pus Cell [normal-1,abnormal-0]',value=None,placeholder="Type a number...")
    pus_cell_clumps = st.number_input('pus_cell_clumps [present-1,not present-0]',value=None,placeholder="Type a number...")
    bacteria = st.number_input('Bacteria [present-1,not present-0]',value=None,placeholder="Type a number...")
    blood_glucose_random = st.number_input('Blood Glucose Random [60-500]',value=None,placeholder="Type a number...")
    blood_urea = st.number_input('Blood Urea [1.5-250]',value=None,placeholder="Type a number...")
    serum_creatinine = st.number_input('Serum Creatinine [0.4-76]',value=None,placeholder="Type a number...")
    sodium = st.number_input('Sodium [100-163]',value=None,placeholder="Type a number...")
    potassium = st.number_input('Potassium [2.5-47]',value=None,placeholder="Type a number...")
    haemoglobin = st.number_input('Haemoglobin [3.1-17.8]',value=None,placeholder="Type a number...")
    packed_cell_volume = st.number_input('Packed Cell Volume [14-55]',value=None,placeholder="Type a number...")
    white_blood_cell_count = st.number_input('White Blood Cell Count [2000-20000]',value=None,placeholder="Type a number...")
    red_blood_cell_count = st.number_input('Red Blood Cell Count [2.1-6.5] millions',value=None,placeholder="Type a number...")
    hypertension = st.number_input('Hypertension [Yes-1,No-0]',value=None,placeholder="Type a number...")
    diabetes_mellitus = st.number_input('Diabetes Mellitus [Yes-1,No-0]',value=None,placeholder="Type a number...")
    coronary_artery_disease = st.number_input('Coronary Artery Disease [Yes-1,No-0]',value=None,placeholder="Type a number...")
    appetite = st.number_input('Appetite [Good-0,Poor-1]',value=None,placeholder="Type a number...")
    peda_edema = st.number_input('Peda Edema [Yes-1,No-0]',value=None,placeholder="Type a number...")
    aanemia = st.number_input('Aanemia [Yes-1,No-0]',value=None,placeholder="Type a number...")
    
    
    
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