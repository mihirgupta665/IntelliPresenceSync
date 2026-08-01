import streamlit as st
import numpy as np
import pandas as pd

import time
from datetime import datetime

from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
    style_compact_top_spacing,
)

from src.database.config import supabase
from src.database.db import check_teacher_exist, create_teacher, teacher_login, get_teacher_subjects, execute_with_retries

from src.pipelines.face_pipeline import predict_attendance

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog
from src.components.dialog_attendance_result import attendance_result_dialog


def teacher_screen():

    style_background_dashboard()
    style_base_layout()
    style_compact_top_spacing()

    # header_dashboard()
    # st.header("Register your teacher profile")

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif "teacher_login_type" not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    logo_url= "https://i.ibb.co/YTYGn5qV/logo.png"  

    logo_col, spacer_col, action_col = st.columns([1.2, 2.2, 2.2], vertical_alignment="center")

    with logo_col:
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-start;">
                <img src="{logo_url}" style="height:100px;" />
            </div>
            """,
            unsafe_allow_html=True,
        )

    with action_col:
        if st.button( "Logout",  type="primary",  key="loginbackbtn", shortcut="Ctrl+Backspace", width="stretch"):
            st.session_state["is_logged_in"] = False
            del st.session_state.teacher_data
            st.rerun()

    st.markdown(
        """
        <h1 style="text-align:center; color:#081c36; margin-bottom:30px;">IntelliPresenceSync</h1>
        """,
        unsafe_allow_html=True,
    )

    st.header(f"""Welcome, {teacher_data["name"]} """)

    # st.space()

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = "take_attendance"

    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == "take_attendance" else "tertiary"
        if st.button("Take Attendance", type=type1, width="stretch", icon=":material/ar_on_you:"):
            st.session_state.current_teacher_tab = "take_attendance"
            st.rerun()        

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == "manage_subjects" else "tertiary"
        if st.button("Manage Subjects", type=type2, width="stretch", icon=":material/book_ribbon:"):
            st.session_state.current_teacher_tab = "manage_subjects"
            st.rerun()        

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == "attendance_records" else "tertiary"
        if st.button("Attendance Records", type=type3, width="stretch", icon=":material/library_books:"):
            st.session_state.current_teacher_tab = "attendance_records"
            st.rerun()

    st.divider()


    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()
    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()


    footer_dashboard()


def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data["teacher_id"]
    st.header("AI Powered Attendance")

    if "attendance_images" not in st.session_state:
        st.session_state.attendance_images = [] 

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning("You have not created any subjects yet! Please Create on to begin!")
        return 

    subject_options = { f"{s["name"]} - {s["subject_code"]}" : s["subject_id"] for s in subjects }

    col1, col2 = st.columns([3,1])

    with col1:
        selected_subject_label = st.selectbox("Select Subject", options=list(subject_options.keys()))

    with col2:
        if st.button("Add Photos", type="primary", icon=":material/photo_prints:", width="stretch"):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

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
                    all_detected_ids = {}

                    for idx, img in enumerate(st.session_state.attendance_images):
                        img_np = np.array(img.convert("RGB"))
                        detected, _, _ = predict_attendance(img_np)

                        if detected:
                            for sid in detected.keys():
                                student_id = int(sid)

                                all_detected_ids.setdefault(student_id, []).append(f"Photo {idx+1}")

                    enrolled_res = execute_with_retries(supabase.table("subject_students").select("*, students(*)").eq("subject_id", selected_subject_id))
                    enrolled_students = enrolled_res.data

                    if not enrolled_students:
                        st.warning(f"No students was enrolled in {selected_subject_label}")

                    else:
                        results, attendance_to_log = [], []

                        current_timestamp = datetime.now().strftime("%y-%m-%dT%H:%M:%S")

                        for node in enrolled_students:
                            student = node["students"]
                            sources = all_detected_ids.get(int(student["student_id"]), [])
                            is_present = len(sources) > 0

                            results.append(
                                {
                                    "Name": student["name"],
                                    "ID": student["student_id"],
                                    "Source": ( ", ".join(sources) if is_present else "--" ),
                                    "Status": "☑️ Present" if is_present else "❌ Absent",
                                }
                            )

                            attendance_to_log.append(
                                {
                                    "student_id" : student["student_id"],
                                    "subject_id" : selected_subject_id,
                                    "timestamp" : current_timestamp,
                                    "is_present" : bool(is_present),
                                }
                            )

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

        with c3:
            if st.button("Use Voice Attendance", type="secondary", widtg="stretch", icon=":material/mic:"):
                voice_attendance_dialog()

                



def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data["teacher_id"]
    col1, col2 = st.columns(2)
    with col1:
        st.header("Subjects Management")
    with col2:
        if st.button("Create new Subject", width="stretch"):
            create_subject_dialog(teacher_id)

    # List All Subjects
    subjects = get_teacher_subjects(teacher_id)
    if subjects:
        for sub in subjects:
            stats = [
                ("🧑‍🎓👩‍🎓", "Students", sub["total_students"]),
                ("🕰️", "Classes", sub["total_classes"]),
            ]
            def share_btn():
                if st.button(f"Share Code: {sub["name"]}", key=f"share_{sub["subject_code"]}", type="primary", icon=":material/share:"):
                    share_subject_dialog(sub["name"], sub["subject_code"])
                st.space(size="xxsmall")

            subject_card(
                name = sub["name"],
                code = sub["subject_code"],
                section = sub["section"],
                stats = stats,
                footer_callback=share_btn
            )
    else:
        st.info("No Subject Found. Create your first Subject")


def teacher_tab_attendance_records():
    st.header("Attendance Records")


def login_teacher(username, password):
    if not username or not password:
        st.error("All Fields are Required!")
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True

    else:
        return False


def teacher_screen_login():
    header_dashboard()

    st.header("Login using password", text_alignment="center")
    st.space(size="small")

    teacher_username = st.text_input("Enter Username", placeholder="Ex. MihirGupta665 " )
    teacher_pass = st.text_input("Enter Password", type="password", placeholder="********")
    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Login", type="tertiary", icon=":material/passkey:", shortcut="control+enter", width="stretch"):
            if login_teacher(teacher_username, teacher_pass):
                st.toast(f"Welcome back {teacher_username}", icon="👋")
                import time
                time.sleep(1)
                st.rerun()
            else:
                st.error("Invalid Credentials")


    with btnc2:
        if st.button("Register Instead", type="secondary", icon=":material/passkey:", width="stretch"):
            st.session_state.teacher_login_type = "register" 

    footer_dashboard()


def register_teacher(teacher_username, teacher_pass, teacher_name, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass or not teacher_pass_confirm:
        return False, "All Fields are required!"

    if teacher_pass_confirm!=teacher_pass:
        return False, "Confirm Password does not match!"

    if check_teacher_exist(teacher_username):
        return False, "Username has already been taken"

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Teacher registration successfull"

    except Exception as e:
        return False, "Error occured while registering teacher"


def teacher_screen_register():
    header_dashboard()

    st.header("Register your teacher profile", text_alignment="center")
    st.space(size="small")

    teacher_username = st.text_input("Enter Username", placeholder="Ex. MihirGupta665 " )
    teacher_name = st.text_input("Enter Your Name", placeholder="Ex. Mihir Gupta" )

    teacher_pass = st.text_input("Enter Password", type="password", placeholder="********")
    teacher_pass_confirm = st.text_input("Confirm Password", type="password", placeholder="********")
    st.space("xxsmall")

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button("Register Now", type=    "tertiary", icon=":material/passkey:", shortcut="control+enter", width="stretch"):
            success, message = register_teacher(teacher_username, teacher_pass, teacher_name, teacher_pass_confirm)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = "login"
                st.rerun()
            else:
                st.error(message)


    with btnc2:
        if st.button("Login Instead", type="secondary", icon=":material/passkey:", width="stretch"):
            st.session_state.teacher_login_type = "login"
                 

    footer_dashboard()
