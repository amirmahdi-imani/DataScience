"""
Pydantic schemas for API input and output.
"""

from pydantic import BaseModel


class PatientInput(BaseModel):
    """
    Patient features required for prediction.
    """

    num_lab_procedures: int
    diag_1: str
    diag_2: str
    diag_3: str

    num_medications: int
    time_in_hospital: int
    age: int

    discharge_disposition_id: int
    number_diagnoses: int
    num_procedures: int

    total_visits: int
    admission_type_id: int
    number_inpatient: int

    race: str
    insulin: str

    admission_source_id: int

    active_medications: int
    gender: str

    number_outpatient: int

    metformin: str
    glipizide: str
    glyburide: str

    number_emergency: int

    changed_medications: int

    change: str

    pioglitazone: str
    rosiglitazone: str
    glimepiride: str



class PredictionOutput(BaseModel):
    """
    Prediction response.
    """

    prediction: int