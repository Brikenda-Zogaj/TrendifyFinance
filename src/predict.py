import numpy as np
import pandas as pd
import joblib
import os

MODEL_PATH = "../models/trend_model.pkl"
DATA_PATH = "./data/preprocessed_data.csv"


def predict_next_expense(days=5):
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
    latest_expense = df["Amount"].iloc[-1:].values.reshape(1,-1)
    predictions = []

    for _ in range(days):
        next_expense = model.predict(latest_expense)[0]
        predictions.append(next_expense)
        latest_expense = np.array([[next_expense]])


    print(f"Predicted next {days} days:")
    for i, pred in enumerate(predictions, 1):
        print(f"Day {i}: {pred:.2f} €")

    return predictions




