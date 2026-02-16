import streamlit as st
from model_utils import predict_sentiment
from ui import render_header, render_sidebar
import time


# Page config
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🎭", layout="centered")

# Load CSS
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Render UI
render_header()
render_sidebar()

st.markdown('<div class="main-card">', unsafe_allow_html=True)

with st.form("sentiment_form"):
    user_input = st.text_area("✍ Enter your text:", height=150)
    submitted = st.form_submit_button("🚀 Analyze Sentiment")

    if submitted:
        if user_input.strip():
            with st.spinner("🔍 Analyzing sentiment..."):
                time.sleep(1)

                # Directly use user input (no translation)
                prediction, probability = predict_sentiment(user_input)

                confidence = max(probability) * 100
                difference = abs(probability[0] - probability[1])

            st.markdown("---")

            if difference < 0.10:
                st.warning("⚠ Sentiment is unclear or neutral. Please enter more specific text.")
            else:
                if prediction == 1:
                    st.success("😊 Positive Sentiment Detected!")
                else:
                    st.error("😡 Negative Sentiment Detected!")

                st.metric("Confidence Score", f"{confidence:.2f}%")
                st.progress(int(confidence))

        else:
            st.warning("Please enter some text.")


st.markdown('</div>', unsafe_allow_html=True)
