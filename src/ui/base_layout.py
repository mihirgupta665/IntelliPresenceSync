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
                    color: #1E293B !important;
                }

                h2{
                    font-family: "Manrope", sans-serif !important ; 
                    font-size: 3.5rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                    color: #1E293B !important;
                }

                h3, h4, p, span{
                    font-family: "Manrope", sans-serif !important ; 
                }

                /
           </style> 
        """,
        unsafe_allow_html=True,
    )
