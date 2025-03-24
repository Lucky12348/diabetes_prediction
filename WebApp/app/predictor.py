"""used to make predictions using the model"""


import pandas as pd

# get the model API
class DiabetesPredictor:
    def __init__(self, model):
        self.model = model

    # function to make predictions
    def predict(self, data: dict) -> int:
        df = pd.DataFrame([data])
        return int(self.model.predict(df)[0])
