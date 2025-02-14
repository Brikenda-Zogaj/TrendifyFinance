import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

# Load data
DATA_PATH = "data/cleaned_data.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    #  This convert 'Date' column to datetime format
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    return df


df = load_data()
# Sidebar for navigation
st.sidebar.title("📍 Navigation")
options = ["📊 View Expenses", "🔮 Predict Expenses"]
choice = st.sidebar.radio("Go to:", options)

if choice == "📊 View Expenses":
    st.subheader("📊 Your Expense Data")
    st.write(df.tail(10))  # This show last 10 expenses

    if "Date" in df.columns:
        min_date, max_date = df["Date"].min(), df["Date"].max()
        start_date, end_date = st.sidebar.date_input(
            "Select Date Range:", [min_date.date(), max_date.date()]
        )

        start_date, end_date = pd.to_datetime(start_date), pd.to_datetime(end_date)
        filtered_df = df[(df["Date"] >= start_date) & (df["Date"] <= end_date)]

        if filtered_df.empty:
            st.warning("⚠️ No data available for the selected date range.")
        else:

            st.subheader("📈 Expense Trend (Filtered)")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(filtered_df["Date"], filtered_df["Amount"], marker='o', linestyle='-')
            ax.set_xlabel("Date")
            ax.set_ylabel("Expense Amount (€)")
            ax.set_title("Filtered Expense Trend")
            plt.xticks(rotation=45)
            st.pyplot(fig)

elif choice == "🔮 Predict Expenses":
    from src.predict import predict_next_expense

    st.subheader("🔮 Predict Future Expenses")
    days = st.slider("Select days to predict:", min_value=1, max_value=30, value=5)

    if st.button("Predict"):
        predictions = predict_next_expense(days)
        st.write("### 📌 Predictions:")
        for i, pred in enumerate(predictions, 1):
            st.write(f"**Day {i}:** {pred:.2f} €")

st.sidebar.info("💡 Select an option from the sidebar to continue.")
