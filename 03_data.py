import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Display elements')
st.caption('data 참고사이트: https://docs.streamlit.io/library/api-reference/data')

st.header('1.Metric')
st.metric(label="Temperature", value="70 F", delta="1.2 F")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 F", "1.2 F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.metric(label="Gas price", value=4, delta=0.5, delta_color="inverse")

st.metric(
    label="Active developers", value=123, delta=123, delta_color="off"
)
a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30F", "-9F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)


st.header('Dataframe 조회하기')
titanic = pd.read_csv('./data/t2.csv')
st.dataframe(titanic.head(10))

df = pd.DataFrame(np.random.randn(10, 20), columns=('col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))