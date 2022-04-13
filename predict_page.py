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

    st.write("""### Please answer the general questions below:""")

    st.markdown("""---""")

    Sex = st.slider("Sex (1 = Male, 2 = Female)", 1, 2, 1)

    Age = st.slider("Age", 0, 100, 18)

    Health_Worker_Family = st.slider(
        "Is your family member a healthcare worker? (1 = Yes, 2 = No)", 1, 2, 1)

    Married = st.slider(
        "Are you married? (1 = Yes, 2 = No)", 1, 2, 1)

    Income = st.slider(
        "What is your annual household income (JPY)?  (1 = less than 2 million, 2 = 2-4 million, 3 = 4-6 million, 4 = 6-8 million, 5 = 8-10 million, 6 = 10-12 million, 7 = 12-15 million, 8 = 15-20 million, 9 = ≥20 million, 10 = unknown", 1, 10, 2)

    Current_Mental = st.slider(
        "Current treatment for mental problem (1 = Yes, 2 = No", 1, 2, 1)

    Past_Mental = st.slider(
        "Past treatment for mental problem (1 = Yes, 2 = No)", 1, 2, 1)

    Exercise = st.slider(
        "I exercised for my health (whether indoors or outdoors) (1 = not at all, 7 = extremely)", 1, 7, 2)

    Healthy_Diet = st.slider(
        "I took meals considering the nutrition balance (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Healthy_Sleep = st.slider(
        "I kept regular awakening time and bedtime approximately (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Activity = st.slider(
        "I engaged in activities such as hobbies with absorbing interest (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Interaction_Offline = st.slider(
        "I interacted with my family or friends on a face-to-face basis (except work or class) (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Interaction_Online = st.slider(
        "I interacted with my family or friends online using chat or video calling (except work or class) (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Preventive_Behaviors = st.slider(
        "I spontaneously refrained from going out or altruistically took preventive behaviors (e.g. wearing a mask) to prevent COVID-19 infection to my family or other people (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Optimism = st.slider(
        "I thought about the future positively (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Deterioration_Interact = st.slider(
        "A personal relationship with a close person such as family or friends got worse (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Frustration = st.slider(
        "I have become easily annoyed or irate due to life-change (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Covid_Sleepless = st.slider(
        "I could not sleep because I worried about getting COVID-19 (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    Difficulty_Work = st.slider(
        "My work or schoolwork was interrupted due to life-change (1 = Not at all and 7 = Extreme)", 1, 7, 2)

    st.write("""### Please answer the UCLA_LS3 questions below:""")

    st.markdown("""---""")

    # range = (
    #     "Never",
    #     "Rarely",
    #     "Sometimes",
    #     "Often",
    # )

    question_1 = st.slider(
        "[1] How often do you feel that you are 'in tune' with the people around you? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_2 = st.slider(
        "[2] How often do you feel that you lack companionship? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_3 = st.slider(
        "[3] How often do you feel that there is no one you can turn to? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_4 = st.slider(
        "[4] How often do you feel alone? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_5 = st.slider(
        "[5] How often do you feel part of a group of friends? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_6 = st.slider(
        "[6] How often do you feel that you have a lot in common with the people around you? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_7 = st.slider(
        "[7] How often do you feel that you are no longer close to anyone? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_8 = st.slider(
        "[8] How often do you feel that your interests and ideas are not shared by those around you? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_9 = st.slider(
        "[9] How often do you feel outgoing and friendly? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_10 = st.slider(
        "[10] How often do you feel close to people? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_11 = st.slider(
        "[11] How often do you feel left out? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_12 = st.slider(
        "[12] How often do you feel that your relationships with others are not meaningful? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_13 = st.slider(
        "[13] How often do you feel that no one really knows you well? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_14 = st.slider(
        "[14] How often do you feel isolated from others? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_15 = st.slider(
        "[15] How often do you fee1 you can find companionship when you want it? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_16 = st.slider(
        "[16] How often do you feel that there are people who really understand you? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_17 = st.slider(
        "[17] How often do you feel shy? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_18 = st.slider(
        "[18] How often do you feel that people are around you but not with you? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_19 = st.slider(
        "[19] How often do you feel that there are people you can talk to? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    question_20 = st.slider(
        "[20] How often do you feel that there are people you can turn to? (1=Never, 2=Rarely, 3=Sometimes, and 4=Often)", 1, 4, 2)

    # def range_convert(question):
    #     if question == "Never":
    #         question = 1
    #     elif question == "Rarely":
    #         question = 2
    #     elif question == "Sometimes":
    #         question = 3
    #     elif question == "Often":
    #         question = 3

    UCLA_LS3 = question_1 + question_2 + question_3 + \
        question_4 + question_5 + question_6 + question_7 + \
        question_8 + question_9 + question_10 + question_11 + \
        question_12 + question_13 + question_14 + \
        question_15 + question_16 + question_17 + \
        question_18 + question_19 + question_20

    ok = st.button("Calculate Mental State")

    if ok:
        X = np.array([[
            Sex,
            Age,
            Health_Worker_Family,
            Married,
            Income,
            Current_Mental,
            Past_Mental,
            UCLA_LS3,
            Exercise,
            Healthy_Diet,
            Healthy_Sleep,
            Activity,
            Interaction_Offline,
            Interaction_Online,
            Preventive_Behaviors,
            Optimism,
            Deterioration_Interact,
            Frustration,
            Covid_Sleepless,
            Difficulty_Work
        ]])

        state = regressor_loaded.predict(X)
        if state[0] == 0:
            st.subheader("Not Depressed.")
        elif state[0] == 1:
            st.subheader("Depressed!")
