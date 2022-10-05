import numpy as np
import streamlit as st
import tools

#with old csv format 
# def model_try_out_page():
#     st.title("የ፪ ሺህ ሓበሻ የባህል ምግብ አዳራሽ የሙዚቃ ባንድ የዕለት ሽልማት መተንበያ ድረ-ገፅ")
#     st.write("""### የሽልማት ትንበያ ቀኑን ያስገቡ""")

#     day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#     day = st.selectbox("ቀን", day)

#     clicked = st.button("ተንብይ")

#     if clicked:
#         data = tools.load_model_data('current_model_19_02_test.pkl')
#         model = tools.get_model(data)
#         le_day = tools.get_le_day(data)
        
#         input = np.array([[day.lower()]])
#         input[:, 0] = le_day.transform(input[:, 0])
        
#         input = input.astype(float)
        
#         y_pred = model.predict(input)
        
#         st.subheader(f'የሽልማት መጠን {y_pred[0]:.2f}')
  
    
def model_try_out_page():
    st.title("የ፪ ሺህ ሓበሻ የባህል ምግብ አዳራሽ የሙዚቃ ባንድ የዕለት ሽልማት መተንበያ ድረ-ገፅ")
    st.write("""### የሽልማት ትንበያ ቀኑን ያስገቡ""")

    day_opt = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    
    input_date = st.date_input("ቀን")
  
    clicked = st.button("ተንብይ")

    if clicked:
        data = tools.load_model_data('current_model_21_02_test.pkl')
        model = tools.get_model(data)
        le_day = tools.get_le_day(data)
        le_date = tools.get_le_date(data)
        le_month= tools.get_le_month(data)
        le_year = tools.get_le_year(data)

        input = np.array([[input_date.day,input_date.month,input_date.year,day_opt[input_date.weekday()].lower()]])
        
        
        print(input[:,0])
        input[:,0] = le_date.transform(input[:,0])
        print(input[:,0])
       
        input[:,1] = le_month.transform(input[:,1])
        print(input[:,1])
       
        input[:,2] = le_year.transform(input[:,2])
        print(input[:,2])
       
        input[:,3] = le_day.transform(input[:,3])
        print(input[:,3])        
        
        
        input = input.astype(float)
        
        y_pred = model.predict(input)
        
        # print(day_opt[input_date.weekday()].lower())
        
        st.subheader(f' {day_opt[input_date.weekday()]}, የሽልማት መጠን {y_pred[0]:.2f}')
    
        
        
        
        
        
        
        
