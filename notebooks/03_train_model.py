from ultralytics import YOLO
import yaml
import json
from datetime import datetime
 
model = YOLO('yolov8n.pt')
 
results = model.train(
    data='dataset/data.yaml',
    epochs=100,
    imgsz=640,
    batch=16,
    lr0=0.01,           
    lrf=0.01,
    momentum=0.937,
    weight_decay=0.0005,
    warmup_epochs=3,
    augment=True,
    flipud=0.0,
    fliplr=0.5,
    mosaic=1.0,
    degrees=10,
    translate=0.1,
    scale=0.5,
    shear=2.0,
    perspective=0.0,
    hsv_h=0.015,
    hsv_s=0.7,
    hsv_v=0.4,
    project='runs/detect',
    name='road_damage_v1',
    exist_ok=False,
    verbose=True
)
 
metrics = {
    'run_name': 'road_damage_v1',
    'timestamp': datetime.now().isoformat(),
    'epochs': 100,
    'imgsz': 640,
    'batch': 16,
    'mAP50': float(results.results_dict.get('metrics/mAP50(B)', 0)),
    'mAP50_95': float(results.results_dict.get('metrics/mAP50-95(B)', 0)),
    'precision': float(results.results_dict.get('metrics/precision(B)', 0)),
    'recall': float(results.results_dict.get('metrics/recall(B)', 0)),
}
 
log_path = 'docs/training_log.json'
try:
    with open(log_path) as f:
        log = json.load(f)
except:
    log = []
 
log.append(metrics)
with open(log_path, 'w') as f:
    json.dump(log, f, indent=2)
 
print('\n Training Complete :-')
print(f'mAP@0.5:     {metrics["mAP50"]:.4f}')
print(f'mAP@0.5:0.95:{metrics["mAP50_95"]:.4f}')
print(f'Precision:   {metrics["precision"]:.4f}')
print(f'Recall:      {metrics["recall"]:.4f}')
print(f'Best model:  runs/detect/road_damage_v1/weights/best.pt')
