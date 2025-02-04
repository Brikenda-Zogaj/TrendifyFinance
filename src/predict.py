import pandas as pd
import joblib
import os

MODEL_PATH = "../models/trend_model.pkl"
DATA_PATH = "../data/preprocessed_data.csv"


def predict_next_expense():
    """Loads the model and predicts the next expense."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Train the model first.")

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Preprocessed data not found at {DATA_PATH}. Run preprocessing first.")

    # Loads model
    model = joblib.load(MODEL_PATH)

    # Loads data
    df = pd.read_csv(DATA_PATH)

    # This select the last row for prediction
    latest_data = df.iloc[-1:].drop(columns=["Amount"])
    prediction = model.predict(latest_data)

    print(f"Predicted next expense amount: {prediction[0]:.2f}")
    return prediction[0]


if __name__ == "__main__":
    predict_next_expense()
