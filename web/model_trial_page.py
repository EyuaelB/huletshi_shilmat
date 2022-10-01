import numpy as np
import streamlit as st
import tools


def model_try_out_page():
    st.title("የ፪ ሺህ ሓበሻ የባህል ምግብ አዳራሽ የሙዚቃ ባንድ የዕለት ሽልማት መተንበያ ድረ-ገፅ")
    st.write("""### የሽልማት ትንበያ ቀኑን ያስገቡ""")

    day = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    day = st.selectbox("ቀን", day)

    clicked = st.button("ተንብይ")

    if clicked:
        data = tools.load_model_data('current_model_19_02_test.pkl')
        model = tools.get_model(data)
        le_day = tools.get_le_day(data)
        
        input = np.array([[day.lower()]])
        input[:, 0] = le_day.transform(input[:, 0])
        
        input = input.astype(float)
        
        y_pred = model.predict(input)
        
        st.subheader(f'የሽልማት መጠን {y_pred[0]:.2f}')
        
    
        
        
        
        
        
        
        
        
