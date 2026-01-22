readme: |
  # Churn Prediction Platform

  A complete **Churn Prediction Web App** built using **FastAPI** (backend) and **HTML/CSS/JS** (frontend).  
  Users can upload a CSV file and get churn prediction along with evaluation metrics.

  ---


---

## ✅ Features

- Upload CSV file from frontend  
- Data cleaning, scaling, and feature engineering  
- Feature selection & model prediction  
- Multiple ML algorithms support  
- Clean modular structure using OOP

---

## 🛠️ Installation

###  Create virtual environment
```bash
conda create -n churn_env python=3.11
conda activate churn_env
```
### API Example

Endpoint: POST /predict

Request Example
```bash
{
  "algo": "random_forest",
  "file": "customer_data.csv"
}
{
  "accuracy": 0.89,
  "precision": 0.84,
  "recall": 0.81,
  "f1_score": 0.82,
  "predictions": [0, 1, 0, 0, 1]
}




