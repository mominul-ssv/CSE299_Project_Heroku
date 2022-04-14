import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('knn.pkl', 'rb') as file:
        data = pickle.load(file)
    return data


data = load_model()

knn_loaded = data["model"]


def show_knn_predict():
    st.title("Lonliness Prediction")

    st.write("""### (KNN)""")

    st.write("""### Please answer the general questions below:""")

    st.markdown("""---""")

    Sex = st.slider("Sex (1 = Male, 2 = Female)", 1, 2, 1)

    Married = st.slider(
        "Are you married? (1 = Yes, 2 = No)", 1, 2, 1)

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

    ok = st.button("Calculate Mental State")

    if ok:
        X = np.array([[
            Sex,
            Married,
            Exercise,
            Healthy_Diet,
            Healthy_Sleep,
            Activity,
            Interaction_Offline,
            Interaction_Online,
            Preventive_Behaviors,
            Optimism,
            Deterioration_Interact,
        ]])

        state = knn_loaded.predict(X)
        if state[0] == 0:
            st.subheader("Lonely.")
        elif state[0] == 1:
            st.subheader("Not Lonely!")
