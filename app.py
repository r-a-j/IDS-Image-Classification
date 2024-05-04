import gradio as gr
from src.resize_images import resize_images

def detect_and_classify(image):
    
    # Train

    # Detect
    
    # Classify

    return image, "Metal/Non Metal", "Success"

def resize_images(images_to_resize):
    return "Success..."

with gr.Blocks() as demo:
    
    gr.Markdown("# Industrial Data Science 2")
    gr.Markdown(f'<img src="https://partikel-art.de/wp-content/uploads/2024/03/Partikelart_Logo_header_n-1024x402.png" alt="drawing" height="73" width="186"/>')
    with gr.Tab("Classify image"):
        gr.Markdown("### Detect object")
        with gr.Row():
            image = gr.Image(type="pil", label="Upload Image")
            detected_object_image = gr.Image(type="pil", label="Detected object")
        image_button = gr.Button("Detect")
    
    with gr.Tab("Resize images"):
        with gr.Row():
            images_to_resize = gr.Files(file_types=['.jpg', '.jpeg', '.png'])
            result = gr.Image()
        image_button = gr.Button("Resize")

    image_button.click(detect_and_classify, inputs=image, outputs=detected_object_image)
    image_button.click(resize_images, inputs=images_to_resize, outputs=result)

# interface = gr.Interface(
#     fn=detect_and_classify,
#     inputs=[
#         gr.Image(type="pil", label="Upload Image"),
#         gr.Files(file_types=['.jpg', '.jpeg', '.png'])
#     ],
#     outputs=[
#         gr.Image(type="pil", label="Detected object"),
#         gr.Label(label="Classification")
#     ],
#     title="",
#     description="Upload an image to detect and classify objects"
# )

if __name__ == '__main__':
#     interface.launch()
    demo.launch()