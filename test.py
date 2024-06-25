import streamlit as st

import plotly.express as px

st.title("Hello Streamlit!")
st.write("Welcome to Streamlit using Pipenv.")

year = st.slider('연도를 선택', 2000, 2020)
hobby = st.selectbox('다음 중 취미 선택', ('독서', '걷기'))
st.write(f'당신은 연도 {year}와 취미 {hobby}를 선택했음.')

import pandas as pd
import numpy as np

# 데이터 생성 (20행 3열의 난수. 표준정규분포에서 추출한)
data1 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# 선 그래프 출력
st.line_chart(data1)

dates = pd.date_range(start='2023-01-01', periods=10)

# 데이터 생성
data2 = pd.DataFrame(
    np.random.randn(10, 3),
    index=dates,
    columns=['Temperature', 'Humidity', 'Wind Speed']
)

# 막대 그래프 출력
st.bar_chart(data2)

st.area_chart(data1)



df = pd.DataFrame({
    'x': range(1, 101),
    'y': np.random.randn(100).cumsum()
})

# 그래프 생성
fig = px.line(df, x='x', y='y', title='Random Walk')

# 그래프 출력
st.write("plotly")
st.plotly_chart(fig)



data = pd.DataFrame({
    'x': np.arange(100),
    'y': np.random.randn(100).cumsum()
})

# 그래프 생성
chart = st.Chart(data).mark_line().encode(
    x='x',
    y='y'
).properties(
    title='Random Walk'
)

# 그래프 출력
st.altair_chart(chart, use_container_width=True)