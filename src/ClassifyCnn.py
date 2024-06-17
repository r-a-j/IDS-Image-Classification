# System and Type Imports
import os

# Image Processing Libraries
import cv2
import numpy as np
from PIL import Image

# Machine Learning Frameworks
from keras.src.saving.saving_api import load_model


def preprocess_image(pil_image: Image.Image, img_size: int = 150) -> np.ndarray:
    img_array = np.array(pil_image.convert('L'))
    img_array = cv2.resize(img_array, (img_size, img_size))
    img_array = img_array.reshape(-1, img_size, img_size, 1)
    img_array = img_array / 255.0  # Normalize the image
    return img_array


def preprocess_image_for_segmentation(pil_image: Image.Image, img_size: int = 150) -> np.ndarray:
    img_array = np.array(pil_image)
    img_array = cv2.resize(img_array, (img_size, img_size))
    return img_array


class CnnClassifier:
    def __init__(self):
        self.model = load_model('models/cnn/cnn_metal_nonmetal_classifier_model.keras')

    def classify(self, pil_image: Image.Image) -> str:
        preprocessed_image = preprocess_image(pil_image)
        predictions = self.model.predict(preprocessed_image)
        predicted_class = np.argmax(predictions, axis=1)[0]
        categories = ["metal", "non-metal"]
        return categories[predicted_class]

    def segment_and_draw_bounding_box(self, pil_image: Image.Image) -> Image.Image:
        img_array = preprocess_image_for_segmentation(pil_image)

        _, binary_img = cv2.threshold(
            cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        contours = [
            contour for contour in contours if cv2.contourArea(contour) > 100
        ]

        img_color = img_array.copy()
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            color = (31, 119, 180)
            predicted_category = self.classify(pil_image)
            if predicted_category == "metal":
                color = (255, 127, 14)

            padding = 5
            x1, y1 = max(0, x - padding), max(0, y - padding)
            x2, y2 = min(img_array.shape[1], x + w + padding), min(
                img_array.shape[0], y + h + padding
            )
            cv2.rectangle(img_color, (x1, y1), (x2, y2), color, 1)

            preprocessed_image = preprocess_image(pil_image)
            predictions = self.model.predict(preprocessed_image)
            confidence = (
                predictions[0][0 if predicted_category == "metal" else 1] * 100
            )

            text = f"{predicted_category.capitalize()} ({confidence:.2f}%)"
            font_scale = 0.4
            font = cv2.FONT_HERSHEY_SIMPLEX
            (text_height), _ = cv2.getTextSize(text, font, font_scale, 1)
            text_x = x1 + 2
            text_y = y1 + text_height + 2
            cv2.putText(
                img_color, text, (text_x, text_y), font, font_scale, (0, 0, 0), 1
            )

        home = os.getcwd()
        temp_folder = os.path.join(home, "data/temp")
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        output_path = os.path.join(temp_folder, 'segmented_image.png')
        cv2.imwrite(output_path, img_color)

        return Image.open(output_path)