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

    t1, t2 = st.columns(2)

    with t1:
        type_camera = "primary" if st.session_state.photo_tab == "camera" else "tertiary"
        if st.button("Camera", type="type_camera", width="stretch"):
            st.session_state.photo_tab = "camera"
            
    with t2:
        type_upload= "primary" if st.session_state.photo_tab == "upload" else "tertiary"
        if st.button("Upload Photos", type="type_upload", width="stretch"):
            st.session_state.photo_tab = "upload"

    if st.session_state.photo_tab == "camera":
        cam_photo = st.camera_input("Take Snapshot", key="dialog_cam")
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast("Photo Captured")
            time.sleep(1)
            st.rerun()

    if st.session_state.photo_tab == "upload":
        uploaded_files = st.file_uploader("choose image files", type=["jpg", "png", "jpeg"], accept_multiple_files=True, key="dialog_upload")

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))

                st.toast("Photo Uploaded successfully")
                time.sleep(1)
                st.rerun()

    st.divider()

    if st.session_state.attendance_images:
        st.header("Added Photos")
        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width="stretch", caption=f"Photo {idx+1}")

        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button("Clear All Photos", width="stretch", type="tertiary", icon=":material/delete:"):
                st.session_state.attendance_images = []
                st.success("All Images Cleared")
                time.sleep(1)
                st.rerun()

        with c2:
            has_photos = bool(st.session_state.attendance_images)
            if st.button("Run Face Analysis", width="stretch", type="primary", icon=":material/analytics:"):
                with st.spinner("Deep Scanning Classroom Photos..."):
                    all_detected_id = {}

                    for idx, img in enumerate(st.session_state.attendance_images):
                        img_np = np.array(img.convert("RGB"))
                        detected, _, _ = predict_attendance(img_np)

                        if detected:
                            for sid in detected.key








    if st.button("Done", type="secondary", width="stretch"):
        st.rerun()


            
        
