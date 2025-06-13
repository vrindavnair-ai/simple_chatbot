import streamlit as st
import google.generativeai as genai

# Set up Gemini API
genai.configure(api_key="AIzaSyDTuP9mQuLaEUE7Y3A76ig-k4Ta-wTStWg")  # Replace with your key

# Create the model and chat session
model = genai.GenerativeModel("gemini-1.5-flash")

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.title("💬 Gemini Chatbot")
st.markdown("Talk to Gemini using Google's AI model!")

# Chat history
for msg in st.session_state.chat.history:
    with st.chat_message(msg.role):
        st.markdown(msg.parts[0].text)

# User input
prompt = st.chat_input("Say something...")
if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    response = st.session_state.chat.send_message(prompt)

    with st.chat_message("model"):
        st.markdown(response.text)