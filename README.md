# DiagnoSmart

A Flask-based medical diagnosis web application that uses machine learning models for lab result predictions.

## Features
- Upload X-ray and ECG files (placeholders for future deep learning integration)
- Predict lab results based on patient age using a RandomForestClassifier model
- Simple and user-friendly interface

## Technologies Used
- Python, Flask, scikit-learn, HTML

## How to Run
1. Install dependencies: `pip install flask scikit-learn numpy`
2. Run `train_model.py` to create the ML model.
3. Run `app.py` to start the Flask server.
4. Open `http://127.0.0.1:5000/` in your browser.

## License
MIT License
