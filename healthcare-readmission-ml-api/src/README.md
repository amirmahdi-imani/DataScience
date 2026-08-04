# Source Code

This directory contains the core Python modules responsible for the machine learning inference pipeline and application logic.

The purpose of this structure is to separate machine learning functionality from the API layer, creating a modular, maintainable, and production-ready architecture.

---

# Overview

The `src` package contains the components required to:

* Load the trained machine learning model
* Prepare incoming prediction data
* Apply preprocessing steps
* Validate API inputs
* Generate final predictions
* Manage project configurations

The modules inside this directory are used by the FastAPI application to serve real-time predictions.

---

# Project Architecture

The prediction workflow follows this structure:

```
Client Request
      |
      ↓
FastAPI Application
(app/main.py)
      |
      ↓
Prediction Module
(src/predictor.py)
      |
      ↓
Preprocessing Pipeline
(src/preprocessing.py)
      |
      ↓
Trained CatBoost Model
(models/catboost.pkl)
      |
      ↓
Prediction Response
```

---

# Module Description

## config.py

### Purpose

Central configuration module for managing project paths and constants.

### Responsibilities

* Define project root directory
* Manage data paths
* Manage model paths
* Store reusable project settings
* Define global configuration variables

Main configurations include:

```
PROJECT_ROOT
DATA_DIR
MODELS_DIR
PIPELINE_PATH
REPORTS_DIR
TARGET_COLUMN
RANDOM_STATE
```

---

# predictor.py

### Purpose

Contains the main machine learning prediction logic.

### Responsibilities

* Load the trained CatBoost model
* Receive processed input data
* Generate model predictions
* Return prediction results

Prediction workflow:

```
Input Data
    |
    ↓
Data Preparation
    |
    ↓
Loaded CatBoost Model
    |
    ↓
Prediction Output
```

---

# preprocessing.py

### Purpose

Handles preprocessing operations required before model inference.

### Responsibilities

* Prepare incoming data
* Apply required transformations
* Maintain consistency between training and prediction phases
* Ensure input data matches the model requirements

This module helps prevent differences between training data processing and production inference.

---

# schemas.py

### Purpose

Defines API request and response schemas using Pydantic.

### Responsibilities

* Validate incoming user data
* Define prediction input structure
* Define API response format
* Ensure data consistency

Example workflow:

```
User Input
    |
    ↓
Pydantic Validation
    |
    ↓
Prediction Pipeline
```

---

# utils.py

### Purpose

Contains reusable helper functions used across the project.

### Responsibilities

* Common utility operations
* Shared functions
* Supporting functions for the application

---

# Design Principles

The `src` package follows these principles:

## Modularity

Each component has a specific responsibility, making the system easier to maintain and extend.

## Reproducibility

The same preprocessing and prediction logic is reused during deployment.

## Separation of Concerns

The project separates:

* API layer
* Machine learning logic
* Data preprocessing
* Configuration management

---

# Integration With FastAPI

The source modules are used by:

```
app/main.py
```

The FastAPI application communicates with the prediction pipeline through:

```
app/main.py
        |
        ↓
src/predictor.py
        |
        ↓
src/preprocessing.py
        |
        ↓
models/catboost.pkl
```

---

# Deployment

This modular structure allows the machine learning model to be:

* Served through REST API
* Containerized using Docker
* Integrated with frontend applications
* Extended for future healthcare analytics systems

---

# Future Improvements

Possible improvements include:

* Adding automated model versioning
* Implementing logging and monitoring
* Adding unit tests
* Supporting multiple prediction models
* Integrating model performance monitoring
