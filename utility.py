import streamlit as st  
import hmac  
import tiktoken

# TODO error still showing on tap out of username field
def check_credentials():
    def credentials_entered():
        correct_username = st.secrets["username"]
        correct_password = st.secrets["password"]

        entered_username = st.session_state.get("username", "")
        entered_password = st.session_state.get("password", "")

        username_match = hmac.compare_digest(entered_username, correct_username)
        password_match = hmac.compare_digest(entered_password, correct_password)

        if username_match and password_match:
            st.session_state["credentials_correct"] = True
            del st.session_state["username"]
            del st.session_state["password"]
            # Reset submit flags
            st.session_state["username_submitted"] = False
            st.session_state["password_submitted"] = False
        else:
            st.session_state["credentials_correct"] = False

    # Initialize submit flags if not present
    if "username_submitted" not in st.session_state:
        st.session_state["username_submitted"] = False
    if "password_submitted" not in st.session_state:
        st.session_state["password_submitted"] = False

    if st.session_state.get("credentials_correct", False):
        return True

    # Username input with on_change
    def on_username_change():
        st.session_state["username_submitted"] = True
        credentials_entered()

    # Password input with on_change
    def on_password_change():
        st.session_state["password_submitted"] = True
        credentials_entered()

    st.text_input("Username", key="username", on_change=on_username_change)
    st.text_input("Password", type="password", key="password", on_change=on_password_change)

    # Show error only if user has pressed Enter in username or password at least once
    if (
        ("credentials_correct" in st.session_state and not st.session_state["credentials_correct"])
        and (st.session_state["username_submitted"] or st.session_state["password_submitted"])
    ):
        st.error("😕 Username or password incorrect")

    return False

def count_tokens(text):
    encoding = tiktoken.encoding_for_model('gpt-4o-mini')
    return len(encoding.encode(text))
