# Predictive Healthcare Analytics API

## Overview

Predictive Healthcare Analytics is an end-to-end machine learning project designed to predict hospital readmission risk using patient healthcare data.

The project covers the complete machine learning workflow, including data preprocessing, feature engineering, model comparison, hyperparameter optimization, model explainability, and deployment as a REST API using FastAPI.

The final system uses a trained CatBoost classification model to provide patient readmission risk predictions through an API endpoint.


---

# Problem Statement

Hospital readmissions represent a major challenge for healthcare systems because they increase healthcare costs and may indicate poor patient outcomes.

The goal of this project is to develop a machine learning model that predicts whether a patient is at risk of hospital readmission based on clinical and administrative features.

This prediction system can support healthcare professionals in identifying high-risk patients and improving preventive care strategies.


---

# Dataset

This project uses the:

**Diabetes 130-US Hospitals for Years 1999-2008 dataset**

The dataset contains hospital records collected from 130 US hospitals and includes information about:

- Patient demographics
- Admission details
- Diagnosis information
- Medication records
- Laboratory procedures
- Hospital utilization history


---

# Machine Learning Workflow

The project pipeline includes:

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Engineering
6. Feature Selection
7. Model Training
8. Model Comparison
9. Hyperparameter Optimization
10. Model Explainability
11. API Deployment


---

# Models Evaluated

Several machine learning algorithms were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost


---

# Final Model

After evaluating different models using multiple classification metrics, the final selected model was:

## CatBoost Classifier


Reasons for selecting CatBoost:

- Strong performance on tabular healthcare data
- Good handling of categorical features
- Robust performance compared with baseline models
- Suitable for deployment in production environments


---

# Model Performance

Evaluation metrics considered:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC


The final model achieved:

| Metric | Score |
|---|---|
| Accuracy | 0.595 |
| F1 Weighted | 0.550 |
| ROC-AUC | 0.695 |


---

# Model Explainability

To improve interpretability, SHAP analysis was performed to understand:

- Feature importance
- Feature contribution
- Model decision behavior


This helps make machine learning predictions more understandable in a healthcare context.


---

# API Deployment

The trained model was deployed using:

- FastAPI
- Pydantic schemas
- Modular prediction pipeline


The API provides endpoints for making patient readmission predictions.


## Example Request

```json
{
  "age": 75,
  "time_in_hospital": 5,
  "num_lab_procedures": 40,
  "num_medications": 20
}




Predictive Healthcare Analytics/

│
├── app/
│   └── main.py
│
├── src/
│   ├── config.py
│   ├── predictor.py
│   ├── preprocessing.py
│   ├── schemas.py
│   └── utils.py
│
├── models/
│   └── catboost.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── ...
│   └── 10_model_explainability.ipynb
│
├── reports/
│   └── best_model_summary.csv
│
├── requirements.txt
└── README.md



Future Improvements

Future improvements may include:

Model monitoring
Cloud deployment
Docker containerization
Improved prediction calibration
Integration with healthcare dashboards
Real-time patient risk monitoring
Technologies Used
Programming
Python
Machine Learning
Scikit-learn
CatBoost
XGBoost
LightGBM
Data Processing
Pandas
NumPy
Deployment
FastAPI
Docker
Author

Amirmahdi Imani

Biomedical Engineering | Data Science | Machine Learning