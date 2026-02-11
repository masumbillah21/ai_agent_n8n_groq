
import streamlit as st
from services.api_client import send_article_request

st.set_page_config(page_title="AI Article Processor (Groq)")

st.title("AI Article Processor - Groq Powered")

email = st.text_input("Enter your email")
article_url = st.text_input("Enter article URL")

if st.button("Submit"):
    if email and article_url:
        response = send_article_request(email, article_url)

        if response.get("status") == "sent":
            st.success("Processing started! Check your email.")
            st.write("Session ID:", response.get("session_id"))
        else:
            st.error("Error occurred.")
    else:
        st.warning("Please complete all fields.")
