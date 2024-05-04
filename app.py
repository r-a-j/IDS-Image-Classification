import gradio as gr
from gradio.components import download_button
from src.resize_images import resize_images

def detect_and_classify(image):
    
    # Train

    # Detect
    
    # Classify

    return image

def resize_images(images_to_resize):
    return images_to_resize

with gr.Blocks() as demo:
    
    gr.Markdown("# Industrial Data Science 2 - Group 3")
    gr.Markdown(f'<img src="https://partikel-art.de/wp-content/uploads/2024/03/Partikelart_Logo_header_n-1024x402.png" alt="PartikelART" height="73" width="186"/>')
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
            result = gr.Files(file_count="multiple")
        resize_button = gr.DownloadButton("Resize", variant="primary")    
    
    detect_button.click(detect_and_classify, inputs=image, outputs=detected_object_image)
    resize_button.click(resize_images, inputs=images_to_resize, outputs=result)
    
    gr.Markdown("### Group Members")
    gr.Markdown("###### Ananya Pal, Harsh Yadav, Trung Quy Duc Huynh, Saptarsi Bhattacharya, Purvanshi Sharma, Raj Anilbhai Pawar")

if __name__ == '__main__':
    demo.launch()
    
    # gr.DownloadButton("Download", link="/file=material/test.txt")
    # demo.launch(allowed_paths=["material/"])