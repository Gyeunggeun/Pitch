import streamlit as st
import validators, base64
from pathlib import Path

def add_logo(logo_url: str, height: int = 120):
    if validators.url(logo_url) is True:
        logo = f"url({logo_url})"
    else:
        logo = f"url(data:image/png;base64,{base64.b64encode(Path(logo_url).read_bytes()).decode()})"

    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: {logo};
                background-repeat: no-repeat;
                padding-top: {height - 100}px;
                background-position: -100px -150px;
        </style>
        """,
        unsafe_allow_html=True,
    )