import streamlit as st
from chatbot.chatbot_core import get_bot_response

st.set_page_config(page_title="Chatbot", layout="centered")
st.title("Chatbot ")

st.markdown("Built with **spaCy** and **Streamlit** ")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = get_bot_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))
        st.rerun()

# Display chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {msg}")
