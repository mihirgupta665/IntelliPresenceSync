import streamlit as st
from src.components.footer import footer_dashboard

from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
    style_compact_top_spacing,
)
from src.components.header import header_dashboard

def teacher_screen():

    style_background_dashboard()
    style_base_layout()
    style_compact_top_spacing()

    # header_dashboard()
    # st.header("Register your teacher profile")
    teacher_screen_login()


def teacher_screen_login():
    header_dashboard()
    

    st.header("Login using password", text_alignment="center")
    st.space(size="small")

    teacher_username = st.text_input("Enter Username", placeholder="Ex. Mihir Gupta" )
    teacher_pass = st.text_input("Enter Password", type="password", placeholder="********")
    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        st.button("Login", type="tertiary", icon=":material/passkey:", shortcut="control+enter", width="stretch")
    with btnc2:
        st.button("Register Instead", type="secondary", icon=":material/passkey:", width="stretch")


    footer_dashboard()


def teacher_screen_register():
    header_dashboard()
    

    st.header("Login using password", text_alignment="center")
    st.space(size="small")

    teacher_username = st.text_input("Enter Username", placeholder="Ex. Mihir Gupta" )
    teacher_pass = st.text_input("Enter Password", type="password", placeholder="********")
    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        st.button("Login", type="tertiary", icon=":material/passkey:", shortcut="control+enter", width="stretch")
    with btnc2:
        st.button("Register Instead", type="secondary", icon=":material/passkey:", width="stretch")


    footer_dashboard()
       
