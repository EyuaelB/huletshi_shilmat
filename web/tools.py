import pickle


def load_model_data(pkl_path):
    with open(pkl_path, 'rb') as file:
        data = pickle.load(file)
    return data


def get_model(data):
    return data['model']


def get_le_day(data):
    return data['le_day']


def get_le_date(data):
    return data['le_date']


def get_le_month(data):
    return data['le_month']

def get_le_year(data):
    return data['le_year']