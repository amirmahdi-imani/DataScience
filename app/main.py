"""
FastAPI Application

This module exposes the machine learning model
through REST API endpoints.
"""


from fastapi import FastAPI, HTTPException

from src.predictor import predict
from src.schemas import (
    PatientInput,
    PredictionOutput
)



# ==========================================================
# FastAPI Application
# ==========================================================

app = FastAPI(
    title="Predictive Healthcare Analytics API",
    description=(
        "API for predicting hospital readmission risk "
        "using a trained CatBoost machine learning pipeline."
    ),
    version="1.0.0"
)



# ==========================================================
# Health Check Endpoint
# ==========================================================

@app.get("/")
def root():
    """
    API health check.
    """

    return {
        "status": "API is running",
        "service": "Predictive Healthcare Analytics"
    }



# ==========================================================
# Prediction Endpoint
# ==========================================================

@app.post(
    "/predict",
    response_model=PredictionOutput
)
def predict_patient(
    patient: PatientInput
):
    """
    Predict readmission class for a patient.
    """

    try:

        prediction = predict(
            patient.model_dump()
        )


        return PredictionOutput(
            prediction=prediction
        )


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )