from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from wf_ml_training import XGBoostModel, RandomForestModel, RidgeRegressionModel,StackingModel
from wf_ml_prediction import XGBoostPred
import pickle
import numpy as np
import pandas as pd
import xgboost as xgb

#processs data a little bit due to initial outputs of models and scaling as needed
def process(df):

    df = outliers(df, 'TIM_MIN')
    df = outliers(df, 'temperature_2m (°C)')
    df = df.dropna().reset_index(drop=True)

    scaler = StandardScaler()
    df[['Latitude', 'Longitude','rain (mm)','temperature_2m (°C)']] = scaler.fit_transform(df[['Latitude', 'Longitude','rain (mm)','temperature_2m (°C)']])
    with open('models/scaler_latlong.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    scaler1 = StandardScaler()
    df[['TIM_MIN']] = scaler1.fit_transform(df[['TIM_MIN']])
    with open('models/scaler_latlong1.pkl', 'wb') as f:
            pickle.dump(scaler1, f)

    df['date'] = pd.to_datetime(df['date'])
    df['day'] = df['date'].dt.day

    df['CIP_JOBS_Enc'] = LabelEncoder().fit_transform(df['CIP_JOBS'])
    df = df.drop(columns=['CAD_EVNT_ID', 'CREATE_DATE', 'date', 'CIP_JOBS', 'INCDENT_TMSTMP', 
                          'CLOSNG_TS', 'GEO_CD_X', 'GEO_CD_Y', 'precipitation (mm)', 
                          'RADIO_CODE', 'REASON', 'ADD_TS', 'DISP_TS', 'CLOSNG_TS', 
                          'ARRIVD_TS', 'REAS_CTGRY'])

    df = encode(df, ['BORO_NM', 'PATRL_BORO_NM', 'NYPD_PCT_CD'])

    return df

def outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def encode(df, columns):
    encoder = OneHotEncoder(sparse_output=False)
    for column in columns:
        encoded_array = encoder.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out([column]))
        df = pd.concat([df, encoded_df], axis=1).drop(column, axis=1)
    return df

# splitting data and saving it into data_processed
def traintest(df):
  
    X = df.drop(columns=['TIM_MIN'])
    y = df['TIM_MIN']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    train_data = X_train.copy()
    train_data['TIM_MIN'] = y_train

    test_data = X_test.copy()
    test_data['TIM_MIN'] = y_test

    train_data.to_csv('data_processed/train_data.csv', index=False)
    with open('models/feature_columns.pkl', 'wb') as f: #new line
        pickle.dump(X_train.columns.tolist(), f)
    test_data.to_csv('data_processed/test_data.csv', index=False)

def main():
    df = pd.read_csv("data_processed/PreProcessedDataset.csv")
    readydata = process(df)
    traintest(readydata)
    
# common function to write metrics into summar.txt file
# using saved scaler the errors are being evaluated after scaling it down
def error_metrics(model_name, y_test, y_pred):

    with open('models/scaler_latlong1.pkl', 'rb') as scaler_file:
        scaler1 = pickle.load(scaler_file)

    y_test = np.array(y_test).reshape(-1, 1)
    y_pred = np.array(y_pred).reshape(-1, 1) 

    y_test_original = scaler1.inverse_transform(y_test) 
    y_pred_original = scaler1.inverse_transform(y_pred) 

    mae = mean_absolute_error(y_test_original, y_pred_original)
    rmse = np.sqrt(root_mean_squared_error(y_test_original, y_pred_original)) 
    r2 = r2_score(y_test_original, y_pred_original)

    metrics_row = f"{model_name}\t\t{mae:.4f}\t{rmse:.4f}\t{r2:.4f}\n"
    with open('evaluation/summary.txt', 'a') as file:
        if file.tell() == 0:
            file.write("Model(Evaluation)\t\tMAE\t\tRMSE\t\tR^2\n")
        file.write(metrics_row)

# evaluation of xbgoost model 
def XGBoostEvaluation():
    model = xgb.XGBRegressor()
    model.load_model('models/xgboost_model.bst')

    test_data = pd.read_csv('data_processed/test_data.csv')
    X_test = test_data.drop(columns=['TIM_MIN']) 
    y_test = test_data['TIM_MIN']  

    y_pred = model.predict(X_test)

    error_metrics("XGBoost   (Model)", y_test, y_pred)

