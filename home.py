import streamlit as st

st.set_page_config(
        page_title="WhatsApp Zip Import",
        page_icon="📈",
)
st.title("Get Started with your WhatsApp import!")

st.divider()


st.page_link("pages/import.py", label="Click this button to start the import", icon="📁")

st.divider()

st.write("Code by: [JocelynVelarde](https://github.com/JocelynVelarde)")