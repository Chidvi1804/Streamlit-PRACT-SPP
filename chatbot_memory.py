import streamlit as st

st.title("🧠 Rule-Based Chatbot with Memory")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input from user
user_input = st.text_input("You: ", key="user_input")

# Rule-based response generator
def get_bot_response(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I help you?"
    elif "your name" in message:
        return "I'm a chatbot built with Streamlit!"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

# When user enters a message
if user_input:
    # Append user message
    st.session_state.chat_history.append(("You", user_input))
    
    # Generate bot response
    bot_response = get_bot_response(user_input)
    st.session_state.chat_history.append(("Bot", bot_response))
    
    # Clear the input box
    st.experimental_rerun()

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧍‍♀️ You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")
