# System Libraries
import os

# Third-Party Libraries
import cv2
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
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
        if not isinstance(output_path, str):
            raise ValueError(f"Expected string for output_path, got {type(output_path)}")

        # Ensure resize_image is ndarray
        if not isinstance(resize_image, np.ndarray):
            raise ValueError(f"Expected ndarray for resize_image, got {type(resize_image)}")

        # Save resized image
        cv2.imwrite(output_path, resize_image)

        message.append(f"Resized and saved to: {output_path}")

        return True

    @staticmethod
    def augment_image(image_path, output_folder, augmentations):
        try:
            image = Image.open(image_path)
        except IOError:
            return False

        filename = os.path.basename(image_path)
        name, ext = os.path.splitext(filename)

        for i, augmentation in enumerate(augmentations):
            augmented_image = augmentation(image)
            augmented_filename = f"{name}_aug_{i}{ext}"
            augmented_image.save(os.path.join(output_folder, augmented_filename))

        return True

    @staticmethod
    def resize_image(image, size):
        return image.resize(size, Image.LANCZOS)

    @staticmethod
    def transpose_image(image, method):
        return image.transpose(method)

    @staticmethod
    def rotate_image(image, angle):
        return image.rotate(angle, expand=True)

    @staticmethod
    def crop_image(image, box):
        return image.crop(box)

    @staticmethod
    def convert_image(image, mode):
        return image.convert(mode)

    @staticmethod
    def enhance_image(image, enhancement_type, factor):
        enhancer_dict = {
            'color': ImageEnhance.Color,
            'contrast': ImageEnhance.Contrast,
            'brightness': ImageEnhance.Brightness,
            'sharpness': ImageEnhance.Sharpness
        }

        if enhancement_type in enhancer_dict:
            enhancer = enhancer_dict[enhancement_type](image)
            return enhancer.enhance(factor)
        else:
            raise ValueError(f"Enhancement type {enhancement_type} not recognized.")

    @staticmethod
    def add_padding(image, padding_size, fill_color=(0, 0, 0)):
        return ImageOps.expand(image, border=padding_size, fill=fill_color)

    @staticmethod
    def add_noise(image, noise_type='gaussian'):
        image_array = np.asarray(image)
        if noise_type == 'gaussian':
            mean = 0
            std = 0.1
            gaussian_noise = np.random.normal(mean, std, image_array.shape).astype('uint8')
            noisy_image = Image.fromarray(cv2.add(image_array, gaussian_noise))
        else:
            raise ValueError(f"Noise type {noise_type} not recognized.")
        return noisy_image

    @staticmethod
    def blur_image(image, radius):
        return image.filter(ImageFilter.GaussianBlur(radius))

    @staticmethod
    def shear_image(image, shear_factor):
        width, height = image.size
        xshift = abs(shear_factor) * width
        new_width = width + int(round(xshift))
        image = image.transform(
            (new_width, height),
            Image.AFFINE,
            (1, shear_factor, -xshift if shear_factor > 0 else 0, 0, 1, 0),
            Image.BICUBIC,
        )
        return image

    @staticmethod
    def change_hue(image, hue_factor):
        image = image.convert('RGB')  # Convert to RGB before converting to HSV
        image_array = np.array(image)
        image_hsv = cv2.cvtColor(image_array, cv2.COLOR_RGB2HSV)
    
        # Modify the hue channel
        image_hsv[:, :, 0] = (image_hsv[:, :, 0] + hue_factor) % 180
    
        image_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
        return Image.fromarray(image_rgb, 'RGB')


    @staticmethod
    def cutout(image, cutout_size):
        image_array = np.array(image)
        h, w, _ = image_array.shape
        y = np.random.randint(h)
        x = np.random.randint(w)
        y1 = np.clip(y - cutout_size // 2, 0, h)
        y2 = np.clip(y + cutout_size // 2, 0, h)
        x1 = np.clip(x - cutout_size // 2, 0, w)
        x2 = np.clip(x + cutout_size // 2, 0, w)
        image_array[y1:y2, x1:x2, :] = 0
        return Image.fromarray(image_array)

    @staticmethod
    def mosaic(images, output_size):
        num_images = len(images)
        images = [Image.open(img) for img in images]
        mosaic_image = Image.new('RGB', (output_size * num_images, output_size))
        for i, img in enumerate(images):
            img = img.resize((output_size, output_size))
            mosaic_image.paste(img, (i * output_size, 0))
        return mosaic_image

# Example usage
image_paths = ["path/to/image1.jpg", "path/to/image2.jpg"]
output_folder = "path/to/output_folder"

# Define the augmentations you want to apply
augmentations = [
    lambda img: ImageProcessor.resize_image(img, (256, 256)),
    lambda img: ImageProcessor.transpose_image(img, Image.FLIP_LEFT_RIGHT),
    lambda img: ImageProcessor.rotate_image(img, 45),
    lambda img: ImageProcessor.crop_image(img, (10, 10, 200, 200)),
    lambda img: ImageProcessor.convert_image(img, 'L'),
    lambda img: ImageProcessor.enhance_image(img, 'contrast', 3.0),
    lambda img: ImageProcessor.add_padding(img, padding_size=20),
    lambda img: ImageProcessor.add_noise(img, 'gaussian'),
    lambda img: ImageProcessor.blur_image(img, radius=2),
    lambda img: ImageProcessor.shear_image(img, 0.2),
    lambda img: ImageProcessor.change_hue(img, 100),
    lambda img: ImageProcessor.cutout(img, cutout_size=50),
    lambda img: ImageProcessor.mosaic(image_paths, output_size=128)
]

processor = ImageProcessor()
for image_path in image_paths:
    processor.augment_image(image_path, output_folder, augmentations)
