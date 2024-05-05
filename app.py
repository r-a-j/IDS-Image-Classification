import gradio as gr
from gradio.components import download_button
from src.resize_images import resize_images
from src.utils.read_strings import get_string
from src.k_means import k_means

def detect_and_classify(image):           
    
    if(image == None):        
        gr.Warning(message="Please select image to classify!")
    else:
        classes = 5
        k_means_img_result = k_means(image, classes)
        return k_means_img_result            

def resize_images(images_to_resize):
    
    if(images_to_resize == None):        
        gr.Warning(message="Please select atleast one image file to resize!")
    else:
        return "Saved to folder: resized_images"

theme = gr.themes.Base(
    primary_hue="purple",
    secondary_hue="violet",
    font_mono=['IBM Plex Mono', 'ui-monospace', gr.themes.GoogleFont('Consolas'), 'monospace'],
).set(
    background_fill_primary='*primary_50',
    button_shadow='*shadow_drop',
    button_shadow_active='*block_label_shadow'
)

with gr.Blocks(theme=theme) as demo:
    
    gr.Markdown(get_string("company_logo_url_markdown"))    
    with gr.Tab("Classify object"):
        with gr.Row():
            image = gr.Image(
                type="pil", 
                label="Upload Image")
            detected_object_image = gr.Image(
                type="pil", 
                label="Detected object", 
                height=image.height, 
                width=image.width)
        detect_button = gr.Button("Detect", variant="primary")
    
    with gr.Tab("Resize images"):
        with gr.Row():
            images_to_resize = gr.Files(file_types=['.jpg', '.jpeg', '.png'])
            result = gr.Text(label="Result",scale=1)
        resize_button = gr.DownloadButton("Resize", variant="primary")    
    
    detect_button.click(detect_and_classify, inputs=image, outputs=detected_object_image)
    resize_button.click(resize_images, inputs=images_to_resize, outputs=result)   
    
    gr.Markdown(get_string("group_markdown"))
    gr.Markdown("Ananya Pal, Harsh Yadav, Trung Quy Duc Huynh, Saptarsi Bhattacharya, Purvanshi Sharma, Raj Anilbhai Pawar")

if __name__ == '__main__':
    demo.launch()
