import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

def compute_quantstats(df, columns):
    with open('data_processed/summary.txt', 'w') as file:
        for column in columns:
            if column in df.columns:
                min_value = df[column].min()
                max_value = df[column].max()
                median_value = df[column].median()
                mean_value = df[column].mean()

                file.write(f"Summary Statistics for '{column}':\n")
                file.write(f"  Min: {min_value}\n")
                file.write(f"  Max: {max_value}\n")
                file.write(f"  Median: {median_value}\n")
                file.write(f"  Mean: {mean_value}\n")
                file.write("\n")
                
def compute_qualstats(df, columns):
    df['NYPD_PCT_CD'] = df['NYPD_PCT_CD'].astype(str)
    with open('data_processed/summary.txt', 'a') as file:
        for column in columns:
            if column in df.columns:
                unique_count = df[column].nunique()
                most_frequent = df[column].mode()[0] 
                least_frequent = df[column].value_counts().idxmin() 

                # Append the statistics to the file
                file.write(f"Summary Statistics for '{column}':\n")
                file.write(f"  Number of unique values: {unique_count}\n")
                file.write(f"  Most frequent value: {most_frequent}\n")
                file.write(f"  Least frequent value: {least_frequent}\n\n") 

def correlation_matrix(df):

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = df[numerical_cols].corr()
    lower_triangle = correlation_matrix.where(np.tril(np.ones(correlation_matrix.shape), k=0).astype(bool))
    with open('data_processed/correlations.txt', 'w') as file:
        file.write(lower_triangle.to_string())

def histograms(df):
    
    plt.figure(figsize=(8, 6))
    sns.histplot(df['REAS_CTGRY'], bins=4, color='blue')
    plt.title('Histogram of Categories')
    plt.xlabel('Categories')
    plt.ylabel('Frequency')
    plt.xticks(rotation=90)
    plt.savefig('visuals/ReasonHist.png', format='png')

    plt.figure(figsize=(12, 12))
    sns.histplot(df['PATRL_BORO_NM'], bins=4, color='green')
    plt.title('Histogram of Patrol Units Borough')
    plt.xlabel('Patrol Unit Borough')
    plt.ylabel('Frequency')
    plt.xticks(rotation=35)
    plt.savefig('visuals/PatrolBoroHist.png', format='png')

    plt.figure(figsize=(8, 6))
    sns.histplot(df['BORO_NM'], bins=4, color='brown')
    plt.title('Histogram of Boroughs')
    plt.xlabel('Borough')
    plt.ylabel('Frequency')
    plt.savefig('visuals/BoroHist.png', format='png')

    df['NYPD_PCT_CD'] = pd.to_numeric(df['NYPD_PCT_CD'], errors='coerce')
    sorted_values = np.sort(df['NYPD_PCT_CD'])
    y=sorted_values.astype(str)
    plt.figure(figsize=(13, 6))
    sns.histplot(y, bins=200, color='orange')
    plt.title('Histogram of Precinct Number')
    plt.xlabel('Precinct Number')
    plt.ylabel('Frequency')
    plt.xticks(rotation=90)
    plt.savefig('visuals/PrecinctHist.png', format='png')

def scatterforLatitude(df):

    columns_to_compare = ['Longitude', 'temperature_2m (°C)','TIM_MIN','rain (mm)']
    fig, axes = plt.subplots(2, 2, figsize=(10, 10)) 
    axes = axes.flatten()
    for i, column in enumerate(columns_to_compare):
        axes[i].scatter(df['Latitude'], df[column], color='blue', alpha=0.7)
        axes[i].set_title(f'Scatter plot of Latitude vs {column}')
        axes[i].set_xlabel('Latitude')
        axes[i].set_ylabel(column)

    plt.tight_layout()
    plt.savefig('visuals/scatterforLatitude.png', format='png', dpi=300, bbox_inches='tight')

def scatterforLong(df):
    
    columns_to_compare = ['temperature_2m (°C)','rain (mm)']
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes = axes.flatten()
    for i, column in enumerate(columns_to_compare):
        axes[i].scatter(df['Longitude'], df[column], color='green', alpha=0.7)
        axes[i].set_title(f'Scatter plot of Longitude vs {column}')
        axes[i].set_xlabel('Longitude')
        axes[i].set_ylabel(column)

    plt.tight_layout()
    plt.savefig('visuals/scatterforLong.png', format='png', dpi=300, bbox_inches='tight')

def scatterforTemp(df):

    columns_to_compare = ['rain (mm)','TIM_MIN']
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes = axes.flatten()
    for i, column in enumerate(columns_to_compare):
        axes[i].scatter(df['temperature_2m (°C)'], df[column], color='orange', alpha=0.7)
        axes[i].set_title(f'Scatter plot of Temperature vs {column}')
        axes[i].set_xlabel('temperature_2m (°C)')
        axes[i].set_ylabel(column)

    plt.tight_layout()
    plt.savefig('visuals/scatterforTemp.png', format='png', dpi=300, bbox_inches='tight')

def scatterforTime(df):

    columns_to_compare = ['rain (mm)','Longitude']
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes = axes.flatten()
    for i, column in enumerate(columns_to_compare):
        axes[i].scatter(df['TIM_MIN'], df[column], color='brown', alpha=0.7)
        axes[i].set_title(f'Scatter plot of Time Taken to arrive vs {column}')
        axes[i].set_xlabel('TIM_MIN')
        axes[i].set_ylabel(column)

    plt.tight_layout()
    plt.savefig('visuals/scatterforTime.png', format='png', dpi=300, bbox_inches='tight')


if __name__ == '__main__':

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