# evaluation of randomforest model 
def RandomForestEval():

    with open('models/random_forest_model.pkl', 'rb') as model_file:
        rf_model = pickle.load(model_file)
    
    test_data = pd.read_csv('data_processed/test_data.csv') 
    X_test = test_data.drop(columns=['TIM_MIN']) 
    y_test = test_data['TIM_MIN']  
    y_pred = rf_model.predict(X_test)

    error_metrics("RandomForest (RF)", y_test, y_pred)

# evaluation of ridge model 
def RidgeRegressionEval():

    with open('models/ridgeregression.pkl', 'rb') as model_file:
        ridge_model = pickle.load(model_file)

    test_data = pd.read_csv('data_processed/test_data.csv') 
    X_test = test_data.drop(columns=['TIM_MIN']) 
    y_test = test_data['TIM_MIN']  
    y_pred = ridge_model.predict(X_test)

    error_metrics("Ridge  Regression", y_test, y_pred)

# evaluation of stacking model 
def StackingEval():
     
    with open('models/stackingmodel.pkl', 'rb') as model_file:
        stacking_model = pickle.load(model_file)

    test_data = pd.read_csv('data_processed/test_data.csv') 
    X_test = test_data.drop(columns=['TIM_MIN']) 
    y_test = test_data['TIM_MIN']  
    y_pred = stacking_model.predict(X_test)

    error_metrics("Stacking -  Model", y_test, y_pred)

if __name__ == "__main__":

    raw_input = {
        'CAD_EVNT_ID':103529625,'CREATE_DATE':'5/31/2024','INCDENT_TMSTMP':'5/31/2024 22:27','NYPD_PCT_CD':70,
        'BORO_NM':'BROOKLYN','PATRL_BORO_NM':'PATROL BORO BKLYN SOUTH','GEO_CD_X':997339,'GEO_CD_Y':164281,
        'RADIO_CODE':'10P2','REAS_CTGRY':'INVESTIGATE/POSSIBLE CRIME','REASON':'SUSP PERSON/OUTSIDE (PROWLER)',
        'CIP_JOBS':'Non CIP','ADD_TS':'5/31/2024 22:27','DISP_TS':'6/1/2024 0:21','ARRIVD_TS':'6/1/2024 3:09',
        'TIM_MIN':168,'CLOSNG_TS':'6/1/2024 3:12','Latitude':40.617588,'Longitude':-73.952855,'date':'6/1/2024',
        'hour':0,'temperature_2m (°C)':16.2,'precipitation (mm)':0,'rain (mm)':0
    }
    raw_input2 = {
        'CAD_EVNT_ID':103531241,'CREATE_DATE':'5/31/2024','INCDENT_TMSTMP':'5/31/2024 23:40','NYPD_PCT_CD':115,
        'BORO_NM':'QUEENS','PATRL_BORO_NM':'PATROL BORO QUEENS NORTH','GEO_CD_X':1020196,'GEO_CD_Y':214821,
        'RADIO_CODE':'52K6','REAS_CTGRY':'DISPUTE','REASON':'KNIFE/FAMILY',
        'CIP_JOBS':'Non CIP','ADD_TS':'5/31/2024 23:40','DISP_TS':'6/1/2024 0:31','ARRIVD_TS':'6/1/2024 0:33',
        'TIM_MIN':1.85,'CLOSNG_TS':'6/1/2024 0:38','Latitude':40.756246,'Longitude':-73.870254,'date':'6/1/2024',
        'hour':0,'temperature_2m (°C)':16.3,'precipitation (mm)':0,'rain (mm)':0
    }

    main()
    XGBoostModel()
    predicted_value = XGBoostPred(raw_input)
    predicted_value2 = XGBoostPred(raw_input2)
    print(f"Response time for input1: {predicted_value} minutes")
    print(f"Response time for input2: {predicted_value2} minutes")
    XGBoostEvaluation()

    RandomForestModel()
    RandomForestEval()

    RidgeRegressionModel()
    RidgeRegressionEval()
    
    StackingModel()
    StackingEval()