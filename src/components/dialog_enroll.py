import streamlit as st
from src.database.db import create_subject

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to enroll")
    join_code = st.text_input("Subject Code", placeholder="Eg. CSE101")

    if st.button("Enroll Now", type="primary", width="stretch"):
        if join_code:
            

        else:
            st.warning("Please enter a subject code")