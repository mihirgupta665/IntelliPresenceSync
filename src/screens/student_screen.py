import streamlit as st
from src.components.footer import footer_dashboard

from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
    style_compact_top_spacing,
)
from src.components.header import header_dashboard

import numpy as np
import time
from PIL import Image

from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student

def student_dashboard():
    st.header("DASHBOARD HERE")

def student_screen():

    style_background_dashboard()
    style_base_layout()
    style_compact_top_spacing()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    header_dashboard()

    st.markdown(
        """
        <style>

            [data-testid="stAppViewContainer"] .block-container {
                padding-top: 10px !important;
                margin-top: -50px !important;
            }
        
            div[data-testid="stHeadingWithActionElements"] {
                margin-top: -1rem !important;
                margin-bottom: -0.45rem !important;
            }

            div[data-testid="stHeadingWithActionElements"] + div[data-testid="stWidgetLabel"] {
                margin-top: -0.4rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    show_registration = False
    st.header("Login using FaceID", text_alignment="center")

    photo_source = st.camera_input("Position your face in the center")
    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("AI is scanning..."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning("No face found in the image!")
            elif num_faces>1:
                st.warning("Multiple faces found in the image")
            else:

                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"]==student_id), None)

                    if student:
                        st.session_state.is_logged_in = True 
                        st.session_state.user_role = "student"
                        st.session_state.student_role = student
                        st.toast(f"{student["name"]} - Welcome Back!")
                        time.sleep(1)
                        st.rerun()


                else:    
                    st.info("Face Not Recognized! You might be a new student")
                    show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header("Register new Profile")
            new_name = st.text_input("Enter your name", placeholder=" Ex. Mihir Gupta")

            st.subheader("(Optional) : Voice Enrollment")
            st.info("Enroll your voice for attendance")

            audio_data = None

            try:
                audio_data = st.audio_input(f"Record a short phrase for voice capturing. Phrase example: 'I am present teacher, My name is {new_name}'")

            except Exception:
                st.error("Error occured during capturing of voice for recording")

                if st.button("Create Account"):
                    if new_name:
                        with st.spinner("Creating Profile..."):
                            img = np.array(Image.open(photo_source))
                            encodings = get_face_embeddings(img)
                            if encodings:
                                face_emb = encodings[0].tolist()

                                voice_emb =  None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())

                                response_data = create_student(new_name, face_embeddings=face_emb, voice_embedding=voice_emb)    

                                if response_data:
                                    train_classifier()

                                    st.session_state.is_logged_in = True 
                                    st.session_state.user_role = "student"
                                    st.session_state.student_role = response_data[0]
                                    st.toast(f"Welcome {new_name} \n Profile Successfully Created")
                                    time.sleep(1)
                                    st.rerun()

                            else:
                                st.error("Error occured while capturing facial features for Registration!")

                    else:
                        st.warning("Please enter your name!")




    footer_dashboard()
