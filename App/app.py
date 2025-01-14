from flask import Flask, request, render_template, jsonify, send_from_directory
import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.utils import load_img, img_to_array

app = Flask(__name__)

# Load the CNN model
model = tf.keras.models.load_model('final_model.keras')

def preprocess_image(image_path):
    img = img_to_array(load_img(image_path, target_size=(100, 100)))
    img = np.array(img) / 255.0  # Normalize to [0, 1]
    img = np.expand_dims(img, axis=0)
    return np.array(img)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        img = preprocess_image(file_path)
        prediction = model.predict(img.reshape(1, 100, 100, 3))
        
        # Get the prediction value and convert to a native Python float
        prediction_value = float(prediction[0][0])
        if prediction_value < 0.5:
            result = 'Malaria detected'
        else:
            result = 'No malaria detected'
 
        return jsonify({'result': result, 'prediction': prediction_value, 'filename': file.filename})
    return jsonify({'result': 'No file uploaded'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)