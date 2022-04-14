import streamlit as st
from dev_page import show_dev_page
from logistic_regression_predict import show_logistic_regression_predict
from knn_predict import show_knn_predict
from naive_bayes_predict import show_naive_bayes_predict

page = st.sidebar.selectbox(
    "Select Page:", ("Developers", "Predict (Logistic Regression)", "Predict (KNN)", "Predict (Naive Bayes)"))

if page == "Developers":
    show_dev_page()
elif page == "Predict (Logistic Regression)":
    show_logistic_regression_predict()
elif page == "Predict (KNN)":
    show_knn_predict()
elif page == "Predict (Naive Bayes)":
    show_naive_bayes_predict()
