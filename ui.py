import streamlit as st

def render_header():
    st.markdown('<div class="title">🎭 AI Sentiment Analyzer</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Understand emotions in text instantly using Machine Learning</div>', unsafe_allow_html=True)

def render_sidebar():
    st.sidebar.title("📌 About Project")
    st.sidebar.write("""
    - Uses TF-IDF Vectorization
    - Trained with Logistic Regression
    - Built using Streamlit
    - Real-time predictions
    """)
    st.sidebar.write("Developed by Anokhi Mantri")
