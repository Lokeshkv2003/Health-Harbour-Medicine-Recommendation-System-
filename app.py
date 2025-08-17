import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('model.pkl')

# Load the necessary datasets
medicine = pd.read_csv('medications1.csv.csv')  # Correct path to your medication dataset
precaution = pd.read_csv('precautions_df.csv')  # Correct path to your precautions dataset
diet = pd.read_csv('diets.csv')  # Correct path to your diet dataset
grouped_workout = pd.read_csv('workout_df.csv')  # Correct path to your workout dataset

# List of symptoms
symptoms = [' acidity', ' back_pain', ' bladder_discomfort', ' breathlessness', ' burning_micturition', ' chest_pain', ' chills', ' constipation', ' continuous_sneezing', ' cough', ' cramps', ' fatigue', ' headache', ' high_fever', ' indigestion', ' joint_pain', ' mood_swings', ' muscle_wasting', ' muscle_weakness', ' neck_pain', ' pain_during_bowel_movements', ' patches_in_throat', ' pus_filled_pimples', ' shivering', ' skin_rash',
             ' stiff_neck', ' stomach_pain', ' sunken_eyes', ' vomiting', ' weakness_in_limbs', ' weight_gain', ' weight_loss', ' yellowish_skin', 'itching', ' abdominal_pain', ' acidity', ' anxiety',
            ' blackheads', ' bladder_discomfort', ' blister', ' breathlessness', ' bruising', ' chest_pain', ' chills',
             ' cold_hands_and_feets', ' cough', ' cramps', ' dehydration', ' dizziness', ' fatigue', ' foul_smell_of urine', ' headache', ' high_fever', ' indigestion', ' joint_pain', ' knee_pain', ' lethargy', ' loss_of_appetite', ' mood_swings', ' nausea', ' neck_pain', ' nodal_skin_eruptions', ' pain_during_bowel_movements', ' pain_in_anal_region', 
             ' patches_in_throat', ' pus_filled_pimples', ' restlessness', ' shivering', ' skin_peeling', ' skin_rash', ' stiff_neck', ' stomach_pain', ' sunken_eyes', ' sweating', ' swelling_joints', ' ulcers_on_tongue', ' vomiting', ' weakness_in_limbs', ' weakness_of_one_body_side', ' weight_gain', ' weight_loss', ' yellowish_skin', ' abdominal_pain', ' altered_sensorium', ' anxiety', ' blackheads', ' blister', ' bloody_stool', ' blurred_and_distorted_vision', ' breathlessness', ' bruising', ' burning_micturition', 
             ' chest_pain', ' chills', ' cold_hands_and_feets', ' continuous_feel_of_urine', ' cough', ' dark_urine', ' dehydration', ' diarrhoea', ' dischromic _patches', ' dizziness', ' extra_marital_contacts', ' fatigue', ' foul_smell_of urine', ' headache', ' high_fever', ' hip_joint_pain', ' joint_pain', ' knee_pain', ' lethargy', ' loss_of_appetite', ' loss_of_balance', ' mood_swings', ' movement_stiffness', ' nausea', ' neck_pain', ' nodal_skin_eruptions', ' obesity', ' pain_in_anal_region', ' red_sore_around_nose', ' restlessness', ' scurring', 
             ' silver_like_dusting', ' skin_peeling', ' spinning_movements', ' stomach_pain', ' sweating', ' swelling_joints', ' swelling_of_stomach', ' ulcers_on_tongue', ' vomiting', ' watering_from_eyes', ' weakness_of_one_body_side', ' weight_loss', ' yellowish_skin', ' abdominal_pain', ' altered_sensorium', ' bloody_stool', ' blurred_and_distorted_vision', ' breathlessness', ' burning_micturition', ' chest_pain', ' continuous_feel_of_urine', ' cough', ' dark_urine', ' diarrhoea', ' dischromic _patches', ' distention_of_abdomen', ' dizziness', ' excessive_hunger', ' extra_marital_contacts', ' family_history', ' fatigue', ' headache', ' high_fever', ' hip_joint_pain', ' irregular_sugar_level', ' irritation_in_anus', ' lack_of_concentration', ' lethargy', ' loss_of_appetite', ' loss_of_balance', ' mood_swings', ' movement_stiffness', ' nausea', ' obesity', ' painful_walking', ' passage_of_gases', ' red_sore_around_nose', ' restlessness', ' scurring', ' silver_like_dusting', ' small_dents_in_nails', ' spinning_movements', ' spotting_ urination', ' sweating', ' swelling_joints', ' swelling_of_stomach', ' swollen_legs', ' vomiting', 
             ' watering_from_eyes', ' weight_loss', ' yellow_crust_ooze', ' yellowing_of_eyes', ' yellowish_skin']

