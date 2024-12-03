# 🚨 NYC Emergency Dispatch Response Time Prediction

This project aims to predict **emergency dispatch response time** (in minutes) across New York City's boroughs using a combination of emergency call data and weather conditions. The pipeline processes data, applies preprocessing, trains multiple regression models, evaluates them, and makes real-time predictions.

---

## 📊 Dataset Information

**Source:** [NYC Open Data - NYPD Calls for Service (Year to Date)](https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Year-to-Date-/n2zq-pubd/about_data)

- **Last Updated:** October 21, 2024
- **Data Used:** Calls updated till **July 2024**
- **Weather Data:** Sourced from [Meteomatics API](https://www.meteomatics.com/en/api/overview/)

---

## ✅ Objective

Predict the dispatch response time (`TIM_MIN`) based on:
- Location (latitude, longitude)
- Time (hour, day)
- Weather (temperature, rain)
- Incident features (reason category, precinct, patrol unit)

---

## 🛠️ Preprocessing Steps

1. Filter records from **June 2024** only.
2. Clean and parse timestamps (`ADD_TS`, `DISP_TS`, `ARRIVD_TS`, `CLOSNG_TS`)
3. Merge emergency data with **borough-specific weather data**
4. Handle missing values, encode categorical columns, and engineer features like `day`, `hour`, `CIP_JOBS_Enc`, etc.
5. Normalize features and label using `StandardScaler`
6. Save final dataset to `PreProcessedDataset.csv`

---

## 📈 Model Training

Models trained using `train_data.csv`:
- ✅ **XGBoost Regressor**
- ✅ **Random Forest Regressor**
- ✅ **Ridge Regression**
- ✅ **Stacking Regressor** (XGBoost + RF, with Ridge as meta-learner)

All models are saved in the `models/` directory for reuse.

---

## 📊 Evaluation

Metrics used:
- **MAE (Mean Absolute Error)**
- **RMSE (Root Mean Square Error)**
- **R² Score**

Evaluation results are stored in `evaluation/summary.txt`.

---

## 📍 Prediction Interface

- Accepts raw event + weather data (dictionary format)
- Processes input using same transformations as training
- Makes predictions using saved XGBoost model
- Scales back the prediction to original units (minutes)

--- 

## Run the project

 - Download the Dataset from : https://data.cityofnewyork.us/Public-Safety/NYPD-Calls-for-Service-Year-to-Date-/n2zq-pubd/about_data The above dataset has been updated on Oct 21, and I have used the dataset with updated data till July 2024
 - python wf_evaluation.py  
 - python wf_evaluation.py 

Example output:
```python
Response time for input1: 11.36 minutes
Response time for input2: 3.42 minutes


