import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from src.database.db import execute_with_retries
import time

@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data["student_id"]


    res = execute_with_retries(supabase.table("subjects").select("subject_id", "name").eq("subject_code", subject_code))
    if not res.data:
        st.error(f"Subject {subject_code} not found!")
        if st.button("Close"):
            st.query_params.clear()
            st.rerun()
        return

    subject = res.data[0]
