# Malaria Detection Using Convolutional Neural Networks

## Overview
The goal of this project is to build an efficient system for the automatic diagnosis of malaria by detecting the presence of the Plasmodium parasite in blood cells using Convolutional Neural Networks (CNNs). Given the significant health burden posed by malaria, particularly in Africa, accurate and timely diagnosis can greatly improve patient outcomes and reduce transmission rates.

## Problem Definition
Malaria is a critical health concern globally, with an estimated 249 million cases and 608,000 deaths reported in 2022. Diagnosing malaria manually through microscopic image examination is time-consuming, resource-intensive, and subject to human error. This project leverages CNNs due to their exemplary ability to extract features for accurate image classification.

### Objectives
- To develop an accurate CNN model for classifying blood cells as parasitized or uninfected.
- To create a model suitable for deployment in field clinics, offering rapid results.

### Key Questions
- What are the characteristics of the images?
- How can we differentiate between parasitized and uninfected cells?
- What preprocessing methods enhance the image inputs for CNNs?
- How do existing pre-trained models perform compared to our custom-trained models?
- What is the most effective and efficient CNN architecture for this task?

## Data Description
The dataset consists of 24,958 training images and 2,600 test images of colored blood samples, divided into:
- **Parasitized**: Cells that contain the Plasmodium parasite.
- **Uninfected**: Cells free from the parasite.

## Getting Started
To experiment with this project, you can open it in Google Colab. Follow these steps to set up:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/malaria-detection.git
    cd malaria-detection
    ```

2. Install necessary libraries:
    ```bash
    !pip install -r requirements.txt
    ```

3. Load the dataset into your Google Drive, extract it, and run the preprocessing scripts provided in the notebook.

## Web Application

This project includes a Flask web application for user-friendly prediction of malaria in blood cell images.

### Features
- Upload images for analysis.
- Predict whether malaria is detected in the given blood sample using the trained CNN model.
- Return prediction results in JSON format.

### Application Structure
The application has the following routes:
- `/`: Renders the main page.
- `/upload`: Accepts file uploads and returns classification results.
- `/uploads/<filename>`: Serves the uploaded files.

Here's a summary of the key components in the web application:

#### Uploading and Predicting
When a file is uploaded through the web interface:
1. The image is saved to the `uploads` directory.
2. The image is preprocessed to the required format.
3. The CNN model predicts the presence of malaria.
4. The result is returned as JSON.

### Running the Application
To run the Flask web application, ensure the necessary libraries are installed and execute the application as follows:

```bash
python app.py
```

## Model Building
The project features multiple model architectures, including:
- **Base Model**: A simple CNN with 2 convolutional layers and dropout for regularization.
- **Model 1**: Added complexity with more convolutional layers and appropriate activation functions.
- **Model 2**: Introduces LeakyReLU activation and batch normalization to enhance learning.
- **Model 3**: Utilizes data augmentation techniques for a diverse training set.
- **Model 4**: Adopts the pre-trained VGG16 model for comparative evaluation.

The final model selected for deployment is Model 2, as it demonstrates robust accuracy and efficiency.

### Model Evaluation
Each model is evaluated on key metrics, such as accuracy, precision, recall, and the confusion matrix, to determine performance. The following highlights were noted:
- Model 3 achieved the highest detection accuracy at 98.1%.
- False negatives were minimized across Models 2 and 3, indicating improved detection of parasitized cells compared to the base model.

## Conclusion and Insights
- CNNs efficiently detect malaria in microscopic images, offering a promising solution for automated diagnostics in clinical settings.
- The models highlight the importance of preprocessing, data augmentation, and tuning of hyperparameters.
- Future work can explore using additional techniques or different architectures to further enhance model performance.

## References
1. World Malaria Report 2023.
2. WHO Guidelines for Malaria, October 2023.
3. Original research papers on CNNs and their application in medical image diagnostics.

---

For detailed code and implementation steps, refer to the provided Jupyter notebooks in this repository. Happy coding!
