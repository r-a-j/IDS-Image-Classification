# Industrial Data Science 2

<p>Image Classification</p>

<p align="center">
  <img src="https://github.com/r-a-j/IDS-Image-Classification/blob/main/assets/uni-logo.svg" height="45px" width="250px"/>
</p>

<p align="center">
  <img src="https://github.com/r-a-j/IDS-Image-Classification/blob/main/assets/company-logo.png" height="80px" width="204px"/>
</p>

## Plan

### Step 1: Data Preprocessing
- **Data Collection**: 
  - Gather a dataset of images containing both metal and non-metal objects. This dataset should be diverse and representative of the real-world scenarios you expect the model to encounter.
  
- **Data Preprocessing**: 
  - Resize all images to a uniform size suitable for input to the object detection and classification models. 
  - Augment the data to increase its diversity and robustness.

### Step 2: Object Detection
- **Model Selection**: 
  - Choose a pre-trained object detection model suitable for your task. Popular choices include YOLO, SSD, or Faster R-CNN.
  
- **Model Fine-tuning**: 
  - Fine-tune the selected object detection model on your dataset to improve its performance on your specific task.
  
- **Detection Process**: 
  - When a new image is input to the model, it will perform object detection to identify and locate objects within the image. 
  - The output will include bounding boxes and class labels for each detected object.

### Step 3: Object Classification
- **Model Selection**: 
  - Choose a classifier model suitable for distinguishing between metal and non-metal objects. A Convolutional Neural Network (CNN) is commonly used for image classification tasks.
  
- **Model Training**: 
  - Train the classifier on your dataset of metal and non-metal objects to minimize classification error.
  
- **Integration with Object Detection**: 
  - Integrate the classifier with the object detection model. After objects are detected in an image, the classifier will be used to classify each detected object as either metal or non-metal.

### Step 4: Deployment
- **Interface Setup**: 
  - Set up a user interface using Gradio to allow users to upload images and view the results of object detection and classification.
  
- **Deployment**: 
  - Deploy the application to a server or host it locally so that users can access it via a web browser.

### User Interaction
> Users upload an image containing objects to the interface.
- The image is passed through the object detection model, which identifies and locates objects within the image.
- The detected objects are passed through the classifier, which classifies each object as either metal or non-metal.
- The interface displays the original image with bounding boxes drawn around the detected objects, along with their respective class labels.

### Further Considerations
- **Performance Evaluation**: 
  - Evaluate the performance of the deployed system using metrics such as accuracy, precision, recall, and F1-score.
  
- **Continuous Improvement**: 
  - Monitor the system's performance and gather user feedback to identify areas for improvement. This may involve collecting more data, fine-tuning models, or updating the interface for better usability.

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

<details>
  <summary>option 1</summary>
 
<!--START_SECTION:activity-->

```console
pip install pipreqs
```

```console
pipreqs
```
Detail reference: [here](https://precious-jalebi-a6ee2b.netlify.app/development-docs/#generate-automatic-requirementstxt)


<!--END_SECTION:activity-->

</details>

<details>
  <summary>option 2</summary>
 
<!--START_SECTION:activity-->

```console
pip install pigar
```

```console
pigar generate
```

<!--END_SECTION:activity-->

</details>

<!--END_SECTION:activity-->

</details>

- Install requirements.txt file

```console
pip install -r requirements. txt
```

- [The world's largest collection of open source computer vision datasets and APIs.](https://universe.roboflow.com/)
