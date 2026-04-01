from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header('My App')

user_input = st.text_input('Enter your text')

if st.button("Submit"):
    result = ChatGroq(model = "llama-3.3-70b-versatile" , temperature = 0).invoke(user_input)
    st.text(result.content)


