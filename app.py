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


def resize_images(images_to_resize, new_height=640, new_width=640):
    if images_to_resize is None or not images_to_resize:
        raise ValueError("Please select at least one image file to resize!")

    home = os.getcwd()
    output_folder = os.path.join(home, "data/resized_images")

    if new_height < 640:
        new_height = 640
    elif new_height > 1500:
        new_height = 1500

    if new_width < 640:
        new_width = 640
    elif new_width > 1500:
        new_width = 1500

    image_processor = ImageProcessor()
    saved, message, skipped_files = image_processor.resize_and_save(
        images_to_resize, output_folder, new_width, new_height
    )

    if saved == True:
        log_message("info", message, skipped_files)

    if saved == False:
        log_message("error", message, skipped_files)    

    return sp.get_string("resized_success_html")


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
    background_fill_primary="*primary_50",
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
            images_to_resize = gr.Files(
                file_types=[extension.value for extension in ImageExtension]
            )
            result = RichTextbox(label="Result", scale=1)
        resize_button = gr.DownloadButton(label="Resize", variant="primary")

    detect_yolo_button.click(
        detect_yolo_and_classify,
        inputs=image_for_yolo,
        outputs=detected_yolo_object_image,
    )
    detect_cnn_button.click(
        detect_cnn_and_classify, inputs=image_for_cnn, outputs=detected_cnn_object_image
    )
    resize_button.click(
        resize_images,
        inputs=[images_to_resize, image_height, image_width],
        outputs=result,
    )

    gr.Markdown(sp.get_string("group_markdown"))
    gr.Markdown(sp.get_string("group_members"))

if __name__ == "__main__":
    demo.launch()
