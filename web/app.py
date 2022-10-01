import streamlit as st
from model_trial_page import model_try_out_page

st.sidebar.selectbox("Try or View Data", ("Try-Out", "View Data"))

model_try_out_page()