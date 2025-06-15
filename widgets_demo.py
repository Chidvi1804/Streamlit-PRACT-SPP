import streamlit as st
st.title("Basic Widget App")
name=st.text_input("What's your name?")
age=st.number_input("What's your age?",0,100)
hobby=st.selectbox("What's your hobby",['Drawing','Cricket','Book'])
agree=st.checkbox("i agree to terms and conditions")

if st.button("Submit"):
    st.write(f'Hello,{name}, You are {age} years old and love doing {hobby}')
    if agree:
        st.success("Terms accepted")
    else:
        st.error("Please accept")