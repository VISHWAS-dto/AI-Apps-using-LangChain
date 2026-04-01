from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name",["Attention Is All You Need",
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox(
    "Select Explanation Style",["Beginner-Friendly","Technical","Code-Oriented","Mathematical"])

length_input = st.selectbox(
    "Select Explanation Length",["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)","Long (detailed explanation)"])

if st.button('Submit'):
    result = ChatGroq(model = "llama-3.3-70b-versatile" , temperature = 0)
    result = result.invoke(f"{paper_input} ({style_input}) ({length_input})")
    st.text(result.content)
