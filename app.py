# System Libraries
import os

# Third-Party Libraries
import gradio as gr
from gradio_rich_textbox import RichTextbox

# Project-Specific Imports
from src.ImageProcessor import ImageProcessor
from src.utils.StringProcessor import StringProcessor
from src.ClusteringAlgorithm import ClusteringAlgorithm
from src.ClassifyYolo import YoloClassifier
from src.utils.ImageExtension import ImageExtension
from src.ClassifyCnn import CnnClassifier

# Image Processing Libraries
from PIL import Image

def kmeans_cluster(pil_image):
    if pil_image is None:
        gr.Warning(message="Please select image to cluster!")
    else:
        classes = 5
        ca = ClusteringAlgorithm()
        k_means_img_result = ca.k_means(pil_image, classes)
        return k_means_img_result

def detect_yolo_and_classify(pil_image: Image.Image) -> Image.Image:
    if pil_image is None:
        raise ValueError("Please select an image to classify!")
    else:
        classifier = YoloClassifier()
        output_image = classifier.classify(pil_image)
        return output_image

def detect_cnn_and_classify(pil_image: Image.Image) -> Image.Image:
    if pil_image is None:
        raise ValueError("Please select an image to classify!")
    else:
        classifier = CnnClassifier()
        output_image = classifier.segment_and_draw_bounding_box(pil_image)
        return output_image

def create_message(message, skipped_files):
    return f"Message: {' '.join(message)}\nSkipped Files: {' '.join(skipped_files)}"

def log_message(message_type, message, skipped_files):
    formatted_message = create_message(message, skipped_files)
    if message_type == "info":
        gr.Info(formatted_message)
    elif message_type == "error":
        gr.Error(formatted_message)
    else:
        raise ValueError("Invalid message_type")

def resize_images(images_to_resize, new_height, new_width):
    if images_to_resize is None or not images_to_resize:
        raise ValueError("Please select at least one image file to resize!")

    home = os.getcwd()
    output_folder = os.path.join(home, "data/resized_images")

    if new_height < 128:
        new_height = 128
    elif new_height > 2560:
        new_height = 2560

    if new_width < 128:
        new_width = 128
    elif new_width > 2560:
        new_width = 2560

    image_processor = ImageProcessor()
    saved, message, skipped_files = image_processor.resize_and_save(images_to_resize, 
                                                                    output_folder, 
                                                                    new_width, 
                                                                    new_height)

    if saved:
        log_message("info", message, skipped_files)

    if not saved:
        log_message("error", message, skipped_files)

    return sp.get_string("resized_success_html")

def apply_augmentations(images_to_augment, augmentations, image_height, image_width):
    if images_to_augment is None or not images_to_augment:
        raise ValueError("Please select at least one image file to augment!")

    home = os.getcwd()
    output_folder = os.path.join(home, "data/augmented_images")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    augmentations_map = {
        'Resize': lambda img: ImageProcessor.resize_image(img, (image_width, image_height)),
        'Flip Horizontal': lambda img: ImageProcessor.transpose_image(img, Image.FLIP_LEFT_RIGHT),
        'Flip Vertical': lambda img: ImageProcessor.transpose_image(img, Image.FLIP_TOP_BOTTOM),
        'Rotate': lambda img: ImageProcessor.rotate_image(img, 45),  # You can allow custom angles
        'Crop': lambda img: ImageProcessor.crop_image(img, (10, 10, image_width - 10, image_height - 10)),
        'Grayscale': lambda img: ImageProcessor.convert_image(img, 'L'),
        'Enhance Contrast': lambda img: ImageProcessor.enhance_image(img, 'contrast', 2.0),
        'Enhance Brightness': lambda img: ImageProcessor.enhance_image(img, 'brightness', 2.0),
        'Enhance Color': lambda img: ImageProcessor.enhance_image(img, 'color', 2.0),
        'Enhance Sharpness': lambda img: ImageProcessor.enhance_image(img, 'sharpness', 2.0),
        'Add Padding': lambda img: ImageProcessor.add_padding(img, 20),
        'Add Noise': lambda img: ImageProcessor.add_noise(img, 'gaussian'),
        'Blur': lambda img: ImageProcessor.blur_image(img, 2),
        'Shear': lambda img: ImageProcessor.shear_image(img, 0.2),
        'Change Hue': lambda img: ImageProcessor.change_hue(img, 100),
        'Cutout': lambda img: ImageProcessor.cutout(img, 50),
        'Mosaic': lambda img: ImageProcessor.mosaic(images_to_augment, 128)  # This requires multiple images
    }

    selected_augmentations = [augmentations_map[aug] for aug in augmentations]

    image_processor = ImageProcessor()
    messages = []

    for image_path in images_to_augment:
        success = image_processor.augment_image(image_path, output_folder, selected_augmentations)
        if success:
            messages.append(f"Augmented and saved to: {output_folder}")

    return "\n".join(messages)

