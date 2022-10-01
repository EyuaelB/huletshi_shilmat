import numpy as np
import streamlit as st
import pickle


def load_model(pkl_path):
    with open(pkl_path, 'rb') as file:
        data = pickle.load(file)
    return data


def model_try_out_page():
    st.title("የ፪ ሺህ ሓበሻ የባህል ምግብ አዳራሽ የሙዚቃ ባንድ ሽልማት መትንበያ ድረ-ገፅ")
    st.write("""### የሽልማት ትንበያ ቀኑን ያስገቡ""")

    day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    day = st.selectbox("ቀን", day)

    clicked = st.button("ተንብይ")

    if clicked:
        pass
