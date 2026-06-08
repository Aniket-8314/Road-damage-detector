import os
import cv2
import matplotlib.pyplot as plt
 
def verify_dataset(img_dir, label_dir, num_samples=5):
    images = os.listdir(img_dir)[:num_samples]
    fig, axes = plt.subplots(1, len(images), figsize=(20, 4))
 
    for i, img_name in enumerate(images):
        img_path = os.path.join(img_dir, img_name)
        label_path = os.path.join(label_dir, img_name.replace('.jpg', '.txt'))
 
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w = img.shape[:2]
 
        # Draw bounding boxes
        if os.path.exists(label_path):
            with open(label_path) as f:
                for line in f.readlines():
                    cls, cx, cy, bw, bh = map(float, line.strip().split())
                    x1 = int((cx - bw/2) * w)
                    y1 = int((cy - bh/2) * h)
                    x2 = int((cx + bw/2) * w)
                    y2 = int((cy + bh/2) * h)
                    color = (255, 0, 0) if cls == 0 else (0, 255, 0)
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
        axes[i].imshow(img)
        axes[i].axis('off')
 
    plt.tight_layout()
    plt.savefig('docs/dataset_preview.png')
    print('Saved preview to docs/dataset_preview.png')
 
verify_dataset('dataset/images/train', 'dataset/labels/train')