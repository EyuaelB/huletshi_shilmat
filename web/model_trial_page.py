import numpy as np
import streamlit as st
import tools


# def model_try_out_page():
#     st.title("የ፪ ሺህ ሓበሻ የባህል ምግብ አዳራሽ የሙዚቃ ባንድ የዕለት ሽልማት መተንበያ ድረ-ገፅ")
#     st.write("""### የሽልማት ትንበያ ቀኑን ያስገቡ""")

    # day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    # day = st.selectbox("ቀን", day)
    # day_of_month = 
    # year = 

    # clicked = st.button("ተንብይ")
    
#with old csv format 
#     if clicked:
#         data = tools.load_model_data('current_model_19_02_test.pkl')
#         model = tools.get_model(data)
#         le_day = tools.get_le_day(data)
        
#         input = np.array([[day.lower()]])
#         input[:, 0] = le_day.transform(input[:, 0])
        
#         input = input.astype(float)
        
#         y_pred = model.predict(input)
        
#         st.subheader(f'የሽልማት መጠን {y_pred[0]:.2f}')
  
   

#with new csv format
    # if clicked:
    #     data = tools.load_model_data('xgmodel27.pkl')
    #     model = tools.get_model(data)
    #     le_day = tools.get_le_day(data)
        
        
    #     #input array
    #     np.array([[]])
        
        
        
    #     input = np.array([[day.lower()]])
    #     input[:, 0] = le_day.transform(input[:, 0])
        
    #     input = input.astype(float)
        
    #     y_pred = model.predict(input)
        
    #     st.subheader(f'የሽልማት መጠን {y_pred[0]:.2f}')



    
def model_try_out_page():
    st.title("የ፪ ሺህ ሓበሻ የባህል ምግብ አዳራሽ የሙዚቃ ባንድ የዕለት ሽልማት መተንበያ ድረ-ገፅ")
    st.write("""### የሽልማት ትንበያ ቀኑን ያስገቡ""")
    
    
    # First Input
    day_opt = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    day = st.selectbox("ዕለት/Day Of The Week", day_opt)

    
    # Second input
    input_day_of_month = st.slider('የወሩ ቀን/Day Of The Month',1,30,1)
    
    
    # Third input
    month_opt = ("Jan", "Feb", "March", "April", "May", "June", "July","Aug","Sep","Oct","Nov","Dec")
    month = st.selectbox("ቀን/Day Of The Month", month_opt)
    
    
    # Last Input
    # input_year = st.slider('ዓ.ዓ/Year',2022,2025,2022)
    
    
    # input_date = st.date_input("ቀን")
  
    clicked = st.button("ተንብይ")
    if clicked:
        data = tools.load_model_data('ext_model32.pkl')
        model = tools.get_model(data)
        
        
        # input format -  DayName,DayOfTheWeek,DayOfTheMonth,Month,Year
        input = np.array([[tools.feature_day_of_week(day,day_opt),
                           input_day_of_month,
                           tools.feature_day_of_month(month,month_opt)]])
              
        y_pred = model.predict(input)
        
        st.subheader(f'የሽልማት መጠን/Predicted Income for {month},{day},{input_day_of_month} :  {y_pred[0]:.2f}')

   
        
        
        
        
        
        
        
        
