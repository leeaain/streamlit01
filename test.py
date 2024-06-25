import streamlit as st
# 추가 해봄

st.title("Hello Streamlit!")
st.write("Welcome to Streamlit using Pipenv.")

year = st.slider('연도를 선택', 2000, 2020)
hobby = st.selectbox('다음 중 취미 선택', ('독서', '걷기'))
st.write(f'당신은 연도 {year}와 취미 {hobby}를 선택했음.')

import pandas as pd
import numpy as np

# 데이터 생성
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# 선 그래프 출력
st.line_chart(data)

print(data)