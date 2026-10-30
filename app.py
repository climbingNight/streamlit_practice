import streamlit as st

st.title('Hello world!')

st.write(1234)

st.write(':red[streamlit] is :blue-background[best] :sunglasses:')

if st.button(':sunglasses:'):
    st.write('여기 사람 있어요!!!')

st.write("동의하시면 아래 내용에 체크해 주세요.")
agree = st.checkbox('동의? 어 보감')

if agree:
    st.write(':blue-background[ㅇㅈ? ㅇ ㅇㅈ]')
else:
    st.write(':red[위에 체크 해보삼]')

option = st.selectbox(
    ":red[연락 어캐 받을랭?]",
    ('이멜', '유선', '문자')
)
st.write(':yellow[선택한 방식:]', option)

age = st.slider('몇살이가?', 0, 130, 55)
st.write("저는 ", age, "살 입니다!")

text1 = st.text_input("이름을 입력하세요.")
text2 = st.text_area("자기소개 해주세요.")
st.write("이름 입력값: " + text1)
st.write("자기소개 입력값: " + text2)