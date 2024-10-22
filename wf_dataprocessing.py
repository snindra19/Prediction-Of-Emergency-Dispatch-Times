import pandas as pd

def prepare_weather(df):
    df['time'] = df['time'].str.replace('T', ' ', regex=False)
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    df['date'] = df['time'].dt.date
    df['hour'] = df['time'].dt.hour
    return df

def preprocessing():
    file_path = "data_original/NYPD_Calls_for_Service__Year_to_Date__20241016.csv"
    df = pd.read_csv(file_path, low_memory=False)
    
    # Parse DISP_TS as datetime
    df['DISP_TS'] = pd.to_datetime(df['DISP_TS'], format="%m/%d/%Y %I:%M:%S %p", errors='coerce')
    
    # Filter for June 2024 records only
    df = df[(df['DISP_TS'].dt.month == 6) & (df['DISP_TS'].dt.year == 2024)]
    
    # due to the large size of the data i will be taking the latest months that NYPD has to offer
    # June 2024 with 608,150 records
    # reading original weather data
    file_path0 = "data_original/Bronx.csv"
    file_path1 = "data_original/Brooklyn.csv"
    file_path2 = "data_original/Manhattan.csv"
    file_path3 = "data_original/Queens.csv"
    file_path4 = "data_original/Staten Island.csv"
    
    # first three rows are irrelevant
    df0 = pd.read_csv(file_path0, skiprows=3)
    df1 = pd.read_csv(file_path1, skiprows=3)
    df2 = pd.read_csv(file_path2, skiprows=3)
    df3 = pd.read_csv(file_path3, skiprows=3)
    df4 = pd.read_csv(file_path4, skiprows=3)
    
    #dropping rows irrelevant to the analysis
    df0.to_csv("data_processed/Bronx_Weather.csv", index=False)
    df1.to_csv("data_processed/Brooklyn_Weather.csv", index=False)
    df2.to_csv("data_processed/Manhattan_Weather.csv", index=False)
    df3.to_csv("data_processed/Queens_Weather.csv", index=False)
    df4.to_csv("data_processed/StatenIsland_Weather.csv", index=False)
    
    #reading all processed weather files
    df40=pd.read_csv("data_processed/Bronx_Weather.csv")
    df41=pd.read_csv("data_processed/Brooklyn_Weather.csv")
    df42=pd.read_csv("data_processed/Manhattan_Weather.csv")
    df43=pd.read_csv("data_processed/Queens_Weather.csv")
    df44=pd.read_csv("data_processed/StatenIsland_Weather.csv")
    
    
    #to merge emergency calls with respective weather we will be using time column to split into date and hour in weather data
    df40 = prepare_weather(df40)
    df41 = prepare_weather(df41)
    df42 = prepare_weather(df42)
    df43 = prepare_weather(df43)
    df44 = prepare_weather(df44)
    
    # to merge data on date and hour we will be using dispatch time as weather data is important at dispatch time only 
    df['date'] = df['DISP_TS'].dt.date
    df['hour'] = df['DISP_TS'].dt.hour
    
    # now each weather data needs to be merged for the respective area/borough
    #so we split join for each area and then merge the entire joint data
    borough_weather_map = {
    'BRONX': df40,
    'BROOKLYN': df41,
    'MANHATTAN': df42,
    'QUEENS': df43,
    'STATEN ISLAND': df44
    }
    
    merged_list = []
    
    for boro, weather_df in borough_weather_map.items():
        boro_df = df[df['BORO_NM'] == boro].copy()
        boro_df['DISP_TS'] = pd.to_datetime(boro_df['DISP_TS'])  # safe to repeat if not done globally
        merged = pd.merge(boro_df, weather_df, on=['date', 'hour'], how='left')
        merged_list.append(merged)
    
    # concatenation of all dataframes will result in conjoined dataframe of emergency calls and respective weather data for that borough
    final_df = pd.concat(merged_list, ignore_index=True)
    
    # Convert timestamps and date to datetime
    final_df['CREATE_DATE'] = pd.to_datetime(final_df['CREATE_DATE'])
    datetime_format = "%m/%d/%Y %I:%M:%S %p"
    final_df['ADD_TS'] = pd.to_datetime(final_df['ADD_TS'], format=datetime_format, errors='coerce')
    final_df['ARRIVD_TS'] = pd.to_datetime(final_df['ARRIVD_TS'], format=datetime_format, errors='coerce')
    final_df['CLOSNG_TS'] = pd.to_datetime(final_df['CLOSNG_TS'], format=datetime_format, errors='coerce')
    
    # now the rows wont be sorted according to date so 
    final_df = final_df.sort_values(by='CREATE_DATE')
    final_df['CREATE_DATE'] = final_df['CREATE_DATE'].dt.date
    
    # since it is clear that we dont have weather data for the month of we will be dropping rows where 'time' is null
    # as time is null for all the data where dispatch was after 6/1/24 00:00
    final_df = final_df.dropna(subset=['time'])
    # Closing the call is inevitable and if its empty its a reporting error and we will drop the rows as it hinders further analysis
    final_df = final_df.dropna(subset=['CLOSNG_TS'])
    
    #All null values handled 
    # we wont be dropping arrived-ts null values because it is due to other dispatch units reaching sooner or dispatch units being called off
    # combining  incident date and time into one column (reducing columns)
    final_df['INCDENT_TMSTMP'] = final_df['INCIDENT_DATE'] + ' ' + final_df['INCIDENT_TIME']
    final_df.drop('INCIDENT_DATE', axis=1, inplace=True)
    final_df.drop('INCIDENT_TIME', axis=1, inplace=True)
    final_df.loc[:, 'INCDENT_TMSTMP'] = pd.to_datetime(final_df['INCDENT_TMSTMP'])
    
    # we count how long it took for dispatch to arrive at scene
    final_df.loc[:, 'TIM_TKN'] = final_df['ARRIVD_TS'] - final_df['DISP_TS']
    # timedelta data is converted into minutes it too for dispatch to arrive on scene
    final_df['TIM_MIN'] = final_df['TIM_TKN'].dt.total_seconds() / 60
    final_df = final_df[(final_df['TIM_MIN'] > 0) & (final_df['TIM_MIN'] < 180)]
    
    
    # now i dont need time taken in timedelta anymore so we will drop it
    final_df.drop('TIM_TKN', axis=1, inplace=True)
    
    # we can drop time as well from weather data as we already have the matching date and hour of the incident to perform analysis
    final_df.drop('time', axis=1, inplace=True)
    
    # the dataframes index is distorted so we reset its index
    final_df = final_df.reset_index(drop=True)
    
    # split type description into category and category description 
    split_desc = final_df['TYP_DESC'].str.split(':', n=1, expand=True)
    
    final_df['REAS_CTGRY'] = split_desc[0].fillna('OTHER')
    final_df['REASON'] = split_desc[1].fillna('UNKNOWN')
    
    
    # now that we have split desc into category and reason we can drop type_desc
    final_df.drop('TYP_DESC', axis=1, inplace=True)
    final_df['snow_depth (m)'].unique()
    
    # it is clear that there has been no snowfall during this month and isnt going to affect analysis
    final_df.drop('snowfall (cm)', axis=1, inplace=True)
    
    #we can drop snow depth as well since there has been no snow
    final_df.drop('snow_depth (m)', axis=1, inplace=True)
    
    
    output_file_path = 'data_processed/PreProcessedDataset.csv'
    final_df.to_csv(output_file_path, index=False)
    print(f"Final processed dataframe generated in {output_file_path}")

if __name__ == '__main__':
    preprocessing()