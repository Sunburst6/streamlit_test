import streamlit as st

st.title('title')
st.success('This is a success message!')
if st.button('Say hello'):
    st.write('clicked!')
else:
    st.write('not clicked!')