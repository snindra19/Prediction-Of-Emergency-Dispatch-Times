from wf_dataprocessing import preprocessing 
from wf_visualization import compute_quantstats,compute_qualstats,correlation_matrix,histograms
from wf_visualization import scatterforLatitude,scatterforLong,scatterforTemp,scatterforTime
import pandas as pd

def main():
    print("Processing data...")
    preprocessing() 

    print("Generating visuals...")
    df=pd.read_csv('data_processed/PreProcessedDataset.csv')
    quantcolumns = ['Latitude', 'Longitude', 'TIM_MIN', 'temperature_2m (°C)','rain (mm)']
    compute_quantstats(df, quantcolumns)
    qualcolumns = ['REAS_CTGRY', 'PATRL_BORO_NM', 'NYPD_PCT_CD', 'BORO_NM']
    compute_qualstats(df, qualcolumns)
    correlation_matrix(df)
    histograms(df)

    scatterforLatitude(df)
    scatterforLong(df)
    scatterforTemp(df)
    scatterforTime(df)

    print("Workflow completed.")

if __name__ == "__main__":
    main()
