import streamlit as st


# Sidebar for navigation
st.sidebar.title("📍 Navigation")
options = ["📊 View Expenses", "🔮 Predict Expenses"]
choice = st.sidebar.radio("Go to:", options)

