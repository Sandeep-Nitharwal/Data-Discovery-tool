from sklearn.externals import joblib

# Load pre-trained ML model
model = joblib.load('path/to/pii_model.pkl')

def detect_pii_ml(data):
    prediction = model.predict([data])
    return prediction
