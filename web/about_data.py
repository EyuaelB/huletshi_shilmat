import pandas as pd
# from matplotlib import pyplot as plt
import streamlit as st


def data_for_bar_chart(df):
    data = df.groupby(['Day'])['Income'].mean().sort_values(ascending=True)
    return data

# def scatter_plot(df,x_data,y_data):
#     plt.scatter(df[x_data].values,df[y_data].values,c="red")
#     # plt.scatter(df['DayName'].values,df[y_value].values,c="red"



def about_data():
    st.title("መዝገቡን በ እይታ ይረዱ")
 
    
    df = pd.read_csv('shilmat_data2.csv')
    st.bar_chart(data_for_bar_chart(df))
    
    
    
    
    # plt.scatter(df['DayName'].values,df['Income'].values,c="red")
    # plt.title("Day  - Income Graph")
    # plt.show()
    
    
    # plt.scatter(df['DayOfTheMonth'].values,y.values,c="red")
    # plt.title("Day of the month - Income Graph")
    # plt.show()
    # df['Date'] = pd.to_datetime(df.Date)
    
    # df['DayOfTheMonth'] = df.Date.dt.day
    
    
   
    # st.plotly_chart(df['DayOfTheMonth'].values,df['Income'].values,c="red")
    
    
    

