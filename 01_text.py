import streamlit as st

st.title('Text elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library')
st.header('Header 연습')
st.subheader('Subheader 연습')
st.text('text 연습')

st.markdown("# This is a Markdown title")
st.markdown("## This is a Markdown title")
st.markdown("This is **the markdown 진하게**")
st.markdown("This is _the Markdown 기울임_")
st.markdown("This is *the Markdown 기울임*")
st.markdown("This is ***the Markdown 진하고 기울임***")

st.markdown('- item')
st.markdown('1. item')

st.code('x=1234')
st.write('\n')
st.write('\n')
st.write('Hello, *World!* :sunglasses:')