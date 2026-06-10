from fastapi import FastAPI, File, UploadFile, Depends, Form
from fastapi.responses import JSONResponse, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional
import base64
import os
 
from .detector import run_detection
from .database import get_db, Detection, create_tables
 
 
app = FastAPI(
    title='Road Damage Detection API',
    description='Detect potholes and road cracks using YOLOv8',
    version='1.0.0'
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)
 
@app.on_event('startup')
def startup():
    # create_tables()
    pass
 
 
@app.get('/')
def root():
    return {'status': 'ok', 'model': 'YOLOv8 Road Damage Detector'}
 
@app.get('/health')
def health():
    return {'status': 'healthy'}
 
@app.post('/detect')
async def detect(
    file: UploadFile = File(...),
    latitude: Optional[float] = Form(None),
    longitude: Optional[float] = Form(None),
    conf: float = Form(0.25),
    db: Session = Depends(get_db)
):
    """
    Upload a road image and get back detection results.
    Optionally include GPS coordinates.
    """
    # Read uploaded file
    image_bytes = await file.read()
 
    try:
        annotated_bytes, detections = run_detection(image_bytes, conf=conf)
    except ValueError as e:
        return JSONResponse(status_code=400, content={'error': str(e)})
 
    for det in detections:
        record = Detection(
            image_name = file.filename,
            latitude   = latitude,
            longitude  = longitude,
            class_name = det['class_name'],
            confidence = det['confidence'],
            severity   = det['severity'],
            area_pct   = det['area_pct'],
        )
        db.add(record)
    db.commit()
 
    annotated_b64 = base64.b64encode(annotated_bytes).decode()
 
    return {
        'filename': file.filename,
        'detections': detections,
        'total_damage_count': len(detections),
        'annotated_image_b64': annotated_b64,
        'gps': {'latitude': latitude, 'longitude': longitude}
    }
 
 
@app.get('/reports')
def get_reports(limit: int = 100, db: Session = Depends(get_db)):
    """Get recent detection reports for the dashboard.""",
    records = db.query(Detection).order_by(Detection.timestamp.desc()).limit(limit).all()
    return [
        {
            'id': r.id,
            'image_name': r.image_name,
            'latitude': r.latitude,
            'longitude': r.longitude,
            'class_name': r.class_name,
            'confidence': r.confidence,
            'severity': r.severity,
            'timestamp': r.timestamp.isoformat() if r.timestamp else None
        }
        for r in records
    ]

