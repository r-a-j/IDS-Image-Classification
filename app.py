from cProfile import label
import os
import gradio as gr
from src.ImageProcessor import ImageProcessor
from src.utils.StringProcessor import StringProcessor
from src.ClusteringAlgorithm import ClusteringAlgorithm
from src.utils.ImageExtension import ImageExtension

def detect_and_classify(image):
    
    if(image == None):
        gr.Warning(message="Please select image to classify!")
    else:
        classes = 5
        
        ca = ClusteringAlgorithm()
        k_means_img_result = ca.k_means(image, classes)
        
        return k_means_img_result            

def resize_images(images_to_resize, new_height = 640, new_width = 640):
    
    if new_height < 640:
        new_height = 640
        
    if new_width < 640:
        new_width = 640
        
    if new_height > 1500:
        new_height = 1500
        
    if new_width > 1500:
        new_width = 1500
    
    if images_to_resize is None:        
        gr.Warning(message="Please select atleast one image file to resize!")
    else:
        HOME = os.getcwd()
        output_folder = os.path.join(HOME, "data/resized_images")
        
        image_processor = ImageProcessor()
        success, message, skippedFiles = image_processor.resize_and_save(
            images_to_resize, 
            output_folder, 
            new_width, 
            new_height)
        
        return f"Message{': '.join(message)} \n Skipped Files{': '.join(skippedFiles)}"

theme = gr.themes.Base(
    primary_hue = "purple",
    secondary_hue = "violet",
    font_mono = [
        'IBM Plex Mono', 
        'ui-monospace', 
        gr.themes.GoogleFont('Consolas'), 
        'monospace'],
).set(
    background_fill_primary = '*primary_50',
    button_shadow = '*shadow_drop',
    button_shadow_active = '*block_label_shadow'
)

with gr.Blocks(theme=theme) as demo:
    
    sp = StringProcessor()
    gr.Markdown(sp.get_string("company_logo_url_markdown"))
    with gr.Tab("Classify object"):
        with gr.Row():
            image = gr.Image(
                type = "pil", 
                label = "Upload Image")
            detected_object_image = gr.Image(
                type = "pil", 
                label = "Detected object", 
                height = image.height, 
                width = image.width)
        detect_button = gr.Button("Detect", variant="primary")
    
    with gr.Tab("Resize images"):
        with gr.Row():
            image_height = gr.Number(label="Image height in px", value=640, scale=1)
            image_width = gr.Number(label="Image width in px", value=640, scale=1)
        with gr.Row():
            images_to_resize = gr.Files(file_types=[extension.value for extension in ImageExtension])
            result = gr.Text(label="Result",scale=1)
        resize_button = gr.DownloadButton("Resize", variant="primary")    
        
    detect_button.click(detect_and_classify, inputs=image, outputs=detected_object_image)
    resize_button.click(resize_images, inputs=[images_to_resize, image_height, image_width], outputs=result)   
    
    gr.Markdown(sp.get_string("group_markdown"))
    gr.Markdown("Ananya Pal, Harsh Yadav, Trung Quy Duc Huynh, Saptarsi Bhattacharya, Purvanshi Sharma, Raj Anilbhai Pawar")

if __name__ == '__main__':
    demo.launch()
