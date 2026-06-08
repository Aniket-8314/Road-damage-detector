from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io
from pathlib import Path
 
MODEL_PATH = 'models/best.pt'
 
_model = None
 
def get_model():
    global _model
    if _model is None:
        _model = YOLO(MODEL_PATH)
    return _model
 
 
def compute_severity(area_pct: float) -> str:
    if area_pct > 5.0:
        return 'Severe'
    elif area_pct > 2.0:
        return 'Moderate'
    return 'Minor'
 
 
def run_detection(image_bytes: bytes, conf: float = 0.25):
    """
    Run YOLO detection on raw image bytes.
    Returns: (annotated_image_bytes, list_of_detections)
    """
    model = get_model()
 
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError('Could not decode image')
 
    img_h, img_w = img.shape[:2]
    img_area = img_h * img_w
 
    results = model(img, conf=conf, verbose=False)
    result = results[0]
 
    detections = []
    for box in result.boxes:
        class_id   = int(box.cls[0])
        confidence = float(box.conf[0])
        x1, y1, x2, y2 = [round(float(v), 1) for v in box.xyxy[0]]
 
        area    = (x2 - x1) * (y2 - y1)
        area_pct = round(area / img_area * 100, 2)
 
        detections.append({
            'class_name': model.names[class_id],
            'confidence': round(confidence, 3),
            'bbox': [x1, y1, x2, y2],
            'severity': compute_severity(area_pct),
            'area_pct': area_pct,
        })
 
    annotated = result.plot()
    _, buf = cv2.imencode('.jpg', annotated)
    annotated_bytes = buf.tobytes()
 
    return annotated_bytes, detections