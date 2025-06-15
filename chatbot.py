import streamlit as st

st.header("simple chatbot")

st.subheader("enter prompt")

user_input=st.text_input("you:"," ")

def respond(input_text):
    input_text=input_text.lower()
    if "hello" in input_text:
        return "Hello,how may i assist you?"
    elif "your name" in input_text:
        return "I'm your simple bot"
    elif "bye" in input_text:
        return "Bye bye"
    else:
        return "sorry i didnt understand"

if user_input:
    response=respond(user_input)
    st.write("Bot:",response)