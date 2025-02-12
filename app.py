import streamlit as st


# Sidebar for navigation
st.sidebar.title("📍 Navigation")
options = ["📊 View Expenses", "🔮 Predict Expenses"]
choice = st.sidebar.radio("Go to:", options)

st.subheader("📊 Your Expense Data")
st.write(df.tail(10))  # Shfaq vetëm 10 të fundit


st.subheader("📈 Expense Trend")
plot_expense_trend(df)