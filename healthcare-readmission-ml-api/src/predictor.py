"""
Prediction Module

This module handles loading the trained model pipeline
and generating predictions for new patient data.
"""


from typing import Dict, Any

import pandas as pd

from src.config import PIPELINE_PATH
from src.utils import load_pickle



# ==========================================================
# Model Loading
# ==========================================================

_model_pipeline = None


def get_model():
    """
    Load the trained model pipeline.

    The model is loaded only once and reused
    for future predictions.

    Returns
    -------
    pipeline
        Trained machine learning pipeline.
    """

    global _model_pipeline

    if _model_pipeline is None:

        _model_pipeline = load_pickle(
            PIPELINE_PATH
        )

    return _model_pipeline



# ==========================================================
# Prediction
# ==========================================================

def predict(patient_data: Dict[str, Any]) -> int:
    """
    Predict patient readmission class.

    Parameters
    ----------
    patient_data : dict
        Patient features.

    Returns
    -------
    int
        Predicted class label.
    """

    try:

        # Load trained pipeline
        pipeline = get_model()


        # Convert dictionary input into DataFrame
        # because sklearn ColumnTransformer expects tabular data
        input_data = pd.DataFrame(
            [patient_data]
        )


        # Generate prediction
        prediction = pipeline.predict(
            input_data
        )


        # Convert numpy array output to Python int
        return int(prediction[0])


    except Exception as e:

        raise RuntimeError(
            f"Prediction failed: {str(e)}"
        )