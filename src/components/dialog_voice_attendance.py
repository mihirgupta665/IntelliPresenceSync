import streamlit as st
import pandas as pd

import time
from datetime import datetime

from src.pipelines.voice_pipeline import process_bulk_audio

from src.database.config import supabase
from src.database.db import execute_with_retries

from src.components.dialog_attendance_result import show_attendance_result

@st.dialog("Voice Attendance")
def voice_attendance_dialog(selected_subject_id):
    st.write("Record the 'I am Present' voices of all students. This entire audio will be analyzed by AI to recogonize the student for attendance purpose.")

    audio_data = None

    audio_data = st.audio_input("Record Classroom Audio")

    if st.button("Analyze Audio", width="stretch", type="primary"):
        with st.spinner("Processing Audio Data"):
            enrolled_res = execute_with_retries(supabase.table("subject_students").select("*, students(*)").eq("subject_id", selected_subject_id))
            enrolled_students = enrolled_res.data

            if not enrolled_students:
                st.warning(f"No students was enrolled in this course")
                time.sleep(1)
                return

            candidates_dict = {
                s["students"]["student_id"] : s["students"]["voice_embedding"]
                for s in enrolled_students if s["students"].get("voice_embedding")
            }

            if not candidates_dict:
                st.warning("No enrolled students have their voice registered")
                time.sleep(1)
                return

            if not audio_data:
                st.error("Please record classroom audio first.")
                print(type(audio_data))
                return

            audio_bytes = audio_data.read()

            detected_scores = process_bulk_audio(audio_bytes, candidates_dict) 

            results, attendance_to_log = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            for node in enrolled_students:
                student = node["students"]
                score = detected_scores.get(student["student_id"], 0.0)
                is_present = bool(score > 0)

                results.append(
                    {
                        "Name": student["name"],
                        "ID": student["student_id"],
                        "Score": score if is_present else "-",
                        "Status": "☑️ Present" if is_present else "❌ Absent",
                    }
                )

                attendance_to_log.append(
                    {
                        "timestamp" : current_timestamp,
                        "subject_id" : selected_subject_id,
                        "student_id" : student["student_id"],
                        "is_present" : bool(is_present)
                    }
                )
            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)

    st.divider() 

    if st.session_state.get("voice_attendance_results"):
        df_results, logs = st.session_state.voice_attendance_results
        show_attendance_result(df_results, logs)
