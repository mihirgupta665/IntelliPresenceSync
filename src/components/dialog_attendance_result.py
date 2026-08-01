import streamlit as st
import time 

from src.database.db import create_attendance


@st.dialog("Attendance Reports")
def attendance_result_dialog(df, logs):
    st.write("Please review the attendance before confirming.")

    st.dataframe(df, hide_index=True, width="stretch")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Discard", width="stretch", type="tertiary"):
            st.rerun()

    with col2:
        if st.button("Confirm and Approve", width="stretch", type="primary"):
            try:
                create_attendance(logs)
                st.success("Attendance Approved Successfully")
                st.session_state.attendance_images = []
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error("Error occured while marking the Attendance")