# Define the custom theme
theme = gr.themes.Base(
    primary_hue="purple",
    secondary_hue="violet",
    font_mono=[
        "IBM Plex Mono",
        "ui-monospace",
        gr.themes.GoogleFont("Consolas"),
        "monospace",
    ],
).set(
    button_shadow="*shadow_drop",
    button_shadow_active="*block_label_shadow",
)

with gr.Blocks(theme=theme) as demo:
    sp = StringProcessor()
    gr.Markdown(sp.get_string("company_logo_url_markdown"))

    with gr.Tab("Classify with Yolo"):
        with gr.Row():
            image_for_yolo = gr.Image(type="pil", label="Upload Image")
            detected_yolo_object_image = gr.Image(
                type="pil",
                label="Detected object with Yolo",
                height=image_for_yolo.height,
                width=image_for_yolo.width,
            )
        detect_yolo_button = gr.Button("Detect", variant="primary")

    with gr.Tab("Classify with CNN"):
        with gr.Row():
            image_for_cnn = gr.Image(type="pil", label="Upload Image")
            detected_cnn_object_image = gr.Image(
                type="pil",
                label="Detected object with CNN",
                height=image_for_cnn.height,
                width=image_for_cnn.width,
            )
        detect_cnn_button = gr.Button("Detect", variant="primary")

    with gr.Tab("Data Augmentation"):
        with gr.Row():
            image_height = gr.Number(label="Image height in px", value=640, scale=1)
            image_width = gr.Number(label="Image width in px", value=640, scale=1)
        with gr.Row():
            images_to_augment = gr.Files(
                file_types=[extension.value for extension in ImageExtension]
            )
            result = RichTextbox(label="Result", scale=1)
        with gr.Row():
            augmentations = gr.CheckboxGroup(label="Select Augmentations", choices=[
                'Resize', 'Flip Horizontal', 'Flip Vertical', 'Rotate', 'Crop', 'Grayscale',
                'Enhance Contrast', 'Enhance Brightness', 'Enhance Color', 'Enhance Sharpness',
                'Add Padding', 'Add Noise', 'Blur', 'Shear', 'Change Hue', 'Cutout', 'Mosaic'
            ])
        augment_button = gr.Button("Apply Augmentations", variant="primary")

    detect_yolo_button.click(
        detect_yolo_and_classify,
        inputs=image_for_yolo,
        outputs=detected_yolo_object_image,
    )
    detect_cnn_button.click(
        detect_cnn_and_classify, inputs=image_for_cnn, outputs=detected_cnn_object_image
    )
    augment_button.click(
        apply_augmentations,
        inputs=[images_to_augment, augmentations, image_height, image_width],
        outputs=result,
    )

    gr.Markdown(sp.get_string("subject_info_markdown"))

if __name__ == "__main__":
    demo.launch()