# User inputs: selecting symptoms via searchable dropdown (multi-select)
st.title("Medicine Recommendation System")
st.write("Select 4 symptoms from the list below:")

# Searchable dropdown for symptoms
selected_symptoms = st.multiselect(
    'Select Symptoms', 
    symptoms,
    help="Start typing to search for symptoms"
)
# Convert selected symptoms to binary input (1 if selected, 0 if not)
binary_input = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]

# Convert binary input to numpy array (as expected by the model)
binary_input = np.array(binary_input).reshape(1, -1)

# Predict disease based on symptoms
if st.button('Predict') and len(selected_symptoms)==4: ##
    prediction = model.predict(binary_input)
    disease_id = prediction[0]

    # Disease mapping (replace with your actual mapping if necessary)
    diseasemap = {
    '(vertigo) Paroymsal  Positional Vertigo': 0, 'AIDS': 1, 'Acne': 2, 
    'Alcoholic hepatitis': 3, 'Allergy': 4, 'Arthritis': 5, 'Bronchial Asthma': 6,
    'Cervical spondylosis': 7, 'Chicken pox': 8, 'Chronic cholestasis': 9, 
    'Common Cold': 10, 'Dengue': 11, 'Diabetes': 12, 'Dimorphic hemmorhoids(piles)': 13, 
    'Drug Reaction': 14, 'Fungal infection': 15, 'GERD': 16, 'Gastroenteritis': 17, 
    'Heart attack': 18, 'Hepatitis B': 19, 'Hepatitis C': 20, 'Hepatitis D': 21, 
    'Hepatitis E': 22, 'Hypertension': 23, 'Hyperthyroidism': 24, 'Hypoglycemia': 25, 
    'Hypothyroidism': 26, 'Impetigo': 28, 'Jaundice': 29, 'Malaria': 30, 'Migraine': 31, 
    'Osteoarthristis': 32, 'Paralysis (brain hemorrhage)': 33, 'Peptic ulcer disease': 34, 
    'Pneumonia': 35, 'Psoriasis': 36, 'Tuberculosis': 37, 'Typhoid': 38, 
    'Urinary tract infection': 39, 'Varicose veins': 40, 'hepatitis A': 41
}
    
    # Map disease ID to disease name
    disease_name = next((k for k, v in diseasemap.items() if v == disease_id), "Disease not found")
    
    st.write(f"Predicted Disease: {disease_name}")

    # Fetch corresponding medicine, precautions, diet, and workout
    if disease_name in medicine['Disease'].values:
        medication = medicine.loc[medicine['Disease'] == disease_name, 'Medication'].values[0]
        st.write(f"Medication: {medication}")
        
    if disease_name in precaution['Disease'].values:
        precautions = precaution.loc[precaution['Disease'] == disease_name, ['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values[0]
        st.write(f"Precautions: {precautions[0]}, {precautions[1]}, {precautions[2]}, {precautions[3]}")
        
    if disease_name in diet['Disease'].values:
        diet_info = diet.loc[diet['Disease'] == disease_name, 'Diet'].values[0]
        st.write(f"Diet: {diet_info}")
        
    if disease_name in grouped_workout['disease'].values:
        workout_info = grouped_workout.loc[grouped_workout['disease'] == disease_name, 'workout'].values[0]
        st.write(f"Workout: {workout_info}")
