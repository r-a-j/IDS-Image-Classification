# Industrial Data Science 2 - Image-Classification

<p align="center">
  <img src="https://github.com/r-a-j/IDS-Image-Classification/blob/main/assets/logo.svg" />
</p>

## Plan

### Step 1: Data Preprocessing
#### 1.1 Data Collection: Gather a dataset of images containing both metal and non-metal objects. This dataset should be diverse and representative of the real-world scenarios you expect the model to encounter.

#### 1.2 Data Preprocessing: Resize all images to a uniform size suitable for input to the object detection and classification models. You may also need to augment the data to increase its diversity and robustness.

### Step 2: Object Detection
#### 2.1 Model Selection: Choose a pre-trained object detection model suitable for your task. YOLO (You Only Look Once), SSD (Single Shot MultiBox Detector), or Faster R-CNN are popular choices.

#### 2.2 Model Fine-tuning: Fine-tune the selected object detection model on your dataset. This involves adjusting the model's parameters to improve its performance on your specific task.

#### 2.3 Detection Process: When a new image is input to the model, it will perform object detection to identify and locate objects within the image. The output will include bounding boxes and class labels for each detected object.

### Step 3: Object Classification
#### 3.1 Model Selection: Choose a classifier model suitable for distinguishing between metal and non-metal objects. A Convolutional Neural Network (CNN) is commonly used for image classification tasks.

#### 3.2 Model Training: Train the classifier on your dataset of metal and non-metal objects. This involves feeding the images through the network and adjusting the model's parameters to minimize classification error.

#### 3.3 Integration with Object Detection: Integrate the classifier with the object detection model. After objects are detected in an image, the classifier will be used to classify each detected object as either metal or non-metal.

### Step 4: Deployment
#### 4.1 Interface Setup: Set up a user interface using Gradio to allow users to upload images and view the results of object detection and classification.

#### 4.2 Deployment: Deploy the application to a server or host it locally so that users can access it via a web browser.

### User Interaction
> Users upload an image containing objects to the interface.
The image is passed through the object detection model, which identifies and locates objects within the image.
The detected objects are passed through the classifier, which classifies each object as either metal or non-metal.
The interface displays the original image with bounding boxes drawn around the detected objects, along with their respective class labels.

### Further Considerations
#### Performance Evaluation: Evaluate the performance of the deployed system using metrics such as accuracy, precision, recall, and F1-score.
#### Continuous Improvement: Monitor the system's performance and gather user feedback to identify areas for improvement. This may involve collecting more data, fine-tuning models, or updating the interface for better usability.


<details>
  <summary>Create virtual env</summary>
 
<!--START_SECTION:activity-->

```console
python -m venv .venv
```

if script execution policy error:
```console
Set-ExecutionPolicy Unrestricted -Scope Process
```

activate virtual environment:
```console
.venv\Scripts\activate
```

or

```console
.\venv\Scripts\Activate.ps1
```
<!--END_SECTION:activity-->

</details>

<details>
  <summary>Autogenerate requirements.txt</summary>
 
<!--START_SECTION:activity-->

```console
pip install pipreqs
```

```console
pipreqs --force
```

detail reference: [here](https://precious-jalebi-a6ee2b.netlify.app/development-docs/#generate-automatic-requirementstxt)
<!--END_SECTION:activity-->

</details>

