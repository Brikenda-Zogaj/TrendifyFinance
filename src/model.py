import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Load cleaned data
DATA_PATH = "../data/cleaned_data.csv"

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}. Run data preprocessing first.")

df = pd.read_csv(DATA_PATH)


if 'Amount' not in df.columns:
    raise ValueError("Expected column 'Amount' not found in dataset.")

X = df[['Amount']]
y = df['Amount'].shift(-1).fillna(df['Amount'].mean())

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Model Evaluation:\nMAE: {mae:.2f}\nMSE: {mse:.2f}")

# Save model
MODEL_PATH = "../models/trend_model.pkl"
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(model, MODEL_PATH)

print(f"Model saved to {MODEL_PATH}")
