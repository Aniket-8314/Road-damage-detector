# 🛣️ AI-Powered Road Damage Detection System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![License](https://img.shields.io/badge/License-MIT-success)

An end-to-end AI system that automatically detects road damages such as potholes and cracks from images and videos using YOLOv8. The platform provides real-time detection, severity analysis, GPS-based mapping, analytics dashboards, and cloud deployment.

---

## 🚀 Live Demo

* Frontend: https://road-damage-detector-a.streamlit.app
* Backend API: https://road-damage-detector-api.onrender.com
* API Documentation: https://road-damage-detector-api.onrender.com/docs
* Model Repository: https://huggingface.co/aniket8314/road-damage

---

## 📌 Problem Statement

Road damage inspection is traditionally performed manually, making it:

* Time-consuming
* Expensive
* Error-prone
* Difficult to scale

This project automates the process using Computer Vision and Deep Learning, enabling faster and more consistent road condition monitoring.

---

## ✨ Features

### AI Detection

* Detect potholes and road cracks using YOLOv8
* Confidence-based predictions
* Severity classification (Minor, Moderate, Severe)
* Image and video support

### Interactive Dashboard

* Upload road images for instant analysis
* Detection visualization with bounding boxes
* Damage statistics dashboard
* Historical detection reports

### GPS Mapping

* Store GPS coordinates with each detection
* Interactive map visualization using Folium
* Damage hotspot identification

### Backend Services

* FastAPI REST API
* PostgreSQL integration
* Detection history storage
* OpenAPI documentation

---

## 🏗️ System Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── YOLOv8 Inference Engine
  │
  ├── PostgreSQL Database
  │
  └── Hugging Face Model Repository
```

---

## 🛠️ Tech Stack

### Machine Learning

* YOLOv8
* PyTorch
* OpenCV
* NumPy

### Backend

* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn

### Frontend

* Streamlit
* Plotly
* Folium
* Streamlit-Folium

### Deployment

* Render
* Streamlit Cloud
* Hugging Face Hub

---

## 📊 Model Performance

### YOLOv8n

| Metric       | Score |
| ------------ | ----- |
| Precision    | 0.621 |
| Recall       | 0.595 |
| mAP@0.5      | 0.605 |
| mAP@0.5:0.95 | 0.274 |

Training Configuration:

* Model: YOLOv8n
* Epochs: 100
* Image Size: 640 × 640
* Batch Size: 16

---

## 📂 Project Structure

```text
road-damage-detector/
│
├── backend/
│   ├── main.py
│   ├── detector.py
│   └── database.py
│
├── frontend/
│   ├── detect_image.py
│   ├── detect_video.py
│   ├── analytics.py
│   └── map_dashboard.py
│
├── app.py
├── requirements.txt
├── render.yaml
└── README.md
```

---

## ⚙️ Local Setup

### Clone Repository

```bash
git clone https://github.com/Aniket-8314/Road-damage-detector.git
cd Road-damage-detector
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn backend.main:app --reload
```

### Run Frontend

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

* Real-time drone footage analysis
* Mobile application integration
* Road condition prediction
* Multi-class damage categorization
* Automated municipal reporting system

---

## 👨‍💻 Author

**Aniket**

Passionate about AI, Computer Vision, Backend Development, and Building Real-World Solutions.

GitHub: https://github.com/Aniket-8314
