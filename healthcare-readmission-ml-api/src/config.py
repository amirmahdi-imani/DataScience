"""
Project Configuration File

This module contains all project-level constants and paths.
All important configurations are centralized here to avoid
hardcoded values across the project.
"""

from pathlib import Path


# ==========================================================
# Project Root
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ==========================================================
# Data Paths
# ==========================================================

DATA_DIR = PROJECT_ROOT / "data"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_DATA_PATH = DATA_DIR / "diabetic_data.csv"
PROCESSED_DATA_PATH = PROCESSED_DATA_DIR / "selected_data.csv"



# ==========================================================
# Model / Pipeline Paths
# ==========================================================

MODELS_DIR = PROJECT_ROOT / "models"

PIPELINE_PATH = MODELS_DIR / "catboost.pkl"



# ==========================================================
# Reports Paths
# ==========================================================

REPORTS_DIR = PROJECT_ROOT / "reports"



# ==========================================================
# Project Settings
# ==========================================================

TARGET_COLUMN = "readmitted"

RANDOM_STATE = 42
