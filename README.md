# 🛣️ AI Road Damage Detection System
 
![Python](https://img.shields.io/badge/Python-3.11-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-ultralytics-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
![License](https://img.shields.io/badge/license-MIT-blue)
 
> End-to-end AI platform detecting road potholes and cracks
> using YOLOv8, with GPS mapping and real-time dashboard analytics.
 
🔗 **[Live Demo](https://your-app.streamlit.app)**
📄 **[API Docs](https://your-api.onrender.com/docs)**
 
## 🎯 Problem
India has 6.3 million km of roads. Manual inspection is slow,
expensive, and inconsistent. This system automates detection
using any camera — dashcam, phone, or drone.
 
## ✨ Features
- Real-time pothole & crack detection (YOLOv8s, mAP@0.5: 0.87)
- Severity scoring: Minor / Moderate / Severe
- GPS-tagged reports stored in PostgreSQL
- Interactive map dashboard with Folium
- FastAPI backend with OpenAPI docs
- Video frame-by-frame analysis
 
## 🏗️ Architecture
[paste your architecture diagram here]
 
## 🚀 Quick Start
```bash
git clone https://github.com/you/road-damage-detector
cd road-damage-detector
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.main:app --reload  # terminal 1
streamlit run app.py               # terminal 2
```
 
## 📊 Model Performance
| Metric | Value |
|--------|-------|
| mAP@0.5 | 0.87 |
| Precision | 0.84 |
| Recall | 0.81 |
| Inference speed | 23ms/image |
 
## 🛠️ Tech Stack
YOLOv8 · OpenCV · FastAPI · Streamlit · PostgreSQL · Folium
