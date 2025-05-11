import streamlit as st
import openai

st.title("🤖 AI Chatbot")

openai.api_key = st.secrets["OPENAI_API_KEY"]

prompt = st.text_input("You:")

if prompt:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write("Bot:", response["choices"][0]["message"]["content"])
