import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(df):

    # This convert 'Date' to datetime (nese ekziston)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
     # This convert numeric columns (injoron stringjet)
    for col in df.select_dtypes(include=['object']).columns:
        if col != 'Date':
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # This fill missing values (vetem numeric values)
    df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)

    # Normalize numerical values (if needed)
    numerical_features = ["Amount"]
    scaler = StandardScaler()
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    print("Data preprocessing completed!")
    return df

if __name__ == "__main__":
    file_path = "../data/cleaned_data.csv"
    df = pd.read_csv(file_path)
    df = preprocess_data(df)
    df.to_csv("../data/preprocessed_data.csv", index=False)
    print("Preprocessed data saved!")