# System Libraries
import os

# Third-Party Libraries
from ultralytics import YOLO
from PIL import Image


class YoloClassifier:
    def __init__(self):
        self.model = YOLO('models/yolo/yolov8n-met-nmet-100-epoc.pt')

    def classify(self, pil_image: Image.Image) -> Image.Image:
        results = self.model([pil_image], conf=0.4)
        for result in results:
            temp_folder = os.path.join(os.getcwd(), "data/temp")
            if not os.path.exists(temp_folder):
                os.makedirs(temp_folder)

            plot_path = os.path.join(temp_folder, 'plot.png')
            result.save(plot_path)
            return Image.open(plot_path)