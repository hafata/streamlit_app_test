import streamlit as st

btn1 = st.button('클릭')


if 'count' not in st.session_state:
    st.session_state.count  = 0

if btn1:
    st.session_state.count += 1
    st.write("버튼눌림",st.session_state.count)

import requests
import pandas as pd

btn2 = st.button('데이터가져오기')
url = "https://script.google.com/macros/s/AKfycbz9VeOcr4zMFcx8dt81X8y9bD_1YSKUgNgiSsRfPC7-zaJJou_zz6sfmyOqa6b-1m9xvQ/exec?mode=read"

if btn2:
    response = requests.get(url, timeout=5000)
    #st.write(response.json())
    df = pd.DataFrame(response.json())
    st.write(df)

    # st.line_chart(df, x='timestamp',y=['temp','temp'])
    # st.line_chart(df)
    led_state = df.sort_values('timestamp').iloc[-1]["led"]
    st.write(f"현재 버튼 상태 : {led_state}")
