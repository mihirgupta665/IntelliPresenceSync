import streamlit as st


def go_home():
    st.session_state["login_type"] = None

def header_home():

    logo_url= "https://i.ibb.co/YTYGn5qV/logo.png"  

    st.markdown(
        f"""
    <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:10px" >
        <img src="{logo_url}" style="height:100px;"  />
        <h1 style="text-align:center; color:#081c36" >IntelliPresenceSync</h1>
    </div>


        """,
        unsafe_allow_html=True,
    )


def header_dashboard():

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
        st.button(
            "Go back to Home",
            type="primary",
            key="go_home_button",
            on_click=go_home,
            shortcut="Ctrl+Backspace",
            width="stretch",
        )

    st.markdown(
        """
        <h1 style="text-align:center; color:#081c36; margin-bottom:30px;">IntelliPresenceSync</h1>
        """,
        unsafe_allow_html=True,
    )
