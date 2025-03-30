"""loads the model by path return the model object"""


import joblib

# load model with path
def load_model(path="../models/TAIPEI_diabetes.pkl"):
    return joblib.load(path)

# load scaler
def load_scaler(path="../models/scaler.pkl"):
    return joblib.load(path)