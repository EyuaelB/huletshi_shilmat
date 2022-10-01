import pickle
import  streamlit as st


def load_model_data(pkl_path):
    with open(pkl_path, 'rb') as file:
        data = pickle.load(file)
    return data


def get_model(data):
    return data['model']


def get_le_day(data):
    return data['le_day']