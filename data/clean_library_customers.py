import pandas as pd

def load_data(filepath):
    print("[1] Loading data...")
    df = pd.read_csv(filepath)
    print(f"    → Loaded {len(df)} rows.")
    return df

def standardize_columns(df):
    print("[2] Standardizing column names...")
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    return df

def drop_missing_essentials(df):
    print("[3] Dropping rows with missing essential data...")
    before = len(df)
    df = df.dropna(subset=['customer_id', 'customer_name'])
    after = len(df)
    print(f"    → Dropped {before - after} rows.")
    return df

def save_cleaned_data(df, output_file):
    print("[4] Saving cleaned data to CSV...")
    df = df.reset_index(drop=True)
    df.to_csv(output_file, index=False)
    print(f"    → File saved: {output_file}")

def main():
    input_file = "03_Library SystemCustomers.csv"
    output_file = "cleaned_library_customers.csv"

    df = load_data(input_file)
    df = standardize_columns(df)
    df = drop_missing_essentials(df)
    save_cleaned_data(df, output_file)

if __name__ == "__main__":
    main()