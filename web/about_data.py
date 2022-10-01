import pandas as pd
# from matplotlib import pyplot as plt
import streamlit as st


def data_for_bar_chart(df):
    data = df.groupby(['day'])['income'].mean().sort_values(ascending=True)
    return data


def about_data():
    st.title("መዝገቡን በ እይታ ይረዱ")
 
    
    df = pd.read_csv('shilmat_data.csv')
    st.bar_chart(data_for_bar_chart(df))

