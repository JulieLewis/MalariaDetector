# Malaria Detection with Convolutional Neural Networks (CNNs)

## Overview
This repository contains a comprehensive project for detecting malaria from microscopic blood images using Convolutional Neural Networks (CNNs). Given the severity of malaria as a global health issue, the objective is to develop an accurate model that can assist in the early diagnosis of this disease, thus preventing fatalities and reducing transmission.

## Problem Definition
Malaria is an urgent health concern, with an estimated **249 million cases** and **608,000 deaths** worldwide in 2022, primarily impacting Africa. Diagnosing malaria accurately is critical, particularly in light of increasing antimalarial drug resistance. Traditional microscopic examination of blood samples is time-consuming and relies on the skill of trained technicians, which can yield variable results.

Outdoor clinics require quick, automated solutions that can accurately distinguish between parasitized and uninfected blood cells. This project aims to leverage CNNs to automate such diagnoses and improve access to accurate health assessments.

### Key Questions
- What features differentiate parasitized and uninfected cells in images?
- Which image preprocessing techniques enhance CNN training?
- How do pre-trained CNN models compare against models trained solely on the dataset?
- Which model achieves the best accuracy and computational efficiency?

## Data Description
The project utilizes a dataset containing **24,958 training** and **2,600 testing** colored images divided into two categories:
- **Parasitized**: Cells infected with the Plasmodium parasite.
- **Uninfected**: Healthy cells.

This dataset allows for supervised learning techniques to classify cells based on image features.

## Installation
To ensure you have all the necessary libraries, you can install them using the following:

```bash
pip install numpy pandas matplotlib seaborn tensorflow opencv-python
```

## Load the Data
The images must be downloaded and stored in a specified directory. Use the following code to extract the files and load the dataset in Google Colab:

```python
import os
import zipfile
import cv2
import numpy as np
import pandas as pd

# Load your dataset
root_path = '/content/drive/MyDrive/Malaria'
with zipfile.ZipFile(os.path.join(root_path, 'cell_images.zip'), 'r') as zip_ref:
    zip_ref.extractall('/content/sample_data')
```

## Model Building
The CNN model is constructed utilizing various techniques for optimized performance:
- **Base Model**: Custom CNN architecture with dropout layers to mitigate overfitting.
- **Expanded Models**: Additional CNN models that apply techniques such as:
  - Batch Normalization
  - Data Augmentation
  - Transfer Learning with pre-trained models like VGG16

The models are evaluated based on accuracy, precision, recall, and F1-score to determine the best-performing architecture.

## Training and Evaluation
For model training, we utilize a set of callback functions to monitor performance during epochs and save the best models:

```python
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

callbacks = [
    EarlyStopping(monitor='val_loss', patience=5, verbose=1, mode='min'),
    ModelCheckpoint('best_model.keras', monitor='val_loss', save_best_only=True)
]
```

Once trained, models are validated using confusion matrices and classification reports, providing insights into model performance.

## Results
- **Model 1** achieved an accuracy of 97.5%.
- **Model 2** with Leaky ReLU and Batch Normalization reached 97.8%.
- **Model 3**, with data augmentation techniques, resulted in an accuracy of **98.1%** and is unveiled as the final model due to its robustness in detecting both uninfected and parasitized cells.

## Conclusion
The model exhibits strong competencies in accurately identifying malaria, addressing the significant health challenge posed by the disease. Despite the inherent challenges, this work demonstrates that CNNs can effectively assist in malaria diagnosis, potentially improving clinical outcomes.

## License
This project is open-source and available under the [MIT License](LICENSE).

## References
1. World Malaria Report 2023
2. WHO Guidelines for Malaria, October 15, 2023
3. Capstone Project Problem Statement
