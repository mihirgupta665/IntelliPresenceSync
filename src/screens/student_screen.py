import streamlit as st
from src.components.footer import footer_dashboard

from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
    style_compact_top_spacing,
)
from src.components.header import header_dashboard

import numpy as np
from PIL import Image



def student_screen():

    style_background_dashboard()
    style_base_layout()
    style_compact_top_spacing()

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

    st.header("Login using FaceID", text_alignment="center")

    photo_source = st.camera_input("Position your face in the center")
    if photo_source:
        np.array(Image.open(photo_source))

    footer_dashboard()

