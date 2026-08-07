# Predictive Healthcare Analytics

## Overview

Predictive Healthcare Analytics is an end-to-end machine learning application designed to predict hospital readmission risk using healthcare data.

The project demonstrates the complete machine learning lifecycle, including data understanding, data preprocessing, exploratory data analysis, feature engineering, feature selection, model training, evaluation, hyperparameter optimization, model explainability, and deployment.

The final solution uses a trained **CatBoost classification model** integrated into a **FastAPI REST API** to provide patient readmission risk predictions.

The application is also containerized using **Docker** to provide a reproducible deployment environment.

---

# Problem Statement

Hospital readmissions are a significant challenge for healthcare systems as they increase costs and may indicate patients who require additional monitoring and support.

The objective of this project is to develop a binary classification model that predicts whether a patient is at risk of hospital readmission based on clinical and administrative healthcare features.

This predictive approach can help explore how machine learning can support healthcare analytics and data-driven decision-making.

---

# Dataset

This project uses the:

**Diabetes 130-US Hospitals for Years 1999-2008 dataset**

The dataset contains patient records collected from 130 US hospitals between 1999 and 2008.

It includes information related to:

* Patient demographics
* Admission information
* Diagnosis codes
* Medication records
* Laboratory procedures
* Previous healthcare utilization

The original readmission target was transformed into a binary classification problem:

* **0:** No readmission
* **1:** Patient readmitted

---

# Machine Learning Workflow

The project pipeline includes:

1. Data Understanding
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Data Preprocessing
5. Feature Engineering
6. Feature Selection
7. Baseline Model Training
8. Model Comparison
9. Hyperparameter Optimization
10. Model Evaluation
11. Model Explainability
12. API Deployment
13. Docker Containerization

---

# Models Evaluated

Multiple machine learning algorithms were trained and compared:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* LightGBM
* CatBoost

Models were evaluated using multiple classification metrics instead of relying on accuracy alone.

---

# Final Model

## CatBoost Classifier

After comparing different models, CatBoost was selected as the final model.

Reasons for selecting CatBoost:

* Strong performance on structured/tabular healthcare data
* Effective handling of categorical variables
* Robust performance compared with baseline models
* Suitable integration with production ML pipelines

---

# Model Performance

The final model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* ROC-AUC

Final CatBoost performance:

| Metric      | Score |
| ----------- | ----: |
| Accuracy    | 0.595 |
| F1 Weighted | 0.550 |
| ROC-AUC     | 0.695 |

---

# Model Explainability

To improve transparency and interpretability, SHAP analysis was performed.

The explainability analysis focuses on:

* Feature importance
* Feature contribution to predictions
* Understanding model decision patterns

This provides better insight into how the model generates predictions, which is an important consideration in healthcare-related machine learning applications.

---

# API Deployment

The trained model was deployed as a REST API using:

* FastAPI
* Pydantic schemas
* Modular prediction pipeline
* Serialized CatBoost model

The API accepts patient information, applies the same preprocessing pipeline used during training, and returns a readmission risk prediction.

FastAPI automatically provides interactive API documentation through Swagger UI.

API documentation:

```
http://localhost:8000/docs
```

Example request:

```json
{
  "age": 75,
  "time_in_hospital": 5,
  "num_lab_procedures": 40,
  "num_medications": 20
}
```

---

# Docker Deployment

The application was containerized using Docker to create a reproducible and isolated runtime environment.

Docker provides:

* Dependency isolation
* Consistent execution environment
* Easier deployment across different systems

Docker image:

Docker Hub:
https://hub.docker.com/repository/docker/amirmahdi113314/predictive-healthcare-analytics-api

Run the application using:

```bash
docker pull amirmahdi113314/predictive-healthcare-analytics-api

docker run -p 8000:8000 amirmahdi113314/predictive-healthcare-analytics-api
```

---

# Project Structure

```
Predictive-Healthcare-Analytics/

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
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── ...
│   └── 10_model_explainability.ipynb
│
├── reports/
│   └── best_model_summary.csv
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

## Programming

* Python

## Machine Learning

* Scikit-learn
* CatBoost
* XGBoost
* LightGBM

## Data Processing

* Pandas
* NumPy

## Visualization & Explainability

* Matplotlib
* Seaborn
* SHAP

## API & Deployment

* FastAPI
* Docker
* Docker Hub
* Uvicorn

---

# Future Improvements

Potential future improvements include:

* Model monitoring
* Cloud deployment
* Prediction probability calibration
* Healthcare dashboard integration
* Real-time patient risk prediction pipeline

---

# Author

**Amirmahdi Imani**

Biomedical Engineering | Data Science | Machine Learning
