# app.py
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import random
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the saved lab model
with open('lab_model.pkl', 'rb') as file:
    lab_model = pickle.load(file)

# Load pre-trained deep learning models for X-ray and ECG (placeholders)
# Uncomment and update these lines when you have real models
# xray_model = load_model('models/xray_model.h5')
# ecg_model = load_model('models/ecg_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    name = request.form['name']
    age = int(request.form['age'])
    
    # Save uploaded files
    xray_file = request.files.get('xray')
    ecg_file = request.files.get('ecg')
    
    if xray_file:
        xray_path = os.path.join(UPLOAD_FOLDER, secure_filename(xray_file.filename))
        xray_file.save(xray_path)
        # Placeholder: load image and predict
        # image = Image.open(xray_path).resize((224, 224))
        # image_array = np.array(image) / 255.0
        # image_array = image_array.reshape((1, 224, 224, 3))
        # xray_result_raw = xray_model.predict(image_array)
        # xray_result = 'Normal' if xray_result_raw[0][0] < 0.5 else 'Abnormal'
        xray_result = random.choice(['Normal', 'Abnormal'])  # Placeholder
    else:
        xray_result = 'No file uploaded'
    
    if ecg_file:
        ecg_path = os.path.join(UPLOAD_FOLDER, secure_filename(ecg_file.filename))
        ecg_file.save(ecg_path)
        # Placeholder: process ECG data and predict
        ecg_result = random.choice(['Normal', 'Abnormal'])  # Placeholder
    else:
        ecg_result = 'No file uploaded'
    
    # Predict lab result using age as input
    lab_input = np.array([[age]])
    lab_result = lab_model.predict(lab_input)[0]
    
    return render_template('result.html', name=name, age=age,
                           xray=xray_result, ecg=ecg_result, lab=lab_result)

if __name__ == "__main__":
    app.run(debug=True)
