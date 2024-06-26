import requests
import pandas as pd
import zipfile
import sqlite3
import io

def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return io.BytesIO(response.content)
    else:
        print("Failed to download data.")
        return None

def extract_data(zip_file):
    with zipfile.ZipFile(zip_file) as zip_ref:
        for file_name in zip_ref.namelist():
            if file_name.endswith('.csv') and 'Metadata' not in file_name:
                with zip_ref.open(file_name) as csv_file:
                    return pd.read_csv(csv_file, skiprows=4)

def clean_data(df):
  
    df.dropna(axis=1, how='all', inplace=True)
    #print("Columns with all NaN values are dropped.")

    df = df.loc[df.notna().all(axis=1)]
    print("Rows with any NaN values are dropped.")

    # Select specific columns to keep
    columns_to_keep = ['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'] + \
                      [str(year) for year in range(1990, 2021)]
    df = df[columns_to_keep]

    df.reset_index(drop=True, inplace=True)
    print("Number of columns:", df.shape[1])  
    return df



def store_data(df, database_path, table_name):
    conn = sqlite3.connect(database_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"Data pipeline executed successfully. Cleaned data stored at {database_path}\n")

def main():
    # Step 1: Pull the Data
    co2_url = "https://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.KT?downloadformat=csv"
    population_url = "https://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
    
    co2_zip_file = download_data(co2_url)
    if co2_zip_file:
        co2_df = extract_data(co2_zip_file)
        if co2_df is not None:
            #print(co2_df.info())
            #print(co2_df.columns)
            co2_df = clean_data(co2_df)
            database_path = ":memory:"  # Using in-memory database for demonstration
            store_data(co2_df, database_path, 'co2_emissions')


    population_zip_file = download_data(population_url)
    if population_zip_file:
        population_df = extract_data(population_zip_file)
        if population_df is not None:
            #print(population_df.info())
            #print(population_df.columns)
            population_df = clean_data(population_df)
            database_path = ":memory:"  # Using in-memory database for demonstration
            store_data(population_df, database_path, 'population')

if __name__ == "__main__":
    main()
