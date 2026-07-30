import streamlit as st
import segno
import io

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "http://localhost:8501"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to Join")

    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind="png", scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("Copy this link to share on Whatsapp or Email")

    with col2:
        st.markdown("### Scan to Join")
        st.image(out.getvalue(), use_column_width=True, caption="QRCode for class joining")















    st.write("Enter the details of new subject")
    sub_id = st.text_input("Subject Code", placeholder="Ex. CSE101")
    sub_name = st.text_input("Subject Name", placeholder="Ex. Introduction to Computer Science")
    sub_section = st.text_input("Section", placeholder="Ex. K23AM")

    if st.button("Create Subject Now", type="primary", width="stretch"):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id, sub_name, sub_section, teacher_id)
                st.toast("Subject Created Successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Error: {str(e)}")

        else:
            st.warning("Please fill all the fields")