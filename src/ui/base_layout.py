import streamlit as st

def style_base_layout():

    st.markdown(
        """
           <style>
                @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@200..800&display=swap');

                /* Hide default of streamlit  */
                #MainMenu, footer, header {
                    visibility: hidden;
                }
                .block-container {
                    padding-top:1.5rem !important
                }

                h1{
                    font-family: "Manrope", sans-serif !important ; 
                    font-size: 3.5rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #756106 !important;
                }

                h2{
                    font-family: "Manrope", sans-serif !important ; 
                    font-size: 2rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #081c36 !important;
                }

                h3, h4, p{
                    font-family: "Manrope", sans-serif !important ; 
                }

                /* Primary Button */
                button {
                    font-family: "Manrope", sans-serif !important;
                    font-weight: 600 !important;
                    border-radius: 14px !important;
                    background: #e8b582 !important;
                    color: #000000 !important;
                    padding: 10px 22px !important;
                    border: none !important;
                    cursor: pointer !important;
                    transition: all 0.25s ease !important;
                }

                /* Secondary Button */
                button[kind="secondary"] {
                    font-family: "Manrope", sans-serif !important;
                    font-weight: 600 !important;
                    border-radius: 14px !important;
                    background: #1e4d8a !important;
                    color: #FFFFFF !important;
                    padding: 10px 22px !important;
                    border: 1px solid #E6DCC8 !important;
                    cursor: pointer !important;
                    transition: all 0.25s ease !important;
                }

                /* Tertiary Button */
                button[kind="tertiary"] {
                    font-family: "Manrope", sans-serif !important;
                    font-weight: 600 !important;
                    border-radius: 14px !important;
                    background: #0F766E !important;
                    color: #FFFFFF !important;
                    padding: 10px 22px !important;
                    border: none !important;
                    cursor: pointer !important;
                    transition: all 0.25s ease !important;
                }

                /* Primary Button Hover */
                button:hover {
                    background: #DFA46A !important;
                    transform: translateY(-2px) scale(1.05);
                    box-shadow: 0 10px 24px rgba(232, 181, 130, 0.35);
                }

                /* Secondary Button Hover */
                button[kind="secondary"]:hover {
                    background: #174173 !important;
                    transform: translateY(-2px) scale(1.05);
                    box-shadow: 0 5px 10px rgba(30, 77, 138, 0.30);
                }

                /* Tertiary Button Hover */
                button[kind="tertiary"]:hover {
                    background: #0C625B !important;
                    transform: translateY(-2px) scale(1.05);
                    box-shadow: 0 10px 24px rgba(15, 118, 110, 0.30);
                }


           </style> 
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():

    st.markdown(
        """
           <style>

                .stApp {
                    background: #FEF5E7 !important
                }

           </style> 
        """,
        unsafe_allow_html=True,
    )


def style_background_home():

    st.markdown(
        """
           <style>

                .stApp {
                    background: #FEF5E7 !important
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #FFF !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                }

           </style> 
        """,
        unsafe_allow_html=True,
    )
