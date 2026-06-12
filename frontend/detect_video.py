import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import os
 
from huggingface_hub import hf_hub_download

@st.cache_resource
def load_model():
    model_path = hf_hub_download(
        repo_id="aniket8314/road-damage",
        filename="best.pt"
    )

    return YOLO(model_path)
# MODEL_PATH = 'models/best.pt'
 
def show():
    st.title('Video Road Damage Detection')
 
    uploaded_video = st.file_uploader('Upload video', type=['mp4', 'avi', 'mov'])
 
    if uploaded_video and st.button('Process Video', type='primary'):
        model = load_model()
 
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmp:
            tmp.write(uploaded_video.read())
            tmp_path = tmp.name
 
        cap = cv2.VideoCapture(tmp_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
 
        st.info(f'Video: {total_frames} frames at {fps} FPS')
        progress = st.progress(0)
        frame_display = st.empty()
        stats_display = st.empty()
 
        total_detections = []
        frame_num = 0
 
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
 
            if frame_num % 5 == 0:
                h, w = frame.shape[:2]

                if max(h, w) > 1280:
                    scale = 1280 / max(h, w)
                    frame = cv2.resize(frame,(int(w * scale), int(h * scale)))
                    
                results = model(frame, conf=0.25,imgsz=640, verbose=False)
                annotated = results[0].plot()
                frame_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
                if frame_num%30 ==0:
                    frame_display.image(frame_rgb, use_column_width=True)
 
                for box in results[0].boxes:
                    total_detections.append({
                        'frame': frame_num,
                        'class': model.names[int(box.cls[0])],
                        'conf': float(box.conf[0])
                    })
 
                stats_display.metric('Detections so far', len(total_detections))
 
            progress.progress(frame_num / total_frames)
            frame_num += 1
 
        cap.release()
        os.unlink(tmp_path)
 
        st.success(f'Done! Found {len(total_detections)} total damage instances.')
