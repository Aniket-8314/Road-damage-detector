import streamlit as st

st.set_page_config(
    page_title="Road Damage Detector",
    page_icon="🛣️",
    layout="wide"
)

# Initialize state
if "entered_app" not in st.session_state:
    st.session_state.entered_app = False

# HOME PAGE
if not st.session_state.entered_app:
    from frontend.home import show
    show()

# MAIN APPLICATION
else:
    st.sidebar.title("🛣️ Road Damage AI")

    page = st.sidebar.radio(
        "Navigate",
        [
            "📸 Detect Image",
            "🎥 Detect Video",
            "🗺️ Map Dashboard",
            "📊 Analytics"
        ]
    )

    if page == "📸 Detect Image":
        from frontend.detect_image import show

    elif page == "🎥 Detect Video":
        from frontend.detect_video import show

    elif page == "🗺️ Map Dashboard":
        from frontend.map_dashboard import show

    elif page == "📊 Analytics":
        from frontend.analytics import show

    show()