from dotenv import load_dotenv
import streamlit as st

from rag import rag
from utility import check_credentials

# TODO how to not make text field on focus red?

# Configuration
st.set_page_config(
    layout="centered",
    page_title="PR Transition Assistant"
)

# Credentials check  
if st.secrets['password_check'] == "True" and not check_credentials():  # TODO how to check bool instead of string?
    st.stop()

# Main app
st.title("PR Transition Assistant")

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = rag(user_prompt)
    st.write(response)
    print(f"User Input is {user_prompt}")

# Disclaimer
with st.expander("**Disclaimer**"):
    st.write(
        """
        **IMPORTANT NOTICE:** This web application is a prototype developed for **educational purposes only**. The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
        **Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**
        Always consult with qualified professionals for accurate and personalized advice.
        """
    )
