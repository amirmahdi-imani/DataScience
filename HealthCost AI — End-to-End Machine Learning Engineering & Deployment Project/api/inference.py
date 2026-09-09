import joblib
import pandas as pd


model = joblib.load("models/final_model.joblib")


def predict(input_data):

    columns = [
        "age",
        "sex",
        "bmi",
        "children",
        "smoker",
        "region"
    ]

    df = pd.DataFrame(input_data, columns=columns)

    prediction = model.predict(df)

    return float(prediction[0])