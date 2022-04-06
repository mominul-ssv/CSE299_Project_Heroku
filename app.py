import streamlit as st
from predict_page import show_predict_page
from dev_page import show_dev_page


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Developers"))

if page == "Predict":
    show_predict_page()
else:
    show_dev_page()
