from pydantic import BaseModel, Field
from typing import Literal


class PredictionRequest(BaseModel):
    age: int = Field(..., ge=18, le=100)
    sex: Literal["male", "female"]
    bmi: float = Field(..., gt=0)
    children: int = Field(..., ge=0, le=10)
    smoker: Literal["yes", "no"]
    region: Literal[
        "southwest",
        "southeast",
        "northwest",
        "northeast"
    ]

class ModelInfoResponse(BaseModel):
    model: str
    task: str
    target: str