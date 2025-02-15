# TrendifyFinance

TrendifyFinance is a simple expense tracking and prediction tool built with Python and Streamlit.

## Features

- **Expense Tracking** - View and analyze your expenses.
- **Date Filtering** - Select a date range to filter expenses.
- **Prediction** - Predict future expenses using a machine learning model.
- **Interactive UI** - Built with Streamlit for easy use.

## Dataset

The data was sourced from Kaggle and used for this project

Dataset sources:
- `myExpenses1.csv` - Collected manually as a sample dataset.
- `cleaned_data.csv` - Processed version with missing values handled.
- `preprocessed_data.csv` - Final version used for training the machine learning model.


##  Installation & Setup

Install dependencies:

```sh
pip install pandas numpy scikit-learn joblib matplotlib streamlit
```
Run the app: 
```sh
streamlit run app.py
```
Or
```sh
python -m streamlit run app.py
```
## How it works 
- **Loads data from**  ```
   data/myExpenses.csv ```
- **Filters expenses by date**
- **Predicts future expenses using a Linear Regression model**

## Files Overview
```app.py``` - **Main UI.**

```src/data_loader.py``` - **Loads expense data.**

```src/visualization.py``` - **Plots expense trends.**

```src/predict.py``` - **Predicts future expenses.**


**More improvements and updates are planned in the future for this project.**

For more details, feel free to contact me at brikendazogajj@gmail.com. 



