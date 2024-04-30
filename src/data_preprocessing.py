from PIL import Image
import os

def resize_image(image_path, size=(224, 224)):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Image file '{image_path}' not found.")
    
    try:
        image = Image.open(image_path)
    except Exception as e:
        raise IOError(f"Error opening image '{image_path}': {e}")

    resized_image = image.resize(size)
    return resized_image
