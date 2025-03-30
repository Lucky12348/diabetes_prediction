"""used to make predictions using the model"""


import pandas as pd

# get the model API
class DiabetesPredictor:
    def __init__(self, model, scaler):
        self.model = model
        self.scaler = scaler

    # function to make predictions
    def predict(self, data: dict) -> int:
        df = pd.DataFrame([data])
        df_scaled = pd.DataFrame(self.scaler.transform(df), columns=df.columns)
        return int(self.model.predict(df_scaled)[0])
