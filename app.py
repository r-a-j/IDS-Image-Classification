import gradio as gr
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

from src.data_preprocessing import resize_image
from src.object_detection import detect_objects, extract_boxes_and_classes, draw_boxes
from src.object_classification import classifier

def detect_and_classify(image):
    
    # Step 1: Data Preprocessing
    #resized_image = resize_image(image)
    resized_image = image
    
    # Step 2: Object Detection
    detections = detect_objects(resized_image, )
    boxes, classes = extract_boxes_and_classes(detections)
    annotated_image = draw_boxes(resized_image, boxes, classes)

    # Step 3: Object Classification
    classification_results = []
    for box, _ in zip(boxes, classes):
        # Extract region of interest from the image
        x_min, y_min, x_max, y_max = [int(coord * 224) for coord in box]  # Adjust to classifier input size
        roi = resized_image[y_min:y_max, x_min:x_max]

        # Perform classification
        prediction = classifier.predict(np.expand_dims(roi, axis=0))

        # Append classification result to list
        classification_results.append(prediction)

    return annotated_image, classification_results

iface = gr.Interface(
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
    iface.launch()