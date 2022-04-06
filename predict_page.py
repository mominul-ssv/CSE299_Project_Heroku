import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

regressor_loaded = data["model"]


def show_predict_page():
    st.title("Depression Prediction")

    st.write("""### Please answer the questions below:""")

    Residence = st.slider(
        "Residence (1 = Tokyo, 2 = Kanagawa, 3 = Saitama, 4 = Chiba, 5 = Osaka, 6 = Hyogo, 7 = Fukuoka)", 1, 7, 1)

    Sex = st.slider("Sex (1 = Male, 2 = Female)", 1, 2, 1)

    Age = st.slider("Age", 0, 100, 18)

    Age_Group = st.slider(
        "Age Group (Pick '4' for 18-19 years, '3' for 20-39 years, '2' for 40-64 years, '1' for greater than 65 years)", 1, 4, 1)

    Job_Group = st.slider(
        "Employment Status (1 = Employed, 2 = Home Maker, 3 = Student, 4 = Unemployed, 5 = Others)", 1, 5, 1)

    Health_Worker_Self = st.slider(
        "Are you a healthcare worker? (1 = Yes, 2 = No)", 1, 2, 1)

    Health_Worker_Family = st.slider(
        "Is your family member a healthcare worker? (1 = Yes, 2 = No)", 1, 2, 1)

    Married = st.slider(
        "Are you married? (1 = Yes, 2 = No)", 1, 2, 1)

    Income = st.slider(
        "What is your annual household income (JPY)?  (1 = less than 2 million, 2 = 2-4 million, 3 = 4-6 million, 4 = 6-8 million, 5 = 8-10 million, 6 = 10-12 million, 7 = 12-15 million, 8 = 15-20 million, 9 = ≥20 million, 10 = unknown", 1, 10, 1)

    Current_Physical = st.slider(
        "Are you currently under any treatment for severe physical illness? (1 = Yes, 2 = No)", 1, 2, 1)

    Past_Physical = st.slider(
        "Have you done gone through any past treatment for severe physical illness? (1 = Yes, 2 = No)", 1, 2, 1)

    Current_Mental = st.slider(
        "Current treatment for mental problem (1 = Yes, 2 = No", 1, 2, 1)

    Past_Mental = st.slider(
        "Past treatment for mental problem (1 = Yes, 2 = No)", 1, 2, 1)

    K6 = 10
    PHQ9 = 6
    UCLA_LS3 = 25
    LSNS6 = 15

    Exercise = st.slider(
        "I exercised for my health (whether indoors or outdoors) (1 = not at all, 7 = extremely)", 1, 7, 1)

    Healthy_Diet = st.slider(
        "I took meals considering the nutrition balance (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Healthy_Sleep = st.slider(
        "I kept regular awakening time and bedtime approximately (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Activity = st.slider(
        "I engaged in activities such as hobbies with absorbing interest (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Interaction_Offline = st.slider(
        "I interacted with my family or friends on a face-to-face basis (except work or class) (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Interaction_Online = st.slider(
        "I interacted with my family or friends online using chat or video calling (except work or class) (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Preventive_Behaviors = st.slider(
        "I spontaneously refrained from going out or altruistically took preventive behaviors (e.g. wearing a mask) to prevent COVID-19 infection to my family or other people (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Optimism = st.slider(
        "I thought about the future positively (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Deterioration_Economy = st.slider(
        "The family budget has tightened (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Deterioration_Interact = st.slider(
        "A personal relationship with a close person such as family or friends got worse (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Frustration = st.slider(
        "I have become easily annoyed or irate due to life-change (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Covid_Anxiety = st.slider(
        "I felt nervous or anxious when I watched news about COVID-19 (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Covid_Sleepless = st.slider(
        "I could not sleep because I worried about getting COVID-19 (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Difficulty_Living = st.slider(
        "My daily life was interrupted due to the shortage of materials relating to prevention for COVID-19 infection (e.g. mask or thermometer) or other daily supplies (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    Difficulty_Work = st.slider(
        "My work or schoolwork was interrupted due to life-change (1 = Not at all and 7 = Extreme)", 1, 7, 1)

    # backend calculation
    # K6 score = [use any input type]
    # PHQ9 score = [use any input type]
    # UCLA_LS3 = [use any input type]

    ok = st.button("Calculate Mental State")

    if ok:
        X = np.array([[
            Residence,
            Sex,
            Age,
            Age_Group,
            Job_Group,
            Health_Worker_Self,
            Health_Worker_Family,
            Married,
            Income,
            Current_Physical,
            Past_Physical,
            Current_Mental,
            Past_Mental,
            K6,
            PHQ9,
            UCLA_LS3,
            LSNS6,
            Exercise,
            Healthy_Diet,
            Healthy_Sleep,
            Activity,
            Interaction_Offline,
            Interaction_Online,
            Preventive_Behaviors,
            Optimism,
            Deterioration_Economy,
            Deterioration_Interact,
            Frustration,
            Covid_Anxiety,
            Covid_Sleepless,
            Difficulty_Living,
            Difficulty_Work
        ]])

        state = regressor_loaded.predict(X)
        st.subheader(f"Mental State: {state[0]}")
