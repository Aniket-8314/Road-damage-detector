from ultralytics import YOLO
import cv2
import os
 
model = YOLO('runs/detect/runs/detect/road_damage_v1-2/weights/best.pt')
 
def detect_image(image_path, save_path=None):
    results = model(image_path, conf=0.25)
    result = results[0]
 
    detections = []
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])
        bbox = box.xyxy[0].tolist()
        class_name = model.names[class_id]
 
        area = (bbox[2]-bbox[0]) * (bbox[3]-bbox[1])
        img_area = result.orig_shape[0] * result.orig_shape[1]
        area_pct = area / img_area
 
        if area_pct > 0.05:
            severity = 'Severe'
        elif area_pct > 0.02:
            severity = 'Moderate'
        else:
            severity = 'Minor'
 
        detections.append({
            'class': class_name,
            'confidence': round(confidence, 3),
            'bbox': [round(x, 1) for x in bbox],
            'severity': severity,
            'area_pct': round(area_pct * 100, 2)
        })
 
    if save_path:
        annotated = result.plot()
        cv2.imwrite(save_path, annotated)
 
    return detections
 
test_images = os.listdir('dataset/images/test')[:5]
for img in test_images:
    path = f'dataset/images/test/{img}'
    results = detect_image(path, save_path=f'demo/{img}')
    print(f'\n{img}:')
    for d in results:
        print(f'  {d["class"]:10} conf={d["confidence"]}  severity={d["severity"]}')