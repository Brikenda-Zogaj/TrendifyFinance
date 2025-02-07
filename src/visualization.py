import pandas as pd
import matplotlib.pyplot as plt


def plot_expense_trend(df):
    """Plots a time series of expenses over time."""

    # Convert 'Date' column to datetime, allowing for different formats
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    # Sort by date (important for time series visualization)
    # df = df.sort_values(by='Date')
    df = df.dropna(subset=['Date', 'Amount']).sort_values(by='Date')

    if df.empty:
        print("No valid data to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Amount'], marker='o', linestyle='-')
    plt.xlabel('Date')
    plt.ylabel('Expense Amount')
    plt.title('Expense Trend Over Time')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
