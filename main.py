from src.data_loader import load_data
from src.exploratory_analysis import explore_data, save_clean_data
from src.visualization import plot_expense_trend
from src.predict import predict_next_expense



if __name__ == "__main__":
    file_path = "data/myExpenses1.csv"
    df = load_data(file_path)
    explore_data(df)
    save_clean_data(df)
    plot_expense_trend(df)
    predict_next_expense()



