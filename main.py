from src.data_loader import load_data
from src.exploratory_analysis import explore_data, save_clean_data

if __name__ == "__main__":
    file_path = "data/myExpenses1.csv"  # Change this to your dataset path
    df = load_data(file_path)
    explore_data(df)
    save_clean_data(df)