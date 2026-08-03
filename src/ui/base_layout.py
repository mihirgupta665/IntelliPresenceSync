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
                }

                h2{
                    font-family: "Manrope", sans-serif !important ; 
                    font-size: 2rem !important;
                    line-height: 1.1 !important;
                    margin-bottom: 0rem !important;
                }

                h3, h4, p{
                    font-family: "Manrope", sans-serif !important ; 
                }

                 /* Primary Button */
                 .stButton button {
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
                 .stButton button[kind="secondary"], btnsec {
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
                 .stButton button[kind="tertiary"] {
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
                 .stButton button:hover {
                     background: #DFA46A !important;
                     transform: translateY(-2px) scale(1.05);
                     box-shadow: 0 10px 24px rgba(232, 181, 130, 0.35);
                 }

                 /* Secondary Button Hover */
                 .stButton button[kind="secondary"]:hover {
                     background: #174173 !important;
                     transform: translateY(-2px) scale(1.05);
                     box-shadow: 0 5px 10px rgba(30, 77, 138, 0.30);
                 }

                 div.st-key-go_home_button button {
                     min-width: 15rem !important;
                     white-space: nowrap !important;
                     justify-content: center !important;
                     padding: 0.9rem 1.4rem !important;
                     border-radius: 18px !important;
                 }

                 /* Tertiary Button Hover */
                 .stButton button[kind="tertiary"]:hover {
                     background: #0C625B !important;
                     transform: translateY(-2px) scale(1.05);
                     box-shadow: 0 10px 24px rgba(15, 118, 110, 0.30);
                 }

                 /* -------------------------------------------------------------
                    st.audio_input Styling (Aesthetic, Premium & Well-Layouted)
                    ------------------------------------------------------------- */
                 
                 /* 1. Main outer container styling */
                 div[data-testid="stAudioInput"] {
                     background-color: #FFFFFF !important;
                     border: 1px solid #E6DCC8 !important;
                     border-radius: 18px !important;
                     padding: 16px !important;
                     box-shadow: 0 4px 20px rgba(232, 181, 130, 0.08) !important;
                     margin: 10px 0 20px 0 !important;
                     transition: all 0.3s ease !important;
                 }
                 
                 div[data-testid="stAudioInput"]:hover {
                     box-shadow: 0 6px 24px rgba(232, 181, 130, 0.15) !important;
                     border-color: #e8b582 !important;
                 }

                 /* Label customization */
                 div[data-testid="stAudioInput"] label {
                     font-family: "Manrope", sans-serif !important;
                     font-weight: 700 !important;
                     color: #081c36 !important;
                     font-size: 1rem !important;
                     margin-bottom: 12px !important;
                 }

                 /* 2. Inner player bar customization */
                 div[data-testid="stAudioInput"] > div:nth-child(2),
                 div[data-testid="stAudioInput"] > div:not([data-testid="stWidgetLabel"]) {
                     background-color: #FEF9F0 !important;
                     border-radius: 12px !important;
                     border: 1px solid #F1E7D8 !important;
                     height: 54px !important;
                     padding-left: 16px !important;
                     padding-right: 90px !important; /* Extra padding on the right for toolbar buttons */
                     display: flex !important;
                     align-items: center !important;
                     position: relative !important;
                     overflow: visible !important; /* Prevent clipping of toolbar buttons */
                 }

                 /* 3. Action buttons (Record, Stop, Play, Pause) */
                 div[data-testid="stAudioInput"] button[data-testid="stAudioInputActionButton"] {
                     background-color: #e8b582 !important;
                     color: #000000 !important;
                     border: none !important;
                     border-radius: 50% !important;
                     width: 38px !important;
                     height: 38px !important;
                     min-width: 38px !important;
                     max-width: 38px !important;
                     padding: 0 !important;
                     margin: 0 4px !important;
                     display: flex !important;
                     align-items: center !important;
                     justify-content: center !important;
                     box-shadow: 0 2px 6px rgba(232, 181, 130, 0.3) !important;
                     cursor: pointer !important;
                     transform: none !important;
                     transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
                 }

                 div[data-testid="stAudioInput"] button[data-testid="stAudioInputActionButton"]:hover {
                     background-color: #DFA46A !important;
                     transform: scale(1.1) !important;
                     box-shadow: 0 4px 12px rgba(232, 181, 130, 0.5) !important;
                 }

                 div[data-testid="stAudioInput"] button[data-testid="stAudioInputActionButton"]:active {
                     transform: scale(0.95) !important;
                 }

                 /* Stop recording button has red accents for caution */
                 div[data-testid="stAudioInput"] button[aria-label="Stop recording"] {
                     background-color: #ff6b6b !important;
                     color: #ffffff !important;
                     box-shadow: 0 2px 6px rgba(255, 107, 107, 0.3) !important;
                 }

                 div[data-testid="stAudioInput"] button[aria-label="Stop recording"]:hover {
                     background-color: #e85a5a !important;
                     box-shadow: 0 4px 12px rgba(255, 107, 107, 0.5) !important;
                 }

                 /* 4. Toolbar action buttons (Download as WAV, Clear recording at the top-right) */
                 /* Position the toolbar inside the player bar on the far right */
                 div[data-testid="stAudioInput"] [data-testid="stWidgetActionGroup"],
                 div[data-testid="stAudioInput"] div[class*="Toolbar"] {
                     position: absolute !important;
                     top: 50% !important;
                     right: 12px !important;
                     transform: translateY(-50%) !important;
                     display: flex !important;
                     flex-direction: row !important;
                     align-items: center !important;
                     gap: 6px !important;
                     margin: 0 !important;
                     padding: 0 !important;
                     background: transparent !important;
                     border: none !important;
                     z-index: 99 !important;
                     height: auto !important;
                     width: auto !important;
                 }

                 /* Reset toolbar nested division background and margins */
                 div[data-testid="stAudioInput"] [data-testid="stWidgetActionGroup"] > div,
                 div[data-testid="stAudioInput"] div[class*="Toolbar"] > div {
                     background-color: transparent !important;
                     border: none !important;
                     box-shadow: none !important;
                     padding: 0 !important;
                     margin: 0 !important;
                     display: flex !important;
                     gap: 6px !important;
                 }

                 div[data-testid="stAudioInput"] div[class*="Toolbar"] button,
                 div[data-testid="stAudioInput"] [data-testid="stWidgetActionGroup"] button,
                 div[data-testid="stAudioInput"] button[aria-label*="download"],
                 div[data-testid="stAudioInput"] button[aria-label*="clear"],
                 div[data-testid="stAudioInput"] button[aria-label*="Clear"],
                 div[data-testid="stAudioInput"] button[aria-label*="Download"] {
                     background-color: #1e4d8a !important; /* Premium deep blue background */
                     color: #FFFFFF !important;
                     border: none !important;
                     padding: 6px !important;
                     width: 32px !important;
                     height: 32px !important;
                     min-width: 32px !important;
                     max-width: 32px !important;
                     border-radius: 8px !important;
                     box-shadow: 0 2px 4px rgba(30, 77, 138, 0.2) !important;
                     display: inline-flex !important;
                     align-items: center !important;
                     justify-content: center !important;
                     transition: all 0.2s ease !important;
                     cursor: pointer !important;
                 }

                 div[data-testid="stAudioInput"] div[class*="Toolbar"] button:hover,
                 div[data-testid="stAudioInput"] [data-testid="stWidgetActionGroup"] button:hover {
                     background-color: #174173 !important;
                     transform: translateY(-2px) scale(1.08) !important;
                     box-shadow: 0 4px 8px rgba(30, 77, 138, 0.4) !important;
                 }

                 div[data-testid="stAudioInput"] div[class*="Toolbar"] button:active,
                 div[data-testid="stAudioInput"] [data-testid="stWidgetActionGroup"] button:active {
                     transform: translateY(0) scale(0.95) !important;
                     box-shadow: 0 2px 4px rgba(30, 77, 138, 0.2) !important;
                 }

                 /* Specific icon adjustments inside toolbar */
                 div[data-testid="stAudioInput"] div[class*="Toolbar"] svg,
                 div[data-testid="stAudioInput"] [data-testid="stWidgetActionGroup"] svg {
                     width: 16px !important;
                     height: 16px !important;
                     fill: #FFFFFF !important;
                     color: #FFFFFF !important;
                 }

                 /* 5. Waveform container adjustments */
                 div[data-testid="stAudioInput"] [data-testid="stAudioInputWaveSurfer"] {
                     height: 32px !important;
                     display: flex !important;
                     align-items: center !important;
                 }

                 /* 6. Timecode text (monospace font) */
                 div[data-testid="stAudioInput"] [data-testid="stAudioInputWaveformTimeCode"] {
                     font-family: "Courier New", Courier, monospace !important;
                     font-weight: bold !important;
                     color: #081c36 !important;
                     font-size: 0.9rem !important;
                     margin-left: 8px !important;
                     opacity: 0.8 !important;
                 }

                 /* -------------------------------------------------------------
                    Dark Mode Theme Adaptation & Widget Visual Stabilization
                    ------------------------------------------------------------- */

                 /* -------------------------------------------------------------
                    Light Mode Defaults (Text Colors, Dialog Background)
                    ------------------------------------------------------------- */
                 h1 {
                     color: #756106 !important;
                 }
                 h2 {
                     color: #081c36 !important;
                 }
                 h3, h4, h5, h6, p, span, li, label,
                 div[data-testid="stMarkdownContainer"] p,
                 div[data-testid="stMarkdownContainer"] li,
                 div[data-testid="stMarkdownContainer"] span,
                 div[data-testid="stMarkdownContainer"] h3,
                 div[data-testid="stMarkdownContainer"] h4,
                 div[data-testid="stMarkdownContainer"] h5,
                 div[data-testid="stMarkdownContainer"] h6,
                 label[data-testid="stWidgetLabel"] p,
                 label[data-testid="stWidgetLabel"] span,
                 div[data-testid="stWidgetLabel"] p,
                 .stMarkdown,
                 .stText,
                 .stCaption {
                     color: #081c36 !important;
                 }

                 div[role="dialog"] {
                     background-color: #FEF5E7 !important;
                     color: #081c36 !important;
                 }
                 div[role="dialog"] div[data-testid="stMarkdownContainer"] p,
                 div[role="dialog"] label[data-testid="stWidgetLabel"] p {
                     color: #081c36 !important;
                 }

                 /* -------------------------------------------------------------
                    Global Overrides (Always White Background and Black Text for Inputs)
                    ------------------------------------------------------------- */
                 
                  /* Input Fields (Text, Selectbox, File Uploaders) */
                  div[data-testid="stTextInput"] input,
                  div[data-testid="stNumberInput"] input,
                  div[data-testid="stTextArea"] textarea {
                      background-color: #FFFFFF !important;
                      color: #000000 !important;
                  }

                  /* Force light color-scheme on inputs to block browser Auto Dark Mode color inversion */
                  div[data-testid="stTextInput"],
                  div[data-testid="stTextInput"] *,
                  div[data-testid="stNumberInput"],
                  div[data-testid="stNumberInput"] *,
                  div[data-testid="stTextArea"],
                  div[data-testid="stTextArea"] * {
                      color-scheme: light !important;
                  }

                  /* Input Parent Containers */
                  div[data-testid="stTextInput"] div[data-baseweb="input"],
                  div[data-testid="stNumberInput"] div[data-baseweb="input"],
                  div[data-testid="stTextArea"] div[data-baseweb="textarea"] {
                      background: #FFFFFF !important;
                      background-color: #FFFFFF !important;
                      border-color: #E6DCC8 !important;
                  }

                  /* Force all descendants of the input container to have transparent background (e.g. eye icon wrapper) */
                  div[data-baseweb="input"] *,
                  div[data-baseweb="textarea"] * {
                      background: transparent !important;
                      background-color: transparent !important;
                  }

                  /* Force buttons and divs inside the input box to be transparent in all states (hover/active/focus) */
                  div[data-baseweb="input"] button,
                  div[data-baseweb="input"] button:hover,
                  div[data-baseweb="input"] button:active,
                  div[data-baseweb="input"] button:focus,
                  div[data-testid="stTextInput"] div[data-baseweb="input"] div,
                  div[data-testid="stTextInput"] div[data-baseweb="input"] button {
                      background: transparent !important;
                      background-color: transparent !important;
                      box-shadow: none !important;
                      border: none !important;
                  }

                  /* Ensure the toggle button (eye icon) SVG is dark and visible */
                  div[data-baseweb="input"] button svg,
                  div[data-baseweb="input"] svg {
                      fill: #081c36 !important;
                      color: #081c36 !important;
                  }

                  /* Force input border and outline styling on focus and active states */
                  div[data-baseweb="input"]:focus-within,
                  div[data-baseweb="textarea"]:focus-within {
                      border-color: #e8b582 !important;
                      box-shadow: 0 0 0 1px #e8b582 !important;
                      outline: none !important;
                  }

                  /* Placeholder Text Styling (Force dark gray placeholder in all inputs) */
                  div[data-testid="stTextInput"] input::placeholder,
                  div[data-testid="stNumberInput"] input::placeholder,
                  div[data-testid="stTextArea"] textarea::placeholder,
                  input::placeholder,
                  textarea::placeholder {
                      color: #666666 !important;
                      opacity: 1 !important; /* Firefox */
                  }

                  /* Webkit/Blink placeholder override */
                  div[data-testid="stTextInput"] input::-webkit-input-placeholder,
                  input::-webkit-input-placeholder {
                      color: #666666 !important;
                      opacity: 1 !important;
                  }

                  /* Firefox placeholder override */
                  div[data-testid="stTextInput"] input::-moz-placeholder,
                  input::-moz-placeholder {
                      color: #666666 !important;
                      opacity: 1 !important;
                  }

                 /* Select Box Trigger */
                 div[data-testid="stSelectbox"] div[data-baseweb="select"] {
                     background-color: #FFFFFF !important;
                     border-color: #E6DCC8 !important;
                 }

                 /* Select Box Selected Option */
                 div[data-testid="stSelectbox"] div[data-baseweb="select"] div[class*="StyledValue"] {
                     color: #000000 !important;
                 }

                 /* Select Dropdown Portal / List Box Options */
                 div[data-baseweb="popover"] ul,
                 div[data-baseweb="popover"] li,
                 div[role="listbox"],
                 ul[role="listbox"] {
                     background-color: #FFFFFF !important;
                     color: #000000 !important;
                 }

                 div[data-baseweb="popover"] li:hover,
                 div[role="listbox"] li:hover {
                     background-color: #FEF5E7 !important;
                     color: #081c36 !important;
                 }

                 /* File Uploader Dropzone & Filename */
                 div[data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] {
                     background-color: #FFFFFF !important;
                     border: 1px dashed #E6DCC8 !important;
                     color: #081c36 !important;
                 }
                 div[data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] div {
                     color: #081c36 !important;
                 }
                 div[data-testid="stFileUploader"] div[data-testid="stFileUploaderFileName"] {
                     color: #081c36 !important;
                 }

                 /* Ensure button text inherits button color instead of getting overridden by global text rules */
                 .stButton button,
                 .stButton button *,
                 .stButton button p,
                 .stButton button span,
                 .stButton button div,
                 .stButton button [data-testid="stMarkdownContainer"] p,
                 .stButton button [data-testid="stMarkdownContainer"] span,
                 div[data-testid="stAudioInput"] button,
                 div[data-testid="stAudioInput"] button *,
                 [role="button"],
                 [role="button"] *,
                 [role="button"] p,
                 [role="button"] span {
                     color: inherit !important;
                 }

                 /* -------------------------------------------------------------
                    Streamlit Component Color Stabilization (Prevent Dark Mode Distortions)
                    ------------------------------------------------------------- */
                 
                 /* Sidebar Styling (Keep Cream Background and Dark Text) */
                 section[data-testid="stSidebar"],
                 section[data-testid="stSidebar"] div,
                 section[data-testid="stSidebar"] p,
                 section[data-testid="stSidebar"] span,
                 section[data-testid="stSidebar"] label {
                     background-color: #FEF5E7 !important;
                     color: #081c36 !important;
                 }
                 section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
                     color: #081c36 !important;
                 }

                 /* Toast Messages Styling (Keep Cream Background and Dark Text) */
                 div[data-testid="stToast"],
                 .stToast {
                     background-color: #FEF9F0 !important;
                     border: 1px solid #E6DCC8 !important;
                     color: #081c36 !important;
                     box-shadow: 0 4px 12px rgba(232, 181, 130, 0.15) !important;
                 }
                 div[data-testid="stToast"] p,
                 div[data-testid="stToast"] span,
                 div[data-testid="stToast"] div {
                     color: #081c36 !important;
                 }

                 /* Alert Banners (Success, Error, Info, Warning) */
                 div[data-testid="stAlert"],
                 div[data-testid="stAlert"] * {
                     background-color: #FEF9F0 !important;
                     border-color: #E6DCC8 !important;
                     color: #081c36 !important;
                 }

                 /* Expanders (Keep White Background and Dark Text) */
                 div[data-testid="stExpander"] {
                     background-color: #FFFFFF !important;
                     border: 1px solid #E6DCC8 !important;
                 }
                 div[data-testid="stExpander"] details summary,
                 div[data-testid="stExpander"] details summary * {
                     color: #081c36 !important;
                 }

                 /* Spinner Text (Always Dark Blue) */
                 div[data-testid="stSpinner"] {
                     color: #081c36 !important;
                 }

                 /* Horizontal Dividers */
                 hr {
                     border-color: #E6DCC8 !important;
                 }

                 /* Dialog Close Button (Always Dark Icon) */
                 div[role="dialog"] button svg {
                     fill: #081c36 !important;
                     color: #081c36 !important;
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


def style_compact_top_spacing():

    st.markdown(
        """
           <style>
                [data-testid="stAppViewContainer"] .block-container {
                    padding-top: 10px !important;
                    margin-top: -30px !important;
                }
           </style>
        """,
        unsafe_allow_html=True,
    )
