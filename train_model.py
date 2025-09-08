# train_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Dummy training data: [age]
X = np.array([[20], [25], [30], [35], [40], [45], [50], [55], [60], [65]])
y = ['Normal', 'Normal', 'Normal', 'Abnormal', 'Abnormal', 'Abnormal', 'Abnormal', 'Abnormal', 'Abnormal', 'Abnormal']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open('lab_model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Model trained and saved as 'lab_model.pkl'")
