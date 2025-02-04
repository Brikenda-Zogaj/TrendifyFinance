import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(df):
    # Handle missing values
    df.fillna(df.mean(), inplace=True)

    # Normalize numerical values (if needed)
    numerical_features = ["Amount"]
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    print("Data preprocessing completed!")
    return df