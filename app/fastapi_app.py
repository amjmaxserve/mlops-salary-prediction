import os
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# -----------------------------
# Base Path
# -----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "..", "model")

# -----------------------------
# Load Model Files
# -----------------------------

model = joblib.load(
    os.path.join(MODEL_DIR, "salary_model.pkl")
)

label_encoders = joblib.load(
    os.path.join(MODEL_DIR, "label_encoders.pkl")
)

target_encoder = joblib.load(
    os.path.join(MODEL_DIR, "target_encoder.pkl")
)

# -----------------------------
# FastAPI App
# -----------------------------

app = FastAPI()

# -----------------------------
# Input Schema
# -----------------------------

class EmployeeData(BaseModel):
    age: int
    education: str
    hours_per_week: int
    occupation: str
    experience: int

# -----------------------------
# Home Route
# -----------------------------

@app.get("/")
def home():
    return {
        "message": "FastAPI ML API Running"
    }

# -----------------------------
# Prediction Route
# -----------------------------

@app.post("/predict")
def predict(data: EmployeeData):

    education_encoded = label_encoders['education'].transform([
        data.education
    ])[0]

    occupation_encoded = label_encoders['occupation'].transform([
        data.occupation
    ])[0]

    input_data = pd.DataFrame([{
        'age': data.age,
        'education': education_encoded,
        'hours_per_week': data.hours_per_week,
        'occupation': occupation_encoded,
        'experience': data.experience
    }])

    prediction = model.predict(input_data)

    result = target_encoder.inverse_transform(prediction)

    return {
        "prediction": result[0]
    }
