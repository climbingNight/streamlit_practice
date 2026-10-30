import streamlit as st
import time

st.title('Media elements')

st.caption('meda 참고사이트: https://docs.streamlit.io/library/api-reference/media')

st.header("Media elements")
if st.button("랜덤이미지"):
    random_url = f'https://picsum.photos/250/250?random={time.time()}'
    st.image(random_url)

st.header('2.Audio')
st.audio('./data/MusicSample.mp3')

st.header('3.Video')
st.video('./data/VideoSample.mp4')