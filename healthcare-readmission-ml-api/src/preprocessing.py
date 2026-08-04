"""
Data preprocessing utilities for inference.

This module prepares raw input data before sending it
to the trained pipeline.
"""

import pandas as pd



# ==========================================================
# Input Preparation
# ==========================================================

def prepare_input(data: dict) -> pd.DataFrame:
    """
    Convert raw input dictionary into a pandas DataFrame.

    Parameters
    ----------
    data : dict
        Raw input features.

    Returns
    -------
    pd.DataFrame
        Prepared input dataframe.
    """

    df = pd.DataFrame([data])

    return df