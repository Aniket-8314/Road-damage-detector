from ultralytics import YOLO
 
model = YOLO('runs/detect/runs/detect/road_damage_v1/weights/best.pt')
 
metrics = model.val(
    data='dataset/data.yaml',
    split='test',
    conf=0.25,
    iou=0.45,
    plots=True
)
 
print('Per-class metrics:')
for i, name in model.names.items():
    print(f'  {name}: mAP50={metrics.box.maps[i]:.3f}')
