"""
Utility Functions

This module contains reusable helper functions used across
the project.
"""

from pathlib import Path
import joblib


# ==========================================================
# File Utilities
# ==========================================================

def load_pickle(file_path: Path):
    """
    Load a serialized object from disk.

    Parameters
    ----------
    file_path : Path
        Path to the saved object.

    Returns
    -------
    object
        Loaded Python object.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    obj = joblib.load(file_path)

    return obj



def save_pickle(obj, file_path: Path):
    """
    Save a Python object to disk.

    Parameters
    ----------
    obj : object
        Python object to save.

    file_path : Path
        Destination path.
    """

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    joblib.dump(
        obj,
        file_path
    )



# ==========================================================
# Path Utilities
# ==========================================================

def check_file_exists(file_path: Path):
    """
    Check whether a file exists.

    Returns
    -------
    bool
    """

    return file_path.exists()