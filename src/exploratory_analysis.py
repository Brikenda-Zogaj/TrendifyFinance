import pandas as pd
import os

def explore_data(df):
    """Prints basic info and statistics of the dataset."""
    print("\nDataset Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nBasic Statistics:")
    print(df.describe())

def save_clean_data(df, output_path="data/cleaned_data.csv"):
    """Saves cleaned DataFrame to a CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
