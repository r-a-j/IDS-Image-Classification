# System Libraries
import os

# Third-Party Libraries
import cv2

# Image Processing Libraries
import numpy as np

# Local Imports
from src.utils.ImageExtension import ImageExtension


class ImageProcessor:
    def __init__(self):
        pass

    @staticmethod
    def round_to_multiple(number, base):
        return base * round(int(number) / base)

    def resize_and_save(self, images_to_resize, output_folder, new_width, new_height):
        skipped_list = []
        message = []

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        new_width = self.round_to_multiple(new_width, 128)
        new_height = self.round_to_multiple(new_height, 128)

        for image_path in images_to_resize:
            if any(image_path.endswith(ext.value) for ext in ImageExtension):
                success = self._process_image(image_path, output_folder, new_width, new_height, message)
                if not success:
                    skipped_list.append(f"Error processing {image_path}. Skipping.")

        return True, message, skipped_list

    @staticmethod
    def _process_image(image_path, output_folder, new_width, new_height, message):
        image = cv2.imread(image_path)
        if image is None:
            return False

        resize_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

        filename = os.path.basename(image_path)
        output_path = os.path.join(output_folder, filename)

        # Ensure output_path is a string
        isinstance(output_path, str), f"Expected string but got {type(output_path)}"

        # Ensure resize_image is ndarray
        isinstance(resize_image, np.ndarray), f"Expected ndarray but got {type(resize_image)}"

        # Save resized image
        cv2.imwrite(output_path, resize_image)

        message.append(f"Resized and saved to: {output_path}")
        
        return True
