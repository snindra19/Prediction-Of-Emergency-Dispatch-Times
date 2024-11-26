import xgboost as xgb
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.linear_model import Ridge
import pickle

def XGBoostModel():
    train_data = pd.read_csv('data_processed/train_data.csv')

    X_train = train_data.drop(columns=['TIM_MIN'])
    y_train = train_data['TIM_MIN']

    model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100,
                             learning_rate=0.1, max_depth=6,
                             colsample_bytree=0.8,subsample=0.8, random_state=42)

    model.fit(X_train, y_train)
    model.save_model('models/xgboost_model.bst')

def RandomForestModel():
    train_data = pd.read_csv('data_processed/train_data.csv') 
    X_train = train_data.drop(columns=['TIM_MIN'])  
    y_train = train_data['TIM_MIN'] 

    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1) 
    rf_model.fit(X_train, y_train)

    with open('models/random_forest_model.pkl', 'wb') as model_file:
        pickle.dump(rf_model, model_file)

def RidgeRegressionModel():
    train_data = pd.read_csv('data_processed/train_data.csv') 
    X_train = train_data.drop(columns=['TIM_MIN'])  
    y_train = train_data['TIM_MIN'] 

    ridge_model = Ridge(alpha=1.0, random_state=42)
    ridge_model.fit(X_train, y_train)

    with open('models/ridgeregression.pkl', 'wb') as model_file:
        pickle.dump(ridge_model, model_file)

def StackingModel():
    train_data = pd.read_csv('data_processed/train_data.csv')

    X_train = train_data.drop(columns=['TIM_MIN'])  
    y_train = train_data['TIM_MIN'] 

    base_learners = [ ('xgb', xgb.XGBRegressor(n_estimators=50, eval_metric='mlogloss')),
        ('rf', RandomForestRegressor(n_estimators=50, random_state=42))
    ]

    meta_model = Ridge() 
    stacking_model = StackingRegressor(estimators=base_learners, final_estimator=meta_model)
    #to keep track of what is running and completed
    # for name, model in base_learners:
    #     print(f"training {name}...")
    #     model.fit(X_train, y_train)
    #     print(f"{name} training completed.")
    print("training stacking model")
    stacking_model.fit(X_train, y_train)
    print("training completed")
    with open('models/stackingmodel.pkl', 'wb') as model_file:
        pickle.dump(stacking_model, model_file)