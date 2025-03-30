"""API definition and the code to run the API in a separate thread"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.model_loader import load_model, load_scaler
from app.predictor import DiabetesPredictor
import threading
import uvicorn

model = load_model()
scaler = load_scaler()
predictor = DiabetesPredictor(model, scaler)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

def encode_bmi_category(bmi):
    if bmi < 18.5:
        return 0  # underweight
    elif bmi < 25:
        return 1  # normal weight
    elif bmi < 30:
        return 2  # overweight
    elif bmi < 35:
        return 3  # obese
    else:
        return 4  # severely obese

# data model for API
class PatientData(BaseModel):
    Pregnancies: int
    PlasmaGlucose: int
    DiastolicBloodPressure: int
    TricepsThickness: int
    SerumInsulin: int
    BMI: float
    DiabetesPedigree: float
    Age: int

# endpoint for prediction
@app.post("/predict")
def predict(data: PatientData):
    patient_dict = data.model_dump()
    patient_dict["bmi_category"] = encode_bmi_category(patient_dict["BMI"])
    prediction = predictor.predict(patient_dict)
    return {"prediction": prediction}

# function to run the API
def run_api():
    uvicorn.run(app, host="0.0.0.0", port=8000)

# function to start the API in a separate thread
def start_api_thread():
    thread = threading.Thread(target=run_api, daemon=True)
    thread.start()
