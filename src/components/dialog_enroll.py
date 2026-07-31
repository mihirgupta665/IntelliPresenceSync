import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from src.database.db import execute_with_retries
import time

@st.dialog("Enroll in Subject")
def enroll_dialog():
    st.write("Enter the subject code provided by your teacher to enroll")
    join_code = st.text_input("Subject Code", placeholder="Eg. CSE101")

    if st.button("Enroll Now", type="primary", width="stretch"):
        if join_code:
            res = execute_with_retries(supabase.table("subjects").select("subject_id, name, subject_code").eq("subject_code", join_code))
            if res.data:
                subject  = res.data[0]  
                student_id = st.session_state.student_data["student_id"]
                student_name = st.session_state.student_data["name"]

                check = execute_with_retries(supabase.table("subject_students").select("*").eq("subject_id", subject["subject_id"]).eq("student_id", student_id))
                if check.data:
                    st.warning(f"{student_name} is already enrolled in subject {subject["name"]}")
                else:
                    enroll_student_to_subject(student_id, subject["subject_id"])
                    st.success(f"{student_name} is successfully enrolled in subject {subject["name"]}")
                    time.sleep(1)
                    st.rerun()

        else:
            st.warning("Please enter a subject code") 