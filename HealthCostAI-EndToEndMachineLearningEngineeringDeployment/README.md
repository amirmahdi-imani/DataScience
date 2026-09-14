# HealthCost AI — End-to-End Machine Learning Engineering

An end-to-end machine learning project for predicting medical insurance charges, covering the complete workflow from data science and model development to API serving, containerization, cloud deployment, and a production web interface.

## Live Demo

**Frontend:**
https://healthcostai-end-to-end-machine-lea-pi.vercel.app/

**Backend API:**
https://datascience-mf6o.onrender.com

**API Documentation:**
https://datascience-mf6o.onrender.com/docs

---

## Overview

HealthCost AI is an end-to-end machine learning engineering project built around a medical insurance cost prediction model.

The project demonstrates how a trained machine learning model can be transformed into a deployable application through:

* Data preprocessing and feature engineering
* Machine learning model training
* Model serialization
* FastAPI model serving
* Docker containerization
* Cloud backend deployment
* Next.js frontend development
* Production deployment with Vercel
* Frontend-to-API integration

The goal is not only to build a predictive model, but to demonstrate the complete engineering pipeline required to make that model accessible through a real web application.

---

## Architecture

```text
                         ┌──────────────────────┐
                         │       User           │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   Next.js Frontend   │
                         │      Vercel          │
                         └──────────┬───────────┘
                                    │
                              HTTP / JSON
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     FastAPI API      │
                         │       Render         │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  ML Prediction       │
                         │     Pipeline         │
                         │  Random Forest       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Predicted Insurance  │
                         │       Charges        │
                         └──────────────────────┘
```

---

## Machine Learning

The prediction system uses a Scikit-learn pipeline containing preprocessing and a Random Forest regression model.

### Input Features

| Feature  | Type        |
| -------- | ----------- |
| Age      | Numeric     |
| Sex      | Categorical |
| BMI      | Numeric     |
| Children | Numeric     |
| Smoker   | Categorical |
| Region   | Categorical |

### Preprocessing

**Numerical features**

* Median imputation
* Standard scaling

Features:

```text
age
bmi
children
```

**Categorical features**

* Most-frequent imputation
* One-hot encoding
* Unknown categories handled safely

Features:

```text
sex
smoker
region
```

### Model

```text
RandomForestRegressor
n_estimators = 200
random_state = 42
```

The complete preprocessing and model pipeline is serialized using `joblib`.

Model artifact:

```text
models/final_model.joblib
```

---

## Backend

The backend is implemented with **FastAPI** and provides the interface between the frontend and the machine learning model.

### API Endpoints

| Method | Endpoint      | Description                           |
| ------ | ------------- | ------------------------------------- |
| GET    | `/health`     | API health check                      |
| POST   | `/predict`    | Generate a medical cost prediction    |
| GET    | `/model-info` | Return model information              |
| GET    | `/docs`       | Interactive Swagger API documentation |

### Example Prediction Request

```json
{
  "age": 30,
  "sex": "male",
  "bmi": 28.5,
  "children": 2,
  "smoker": "no",
  "region": "southwest"
}
```

### Example Response

```json
{
  "predicted_charges": 0000.00
}
```

---

## Frontend

The frontend is built with:

* Next.js
* React
* TypeScript
* Tailwind CSS
* shadcn/ui
* Lucide Icons
* next-themes

### Main Pages

```text
/
├── Home
├── /predict
└── /about
```

### Prediction Flow

```text
User Input
    ↓
Prediction Form
    ↓
Frontend API Request
    ↓
FastAPI /predict
    ↓
Scikit-learn Pipeline
    ↓
Random Forest
    ↓
Prediction Response
    ↓
Result Display
```

---

## Project Structure

```text
HealthCostAI-EndToEndMachineLearningEngineeringDeployment/
│
├── notebooks/
│   ├── ...
│
├── models/
│   └── final_model.joblib
│
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── inference.py
│
├── frontEnd/
│   └── healthcostai-end-to-end-machine-learning-engineering/
│       ├── src/
│       │   ├── app/
│       │   ├── components/
│       │   ├── config/
│       │   ├── lib/
│       │   └── types/
│       ├── public/
│       ├── package.json
│       ├── package-lock.json
│       ├── next.config.ts
│       ├── tsconfig.json
│       └── ...
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Technology Stack

### Machine Learning

* Python
* Pandas
* Scikit-learn
* Joblib

### Backend

* FastAPI
* Uvicorn
* Pydantic

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS
* shadcn/ui

### DevOps & Deployment

* Docker
* Git
* GitHub
* Render
* Vercel

---

## Deployment

### Backend

The FastAPI application is containerized with Docker and deployed on Render.

```text
Docker
   ↓
FastAPI
   ↓
Render
```

Backend:

https://datascience-mf6o.onrender.com

### Frontend

The Next.js application is deployed on Vercel.

```text
Next.js
   ↓
Vercel
```

Frontend:

https://healthcostai-end-to-end-machine-lea-pi.vercel.app/

The frontend communicates with the deployed backend through the environment variable:

```env
NEXT_PUBLIC_API_URL=https://datascience-mf6o.onrender.com
```

---

## Local Development

### Backend

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn api.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

### Frontend

Navigate to the frontend directory:

```bash
cd frontEnd/healthcostai-end-to-end-machine-learning-engineering
```

Install dependencies:

```bash
npm install
```

Create `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

Run the development server:

```bash
npm run dev
```

Frontend:

```text
http://localhost:3000
```

---

## Engineering Highlights

This project demonstrates:

* End-to-end ML development
* Reproducible preprocessing pipelines
* Model serialization and inference
* REST API development
* Input validation with Pydantic
* CORS configuration
* Docker-based deployment
* Cloud deployment
* Production frontend development
* API integration
* Environment-based configuration
* Responsive UI
* Light and dark themes
* Separation of frontend, backend, and ML responsibilities

---

## Disclaimer

This application is an educational and engineering demonstration.

Predictions are generated by a machine learning model and should not be considered medical, financial, or insurance advice.

---

## Author

**Amir Imani**

Machine Learning / Data Science / ML Engineering

GitHub:
https://github.com/amirmahdi-imani

