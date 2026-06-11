import streamlit as st
import requests
import base64
from PIL import Image
import io
 
API_URL = 'https://road-damage-detector-api.onrender.com'
 
def show():
    st.title('Road Damage Detection')
    st.markdown('Upload a road image to detect potholes and cracks.')
 
    col1, col2 = st.columns(2)
 
    with col1:
        uploaded = st.file_uploader(
            'Upload road image',
            type=['jpg', 'jpeg', 'png'],
            help='Supports JPG and PNG'
        )
        conf = st.slider('Confidence threshold', 0.1, 0.9, 0.25, 0.05)
 
        with st.expander('📍 Add GPS Location (optional)'):
            lat = st.number_input('Latitude',  value=25.6093, format='%.6f')
            lon = st.number_input('Longitude', value=85.1376, format='%.6f')
 
    if uploaded and st.button('🔍 Detect Damage', type='primary'):
        with st.spinner('Running AI detection...'):
            try:
                response = requests.post(
                    f'{API_URL}/detect',
                    files={'file': (uploaded.name, uploaded.getvalue(), 'image/jpeg')},
                    data={'latitude': lat, 'longitude': lon, 'conf': conf},
                    timeout=120
                )
            except Exception as e:
                st.error(f"Backend connection error: {e}")
                return
 
        if response.status_code == 200:
            data = response.json()
            detections = data['detections']
 
            with col2:
                img_bytes = base64.b64decode(data['annotated_image_b64'])
                img = Image.open(io.BytesIO(img_bytes))
                st.image(img, caption='Detection Results', use_column_width=True)
 
            st.divider()
            m1, m2, m3, m4 = st.columns(4)
            m1.metric('Total Detected', len(detections))
            m2.metric('Potholes', sum(1 for d in detections if d['class_name']=='pothole'))
            m3.metric('Cracks', sum(1 for d in detections if d['class_name']=='crack'))
            severe = sum(1 for d in detections if d['severity']=='Severe')
            m4.metric('Severe Cases', severe)
 
            if detections:
                st.subheader('Detection Details')
                for i, det in enumerate(detections, 1):
                    color = {'Severe':'🔴','Moderate':'🟡','Minor':'🟢'}[det['severity']]
                    st.write(f"{color} **{det['class_name'].title()}** — {det['severity']} — conf: {det['confidence']}")
        else:
            st.error(f'Detection failed: {response.text}')
