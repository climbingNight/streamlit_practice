import streamlit as st
from datetime import datetime
import pandas as pd

st.title('Input Widgets')
st.caption('Input 참고사이트: https://docs.streamlit.io/library/api-reference/widgets')

# 1. Button
st.header('1.Button')

if st.button('노크하기'):
    st.write('여기 사람 있어요.')

if st.button('Say Hello'):
    st.write("hello")
else:
    st.write("goodbye")

# 2. Radio Button
st.header('2.Radio Button')
genre = st.radio('좋아하는 영화 장르는?', {'액션', '느와르', 'SF', '로맨스'})

if genre == 'SF':
    st.write('인터스텔라')
elif genre == '액션':
    st.write('테이큰')
elif genre == '로맨스':
    st.write('말할 수 없는 비밀')
elif genre == '느와르':
    st.write('신세계')

# 3. Checkbox
st.header('3.Checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write(':cat:'*10)

# 4. Select box(단일 선택)
st.header('4.Select box')
option = st.selectbox("어떻게 연락드릴까요?", ('Email', 'Mobile', 'Office phone'))
st.write('네', option, ' (으)로 연락 드리겠습니다.')

# 5. Multi select (다중 선택)
st.header('5.Multi select')
options = st.multiselect(
    '좋아하는 색은?',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)
st.write('당신의 선호 색상은 :')
for i in options:
    st.write(i)

# 6. Input: Text / Number
st.header('6.Input: Text/Number')

st.subheader('***text_input***')
title = st.text_input('가장 좋아하는 영화는?', 'Sound of Music')
st.write('당신의 최애 영화는:', title)

# 8. Slider
st.header('8.Slider')

# 숫자 슬라이더 (단일 값)
st.subheader('**_Slider-이전 구간_**')
age = st.slider('나이가 어떻게 되세요?', 0, 130, 25)
st.write('I am ', age, 'years old')

# 숫자 구간 슬라이더 (최소~최대)
st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간을 선택하세요', 0.0, 100.0, (25.0, 75.0))
st.write('values:', values)

# 날짜 구간 슬라이더
st.subheader('**_년 월 일 사이 구간_**')
slider_date = st.slider(

    '날짜 구간을 선택하세요.',
    min_value = datetime(2024,1,1),
    max_value = datetime(2024,12,31),
    value = (datetime(2024,6,1), datetime(2024,7,31)),
    format = 'YY/MM/DD'
)
st.write('slider date:', slider_date)
st.write('slider_date[0]:', slider_date[0], 'slider_date[1]:', slider_date[1])

# 날짜 구간으로 데이터 조회하기
st.header('날짜 구간으로 데이터 조회하기')

# CSV 데이터 불러오기
df = pd.read_csv('./data/data_subway_in_seoul.csv', encoding='cp949')
st.write('날짜 필드 형식:', df['날짜'].dtypes)
st.write(df)