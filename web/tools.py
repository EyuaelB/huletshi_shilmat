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



# def feature_day_name(day_name:str,day_opt:tuple)->int:
#     for i in range(0,7):
#         if day_opt[i] ==  day_name:
#             return i


def feature_day_of_week (day_name:str,day_opt:tuple)->int:
    for i in range(0,7):
        if day_name == day_opt[i]:
            return i    
    
        
def feature_day_of_month (day_of_month:str,month_opt:tuple)->int:
    for i in range(1,31):
        if  month_opt[i] == day_of_month:
            return i+1    
    