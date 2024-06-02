import os
from ultralytics import YOLO
from PIL import Image

class ClassifyYolo:    
    
    def classify(self, image):        
        model = YOLO("models/yolo/yolov8-custom-50-epoc.pt")
    
        results = model([image])
        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
            obb = result.obb  # Oriented boxes object for OBB outputs
            HOME = os.getcwd()
            temp_folder = os.path.join(HOME, "data/temp")        
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)            
            plot_path = os.path.join(temp_folder, 'plot.png')
            result.save(plot_path)
            return Image.open(plot_path)
        