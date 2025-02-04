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

if __name__ == "__main__":
    file_path = "../data/cleaned_data.csv"
    df = pd.read_csv(file_path)
    df = preprocess_data(df)
    df.to_csv("../data/preprocessed_data.csv", index=False)
    print("Preprocessed data saved!")