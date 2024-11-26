from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pickle
import xgboost as xgb
import pandas as pd
import numpy as np

def XGBoostPred(raw_input):
     
    def process(df):
        with open('models/scaler_latlong.pkl', 'rb') as scaler_file:
            scaler = pickle.load(scaler_file)

        # df[['Latitude', 'Longitude','rain (mm)','temperature_2m (°C)']] = scaler.fit_transform(df[['Latitude', 'Longitude','rain (mm)','temperature_2m (°C)']])
        df[['Latitude', 'Longitude','rain (mm)','temperature_2m (°C)']] = scaler.transform(df[['Latitude', 'Longitude','rain (mm)','temperature_2m (°C)']])


        with open('models/scaler_latlong1.pkl', 'rb') as scaler_file:
            scaler1 = pickle.load(scaler_file)

        # df[['TIM_MIN']] = scaler1.fit_transform(df[['TIM_MIN']])

        df['date'] = pd.to_datetime(df['date'])
        df['day'] = df['date'].dt.day

        df['CIP_JOBS_Enc'] = LabelEncoder().fit_transform(df['CIP_JOBS'])
        df = df.drop(columns=['CAD_EVNT_ID', 'CREATE_DATE', 'date', 'CIP_JOBS', 'INCDENT_TMSTMP', 
                            'CLOSNG_TS', 'GEO_CD_X', 'GEO_CD_Y', 'precipitation (mm)', 
                            'RADIO_CODE', 'REASON', 'ADD_TS', 'DISP_TS', 'CLOSNG_TS', 
                            'ARRIVD_TS', 'REAS_CTGRY'])

        df = encode(df, ['BORO_NM', 'PATRL_BORO_NM', 'NYPD_PCT_CD'])

        return df
    
    def encode(df, columns):
        encoder = OneHotEncoder(sparse_output=False)
        for column in columns:
            encoded_array = encoder.fit_transform(df[[column]])
            encoded_df = pd.DataFrame(encoded_array, columns=encoder.get_feature_names_out([column]))
            df = pd.concat([df, encoded_df], axis=1).drop(column, axis=1)
        return df

    df = pd.DataFrame([raw_input])

    output_df = process(df)

    # expected_columns = [
    #     "Latitude", "Longitude", "hour", "temperature_2m (°C)", "rain (mm)", "day", "CIP_JOBS_Enc",
    #     "BORO_NM_BRONX", "BORO_NM_BROOKLYN", "BORO_NM_MANHATTAN", "BORO_NM_QUEENS", "BORO_NM_STATEN ISLAND",
    #     "PATRL_BORO_NM_PATROL BORO BKLYN NORTH", "PATRL_BORO_NM_PATROL BORO BKLYN SOUTH",
    #     "PATRL_BORO_NM_PATROL BORO BRONX", "PATRL_BORO_NM_PATROL BORO MAN NORTH",
    #     "PATRL_BORO_NM_PATROL BORO MAN SOUTH", "PATRL_BORO_NM_PATROL BORO QUEENS NORTH",
    #     "PATRL_BORO_NM_PATROL BORO QUEENS SOUTH", "PATRL_BORO_NM_PATROL BORO STATEN ISLAND",
    #     "NYPD_PCT_CD_1", "NYPD_PCT_CD_5", "NYPD_PCT_CD_6", "NYPD_PCT_CD_7", "NYPD_PCT_CD_9",
    #     "NYPD_PCT_CD_10", "NYPD_PCT_CD_13", "NYPD_PCT_CD_14", "NYPD_PCT_CD_17", "NYPD_PCT_CD_18",
    #     "NYPD_PCT_CD_19", "NYPD_PCT_CD_20", "NYPD_PCT_CD_22", "NYPD_PCT_CD_23", "NYPD_PCT_CD_24",
    #     "NYPD_PCT_CD_25", "NYPD_PCT_CD_26", "NYPD_PCT_CD_28", "NYPD_PCT_CD_30", "NYPD_PCT_CD_32",
    #     "NYPD_PCT_CD_33", "NYPD_PCT_CD_34", "NYPD_PCT_CD_40", "NYPD_PCT_CD_41", "NYPD_PCT_CD_42",
    #     "NYPD_PCT_CD_43", "NYPD_PCT_CD_44", "NYPD_PCT_CD_45", "NYPD_PCT_CD_46", "NYPD_PCT_CD_47",
    #     "NYPD_PCT_CD_48", "NYPD_PCT_CD_49", "NYPD_PCT_CD_50", "NYPD_PCT_CD_52", "NYPD_PCT_CD_60",
    #     "NYPD_PCT_CD_61", "NYPD_PCT_CD_62", "NYPD_PCT_CD_63", "NYPD_PCT_CD_66", "NYPD_PCT_CD_67",
    #     "NYPD_PCT_CD_68", "NYPD_PCT_CD_69", "NYPD_PCT_CD_70", "NYPD_PCT_CD_71", "NYPD_PCT_CD_72",
    #     "NYPD_PCT_CD_73", "NYPD_PCT_CD_75", "NYPD_PCT_CD_76", "NYPD_PCT_CD_77", "NYPD_PCT_CD_78",
    #     "NYPD_PCT_CD_79", "NYPD_PCT_CD_81", "NYPD_PCT_CD_83", "NYPD_PCT_CD_84", "NYPD_PCT_CD_88",
    #     "NYPD_PCT_CD_90", "NYPD_PCT_CD_94", "NYPD_PCT_CD_100", "NYPD_PCT_CD_101", "NYPD_PCT_CD_102",
    #     "NYPD_PCT_CD_103", "NYPD_PCT_CD_104", "NYPD_PCT_CD_105", "NYPD_PCT_CD_106", "NYPD_PCT_CD_107",
    #     "NYPD_PCT_CD_108", "NYPD_PCT_CD_109", "NYPD_PCT_CD_110", "NYPD_PCT_CD_111", "NYPD_PCT_CD_112",
    #     "NYPD_PCT_CD_113", "NYPD_PCT_CD_114", "NYPD_PCT_CD_115", "NYPD_PCT_CD_120", "NYPD_PCT_CD_121",
    #     "NYPD_PCT_CD_122", "NYPD_PCT_CD_123"
    # ]

    # for column in expected_columns:
    #         if column not in output_df.columns:
    #             output_df[column] = 0

    # output_df = output_df[expected_columns]
    with open('models/feature_columns.pkl', 'rb') as f:
        expected_columns = pickle.load(f)
    output_df = output_df.reindex(columns=expected_columns, fill_value=0)

    model = xgb.XGBRegressor()
    model.load_model('models/xgboost_model.bst')
        
    row_input = output_df.values.reshape(1, -1)
    prediction = model.predict(row_input)

    with open('models/scaler_latlong1.pkl', 'rb') as scaler_file:
        scaler1 = pickle.load(scaler_file)

    y_pred = np.array([prediction])
    y_pred_reshaped = y_pred.reshape(-1, 1) 

    y_pred_original = scaler1.inverse_transform(y_pred_reshaped)

    return y_pred_original[0][0]