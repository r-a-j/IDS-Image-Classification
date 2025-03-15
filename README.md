<p align="center">
  <img src="https://raw.githubusercontent.com/r-a-j/IDS-Image-Classification/refs/heads/main/assets/company-logo.png" alt="PartikelArt Logo" align="left" height="80px" width="204px">
  <img src="https://raw.githubusercontent.com/r-a-j/IDS-Image-Classification/refs/heads/main/assets/uni-logo.svg" alt="TU Dortmund Logo" align="right" height="45px" width="250px">
</p>
<br>
<br>
<br>

<h1 align="center">Industrial Data Science 2</h1>
<br>
<h3 align="center">Metal and Non-Metal Particle Classification and Segmentation</h3>

### Project Overview

This project focuses on developing deep learning models to classify and segment metal and non-metal particles using high-resolution microscope images and low-resolution mobile phone images. The models include YOLOv8 for object detection and a custom CNN for classification. The goal is to create a solution that can adapt to varying image qualities, ensuring it is suitable for a wide range of industrial scenarios, ultimately enhancing cleanliness inspections and reducing contamination risks.

YOLOv8 was selected for its flexibility, offering models from nano to extra-large sizes, enabling deployment on both mobile devices and powerful servers.

## Plan

### Step 1: Data Preprocessing

- **Data Collection**: 
  - The dataset comprises 19,206 metal and 34,674 non-metal high-resolution microscope images, and 288 metal and 372 non-metal low-resolution mobile phone images. This diverse dataset was provided by PartikelART Solutions GmbH, a company specializing in technical cleanliness solutions.

- **Data Preprocessing**: 
  - The CNN images were resized to 128x128 pixels, converted to grayscale, and normalized to a [0, 1] pixel value range. Data augmentation techniques were applied to enhance generalization.
  - For YOLOv8, images were resized to 640x640 pixels, and 500 images were manually labeled with bounding boxes using the makesense.ai tool.

### Step 2: Object Detection

- **Model Selection**: 
  - YOLOv8 was selected for object detection due to its range of model sizes (nano to extra-large) suitable for various deployment environments.

- **Model Fine-tuning**: 
  - YOLOv8 was fine-tuned on the labeled dataset, split into 70% training, 15% validation, and 15% testing.

### Step 3: Object Classification

- **Model Selection**: 
  - A custom Convolutional Neural Network (CNN) was designed for classifying metal and non-metal particles.

- **Model Training**: 
  - The CNN was trained over 100 epochs with a batch size of 32, using early stopping and learning rate reduction to optimize performance and prevent overfitting.

### Step 4: Deployment

- **Interface Setup**: 
  - A user interface was set up using Gradio, allowing users to upload images and view the results of object detection and classification.

- **Deployment**: 
  - The YOLOv8 models can be deployed on mobile devices or servers, depending on the model size. The CNN model is suitable for server deployment in high-performance environments.

### User Interaction

Users upload an image containing objects to the interface. The image is passed through the object detection model, which identifies and locates objects within the image. Detected objects are then classified as metal or non-metal, with results displayed on the original image.

### Further Considerations

- **Performance Evaluation**: 
  - The models are evaluated using metrics such as accuracy, precision, recall, mean Average Precision (mAP), and Intersection over Union (IoU).

- **Continuous Improvement**: 
  - The system’s performance is continuously monitored, and user feedback is collected for further improvements.

## Analytical Strategy

The analytical strategy was carefully designed to address the variability in image quality and class imbalance. The YOLOv8 model was evaluated using mAP and IoU metrics, while the CNN was trained with data augmentation to improve generalization. The combined use of these models ensures robust particle classification and segmentation across different scenarios.

## Results

The project successfully developed models for metal and non-metal particle classification with the following results:

| Model                           | Data Source             | Acc. (Train) | Acc. (Val) | Loss (Train) | Loss (Val) |
|---------------------------------|-------------------------|--------------|------------|--------------|------------|
| YOLOv8n (Obj. Detection)        | Microscope (High Res)   | 75%          | 75%        | 2.10         | 3.32       |
| YOLOv8n (Inst. Segmentation)    | Microscope (High Res)   | 71%          | 71%        | 0.57         | 1.61       |
| YOLOv8n (Obj. Detection)        | Mobile Phone (Low Res)  | 66%          | 66%        | 0.47         | 1.41       |
| CNN                             | Microscope (High Res)   | 97%          | 97%        | 0.10         | 0.20       |
| CNN                             | Mobile Phone (Low Res)  | 93%          | 88%        | 0.17         | 0.30       |

- **Microscope Image Results (CNN)**
  
</br>
<p align="center">
  <img src="https://github.com/r-a-j/IDS-Image-Classification/blob/main/results/CNN%20microscope%20results/Precision_Recall_Curve_Microscope_HD.png" alt="Precision_Recall_Curve_Microscope Image" align="center" >
</p>
</br>

- **Microscope Image Results (YOLOv8)**
  
- **Mobile Image Results (YOLOv8 and CNN)**

## Conclusion

This project demonstrated the effectiveness of YOLOv8 and CNN models in classifying and segmenting metal and non-metal particles across varying image resolutions. While the CNN achieved higher accuracy, YOLOv8 offered flexibility in deployment, making it suitable for different industrial environments. Future work will focus on developing a unified model using transfer learning to handle both high and low-resolution images, providing a single, versatile solution for industrial applications.

## Future Work

The next phase involves creating a single model using transfer learning, combining the strengths of both the existing CNN models trained on high-resolution and low-resolution images. This unified model will be capable of handling diverse image sources, enabling broader deployment across different industrial settings.

## How to Use

1. **Installation:**
   - Clone the repository.
   - Install the required dependencies using `pip install -r requirements.txt`.

2. **Training:**
   - For YOLOv8: Use the provided training script with the labeled dataset.
   - For CNN: Run the training script with the preprocessed images.

3. **Evaluation:**
   - Evaluate the trained models using the test set and analyze the performance metrics.

4. **Deployment:**
   - Deploy the YOLOv8 models on mobile devices or servers.
   - Deploy the CNN model on a high-performance server.

## References

- **Ultralytics YOLOv8:** Glenn Jocher, Ayush Chaurasia, Jing Qiu. "Ultralytics YOLO." (2023). Available at: [Ultralytics YOLO](https://ultralytics.com)
- **PartikelART Solutions GmbH:** Technical Cleanliness Solutions. Available at: [PartikelART](https://www.partikel-art.de/)

---
