"""API definition and the code to run the API in a separate thread"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.model_loader import load_model
from app.predictor import DiabetesPredictor
import threading
import uvicorn

model = load_model()
predictor = DiabetesPredictor(model)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# data model for API
class PatientData(BaseModel):
    Pregnancies: int
    PlasmaGlucose: float
    DiastolicBloodPressure: float
    TricepsThickness: float
    SerumInsulin: float
    BMI: float
    DiabetesPedigree: float
    Age: int

# endpoint for prediction
@app.post("/predict")
def predict(data: PatientData):
    prediction = predictor.predict(data.model_dump())
    return {"prediction": prediction}

# function to run the API
def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# function to start the API in a separate thread
def start_api_thread():
    thread = threading.Thread(target=run_api, daemon=True)
    thread.start()
