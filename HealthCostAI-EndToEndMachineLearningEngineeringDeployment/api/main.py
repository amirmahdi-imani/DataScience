from fastapi import FastAPI, HTTPException
from .schemas import PredictionRequest, ModelInfoResponse
from .inference import predict


app = FastAPI(
    title="HealthCost AI API",
    description="API for predicting medical insurance charges",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/predict")
def make_prediction(request: PredictionRequest):

    input_data = [[
        request.age,
        request.sex,
        request.bmi,
        request.children,
        request.smoker,
        request.region
    ]]

    try:
        prediction = predict(input_data)

        return {
            "predicted_charges": prediction
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


@app.get("/model-info", response_model=ModelInfoResponse)
def model_info():
    return {
        "model": "Random Forest Regressor",
        "task": "Regression",
        "target": "charges"
    }