import os
import cv2
from src.utils.ImageExtension import ImageExtension

class ImageProcessor:
    
    def round_to_multiple(self, number, base):
        return base * round(int(number) / base)
    
    def resize_and_save(self, images_to_resize, output_folder, new_width, new_height):
        
        skippedList = []
        message = []

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            
        new_width = self.round_to_multiple(new_width, 128)
        new_height = self.round_to_multiple(new_height, 128)
        
        for image_path in images_to_resize:
            
            if any(image_path.endswith(ext.value) for ext in ImageExtension):
                
                image = cv2.imread(image_path)
                if image is None:
                    skippedList.append(f"Error reading {image_path}. Skipping.")
                    continue
                

                resize_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)
                                
                filename = os.path.basename(image_path)
                output_path = os.path.join(output_folder, filename)
                
                cv2.imwrite(output_path, resize_image)
                message.append(f"Resized and saved to: {output_path}")

        return True, message, skippedList