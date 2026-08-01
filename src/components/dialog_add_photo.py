import streamlit as st
import time 
import numpy as np

from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from src.database.db import execute_with_retries

from PIL import Image 



@st.dialog("Capture or Upload Photos")
def add_photos_dialog():
    st.write("Add classroom photos to scan for attendance")

    if "photo_tab" not in st.session_state:
        st.session_state.photo_tab = "camera"
    if "processed_upload_keys" not in st.session_state:
        st.session_state.processed_upload_keys = set()
    if "processed_camera_key" not in st.session_state:
        st.session_state.processed_camera_key = None

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == "camera" else "tertiary"
        if st.button("Camera", type=type_camera, width="stretch"):
            st.session_state.photo_tab = "camera"
            
    with t2:
        type_upload= "primary" if st.session_state.photo_tab == "upload" else "tertiary"
        if st.button("Upload Photos", type=type_upload, width="stretch"):
            st.session_state.photo_tab = "upload"

    if st.session_state.photo_tab == "camera":
        cam_photo = st.camera_input("Take Snapshot", key="dialog_cam")
        if cam_photo:
            camera_key = f"{cam_photo.name}_{cam_photo.size}"
            if st.session_state.processed_camera_key != camera_key:
                st.session_state.attendance_images.append(Image.open(cam_photo))
                st.session_state.processed_camera_key = camera_key
                st.toast("Photo Captured")
                time.sleep(1)

    if st.session_state.photo_tab == "upload":
        uploaded_files = st.file_uploader("choose image files", type=["jpg", "png", "jpeg"], accept_multiple_files=True, key="dialog_upload")

        if uploaded_files: 
            for f in uploaded_files:
                file_key = f"{f.name}_{f.size}"
                if file_key not in st.session_state.processed_upload_keys:
                    st.session_state.attendance_images.append(Image.open(f))
                    st.session_state.processed_upload_keys.add(file_key)
                    st.toast("Photo Uploaded successfully")
                    time.sleep(1)

    st.divider() 

    if st.button("Done", type="secondary", width="stretch"):
        st.rerun()


            
        
