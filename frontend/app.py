
import streamlit as st
from services.api_client import send_article_request

st.set_page_config(page_title="AI Article Processor (Groq)")

st.title("AI Article Processor - Groq Powered")

if st.session_state.get("submit_success"):
    st.success("Request accepted. Processing has started in n8n.")
    st.info("Email and Google Sheets update happen after workflow completion.")
    st.write("Session ID:", st.session_state.get("last_session_id"))
    st.session_state.submit_success = False

with st.form("article_form", clear_on_submit=True):
    email = st.text_input("Enter your email")
    article_url = st.text_input("Enter article URL")
    submitted = st.form_submit_button("Submit")

if submitted:
    if email and article_url:
        response = send_article_request(email, article_url)

        if response.get("status") == "sent":
            st.session_state.last_session_id = response.get("session_id")
            st.session_state.submit_success = True
            st.rerun()
        else:
            st.error(response.get("message", "Error occurred."))
    else:
        st.warning("Please complete all fields.")
