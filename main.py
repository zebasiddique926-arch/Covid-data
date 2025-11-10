import pandas as pd
from data_load import load_data

def clean_dataframe_cases(df):
    """Cleans and standardizes the COVID cases dataframe."""
    df.columns = df.columns.str.strip().str.lower()

    rename_map = {
        "state": "state",
        "total case": "total",
        "active": "active",
        "discharged": "discharged",
        "deaths": "deaths",
    }
    df.rename(columns=rename_map, inplace=True)

    # Keep only required columns
    cols = ["state", "total", "active", "discharged", "deaths"]
    df = df[[c for c in cols if c in df.columns]]

    # Convert numeric columns safely
    for col in ["total", "active", "discharged", "deaths"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    return df

def clean_dataframe_vaccine(df):
    """Cleans and standardizes the vaccination dataframe."""
    df.columns = df.columns.str.strip().str.lower()

    rename_map = {
        "state": "state",
        "totalvacc": "total_vaccinated",
        "dose1": "dose1",
        "dose 1": "dose1",
        "dose2": "dose2",
        "dose 2": "dose2",
        "precaution": "precaution",
        "population": "population",
    }
    df.rename(columns=rename_map, inplace=True)

    # Keep only relevant columns
    cols = ["state", "total_vaccinated", "dose1", "dose2", "precaution", "population"]
    df = df[[c for c in cols if c in df.columns]]

    return df

def get_clean_data():
    """Loads, cleans, and merges both datasets."""
    file_path1 = "dataset_1.csv"
    file_path2 = "dataset_2.csv"

    df1, df2 = load_data(file_path1, file_path2)

    if df1 is None or df2 is None:
        raise FileNotFoundError("One or both CSV files are missing or invalid.")

    df1 = clean_dataframe_vaccine(df1)
    df2 = clean_dataframe_cases(df2)

    # Merge on state column
    df = pd.merge(df2, df1, on="state", how="outer")
    return df

if __name__ == "__main__":
    df = get_clean_data()
    print(df.head())
