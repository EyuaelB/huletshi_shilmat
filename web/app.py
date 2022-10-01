import streamlit as st
from model_trial_page import model_try_out_page
from about_data import about_data


selected = st.sidebar.selectbox("Try or View Data", ("Try-Out", "View Data"))

if selected == 'View Data':
    about_data()
else:
    model_try_out_page()