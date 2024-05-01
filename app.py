import gradio as gr

def detect_and_classify(image):
    return image, "Metal/Non Metal"

interface = gr.Interface(
    fn=detect_and_classify,
    inputs=[
        gr.Image(type="pil", label="Upload Image")        
    ],
    outputs=[
        gr.Image(type="pil", label="Detected object"),
        gr.Label(label="Classification")
    ],
    title="Object Detection and Classification",
    description="Upload an image to detect and classify objects"    
)

if __name__ == '__main__':
    interface.launch()