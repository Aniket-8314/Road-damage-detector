import streamlit as st

def show():

    col1, col2, col3 = st.columns([1, 3, 1])

    with col2:

        st.markdown(
            """
            <div style='text-align:center;padding-top:60px'>
                <h1>🛣️ AI Road Damage Detector</h1>
                <h3>Smart Road Inspection using Computer Vision</h3>
                <br>
                <p style='font-size:20px'>
                    Detect potholes, cracks, and road damages using
                    AI-powered image and video analysis.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown(
            """
            ### Features

            ✅ Road Damage Detection from Images

            ✅ Real-Time Video Analysis

            ✅ Interactive Damage Map Dashboard

            ✅ Analytics & Reports

            ✅ YOLO-based AI Detection
            """
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 Enter Application", use_container_width=True):
            st.session_state.entered_app = True
            st.rerun()