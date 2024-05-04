import os
import cv2
from src.utils.image_extensions import ImageExtension
    
def resize_images(input_folder, output_folder, new_width, new_height):
        
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        
        if any(filename.endswith(ext.value) for ext in ImageExtension):
            
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error reading {filename}. Skipping.")
                continue
            
            resize_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
            
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, resize_image)
            print(f"Resized and saved: {output_path}")