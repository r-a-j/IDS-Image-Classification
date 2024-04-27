import gradio as gr
import PIL.Image as Image

def detect_object(image):
    return image

iface = gr.Interface(
    fn=detect_object,
    inputs=[
        gr.Image(type="pil", label="Upload Image")        
    ],
    outputs=gr.Image(type="pil", label="Detected object"),
    title="PartikelART Image Classification",
    description="Laden Sie ein Bild eines kleinen Schrott/Faserobjekts zur Erkennung hoch!",
    examples=[
        ["assets/239_170_2012_Verpacken_Progress_Met.jpg", "Metallobjekt"],
        ["assets/354_186_2015_Kontakt_Oechsler_NM.jpg", "Nichtmetall"]        
    ]    
)

if __name__ == '__main__':
    iface.launch()