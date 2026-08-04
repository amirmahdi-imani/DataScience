# Machine Learning Notebooks

This directory contains the complete machine learning workflow developed for the Predictive Healthcare Analytics project.

The notebooks represent the step-by-step process from raw healthcare data exploration to final model explainability.

---

## Notebook Workflow

### 01 - Data Understanding

**File:**
`01_data_understanding.ipynb`

Purpose:

- Load and inspect the raw dataset
- Understand dataset structure
- Analyze feature types
- Identify missing values and inconsistencies


---

### 02 - Data Cleaning

**File:**
`02_data_cleaning.ipynb`

Purpose:

- Handle missing values
- Remove irrelevant features
- Clean inconsistent data entries
- Prepare data for further analysis


---

### 03 - Exploratory Data Analysis

**File:**
`03_exploratory_data_analysis.ipynb`

Purpose:

- Analyze feature distributions
- Explore relationships between variables
- Investigate target variable distribution
- Identify important patterns in healthcare data


---

### 04 - Data Preprocessing

**File:**
`04_data_preprocessing.ipynb`

Purpose:

- Prepare data for machine learning models
- Apply preprocessing techniques
- Create training-ready datasets


---

### 05 - Feature Engineering

**File:**
`05_feature_engineering.ipynb`

Purpose:

- Create new meaningful features
- Improve model input representation
- Capture healthcare-related patterns


---

### 06 - Feature Selection

**File:**
`06_feature_selective.ipynb`

Purpose:

- Analyze feature importance
- Select relevant features
- Reduce unnecessary complexity


---

### 07 - Model Training

**File:**
`07_model_training.ipynb`

Purpose:

Train multiple machine learning algorithms:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- CatBoost


---

### 08 - Model Comparison

**File:**
`08_model_comparison.ipynb`

Purpose:

- Compare model performance
- Evaluate classification metrics
- Select the best performing model


Metrics:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC


---

### 09 - Hyperparameter Tuning

**File:**
`09_hyperparametr_tuning.ipynb`

Purpose:

- Optimize the selected model
- Search for better hyperparameter configurations
- Improve model performance


---

### 10 - Model Explainability

**File:**
`10_model_explainability.ipynb`

Purpose:

- Analyze model decisions
- Apply SHAP explainability techniques
- Understand feature contributions


---

## Final Outcome

The notebook workflow resulted in a production-ready CatBoost classification model that was integrated into a FastAPI prediction service.

Final model:
