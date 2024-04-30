import tensorflow as tf
import numpy as np

# Load pre-trained YOLO model
yolo_model = tf.keras.models.load_model('path/to/yolo_model.h5')

def detect_objects(image):
    # Preprocess the image for YOLO model
    resized_image = tf.image.resize(image, (416, 416))
    resized_image = resized_image / 255.0  # Normalize pixel values to [0, 1]
    expanded_image = tf.expand_dims(resized_image, axis=0)

    # Perform object detection
    detections = yolo_model.predict(expanded_image)

    # Extract bounding boxes and class labels from YOLO output
    boxes, classes = extract_boxes_and_classes(detections)

    # Draw bounding boxes on the image
    annotated_image = draw_boxes(image, boxes, classes)

    return annotated_image

def extract_boxes_and_classes(detections, confidence_threshold=0.5):
    boxes = []
    classes = []
    
    # Iterate over each detection in the output
    for detection in detections:
        # Extract confidence score and class probabilities
        confidence_scores = detection[:, :, 4:5]
        class_probabilities = detection[:, :, 5:]

        # Filter detections based on confidence threshold
        scores = confidence_scores * class_probabilities
        scores = scores[scores >= confidence_threshold]

        # Get indices of non-zero elements
        indices = np.nonzero(scores)

        # Iterate over indices to extract bounding boxes and class labels
        for idx in zip(*indices):
            box = detection[idx[0], idx[1], :4]
            class_index = np.argmax(detection[idx[0], idx[1], 5:])
            confidence = detection[idx[0], idx[1], 4]
            if confidence > confidence_threshold:
                boxes.append(box)
                classes.append(class_index)
    
    return boxes, classes

def draw_boxes(image, boxes, classes):
    annotated_image = image.copy()
    height, width, _ = image.shape
    
    # Define colors for different classes
    class_colors = {
        0: (255, 0, 0),   # Class 0 (e.g., person) - Red
        1: (0, 255, 0),   # Class 1 (e.g., car) - Green
        # Add more colors for additional classes as needed
    }
    
    # Iterate over each bounding box and draw it on the image
    for box, class_index in zip(boxes, classes):
        # Extract box coordinates
        x_min, y_min, x_max, y_max = box
        
        # Convert box coordinates from relative to absolute
        x_min = int(x_min * width)
        y_min = int(y_min * height)
        x_max = int(x_max * width)
        y_max = int(y_max * height)
        
        # Draw bounding box on the image
        class_color = class_colors.get(class_index, (0, 0, 255))  # Default color: Blue
        annotated_image = cv2.rectangle(annotated_image, (x_min, y_min), (x_max, y_max), class_color, 2)
        
        # Draw class label near the bounding box
        class_label = f"Class {class_index}"
        annotated_image = cv2.putText(annotated_image, class_label, (x_min, y_min - 5),
                                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, class_color, 2)
    
    return annotated_image
