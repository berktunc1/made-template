import requests
import pandas as pd
import zipfile
import sqlite3
import os

def download_data(url, zip_file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(zip_file_path, "wb") as f:
            f.write(response.content)
        return True
    else:
        print("Failed to download data.")
        return False

def extract_data(zip_file_path, extraction_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extraction_path)

def load_data(data_folder):
    for file in os.listdir(data_folder):
        if file.endswith(".csv") and "Metadata" not in file:
            data_file_path = os.path.join(data_folder, file)
            return pd.read_csv(data_file_path, skiprows=4)

def clean_data(df):
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(thresh=5, inplace=True)
    print("Number of rows with NaN values: ",df.isnull().sum().sum())
    df.dropna(inplace=True)
    print("New number of rows with NaN values: ",df.isnull().sum().sum())
    print("\nTotal number of zero values in the DataFrame:", (df == 0).sum().sum())
    df = df[(df != 0).all(axis=1)]
    print("\nNew total number of zero values in the DataFrame:", (df == 0).sum().sum())
    df.reset_index(drop=True, inplace=True)

    print("\n\nDataFrame after cleaning:")
    print(df.info())
    print(df.columns)
    return df

def store_data(df, database_path,table_name):
    conn = sqlite3.connect(database_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data pipeline executed successfully. Cleaned data stored at {database_path}")

def main():
    # Step 1: Pull the Data
    url = "https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv"
    zip_file_path = "datasets/final/worldbank_co2_emissions.zip"
    if download_data(url, zip_file_path):
        # Step 2: Extract and Transform the Data
        extraction_path = "datasets/final"
        extract_data(zip_file_path, extraction_path)
        df = load_data(extraction_path)
        if df is not None:
            print(df.info())
            print(df.columns)
            df = clean_data(df)

            # Step 3: Store the Data in SQLite
            database_path = "datasets/final/co2_emissions.sqlite"
            store_data(df, database_path, 'co2_emissions')

    # Step 1: Pull the Data
    url = "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
    zip_file_path = "datasets/final2/population.zip"
    if download_data(url, zip_file_path):
        # Step 2: Extract and Transform the Data
        extraction_path = "datasets/final2"
        extract_data(zip_file_path, extraction_path)
        df = load_data(extraction_path)
        if df is not None:
            print(df.info())
            print(df.columns)
            df = clean_data(df)

            # Step 3: Store the Data in SQLite
            database_path = "datasets/final2/population.sqlite"
            store_data(df, database_path, 'population')


if __name__ == "__main__":
    main()
