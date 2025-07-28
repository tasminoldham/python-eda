import pandas as pd

def load_data(filepath):
    print("[1] Loading data...")
    df = pd.read_csv(filepath)
    print(f"    → Loaded {len(df)} rows.")
    return df

# CLEANING #

# Strip Whitespace and Standardize Column Names #

def standardize_columns(df):
    print("[2] Standardizing column names...")
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]
    return df

# Clean the dates #

def clean_dates(df):
    print("[3] Cleaning and converting date columns...")
    df['book_checkout'] = df['book_checkout'].str.replace('"', '').str.strip()
    df['book_returned'] = df['book_returned'].str.replace('"', '').str.strip()

    df['book_checkout'] = pd.to_datetime(df['book_checkout'], dayfirst=True, errors='coerce')
    df['book_returned'] = pd.to_datetime(df['book_returned'], dayfirst=True, errors='coerce')

    invalid_dates = df['book_checkout'].isna().sum() + df['book_returned'].isna().sum()
    print(f"    → Invalid date entries: {invalid_dates}")
    return df

# Convert days_allowed_to_borrow column as numeric # 

def convert_days_allowed(df):
    print("[4] Converting 'days_allowed_to_borrow' to numeric...")
    df['days_allowed_to_borrow'] = df['days_allowed_to_borrow'].str.extract(r'(\d+)').astype(float)
    return df

# Drop Rows with Critical Missing Data #

def drop_missing_essentials(df):
    print("[5] Dropping rows with missing essential data...")
    before = len(df)
    df = df.dropna(subset=['book_checkout', 'book_returned', 'customer_id', 'books'])
    after = len(df)
    print(f"    → Dropped {before - after} rows.")
    return df

# Remove Nonsense or Reversed Dates #

def remove_bad_dates(df):
    print("[6] Removing rows with reversed or future dates...")
    before = len(df)
    df = df[df['book_returned'] >= df['book_checkout']]
    df = df[df['book_checkout'] <= pd.Timestamp.today()]
    after = len(df)
    print(f"    → Removed {before - after} rows.")
    return df

# Calculate if overdue # 

def calculate_borrow_stats(df):
    print("[7] Calculating borrow duration and overdue status...")
    df['days_borrowed'] = (df['book_returned'] - df['book_checkout']).dt.days
    df['is_overdue'] = df['days_borrowed'] > df['days_allowed_to_borrow']
    return df

def save_cleaned_data(df, output_file):
    print("[8] Saving cleaned data to CSV...")
    df = df.reset_index(drop=True)
    df.to_csv(output_file, index=False)
    print(f"    → File saved: {output_file}")

def main():
    input_file = "03_Library Systembook.csv"
    output_file = "cleaned_library_books.csv"

    df = load_data(input_file)
    df = standardize_columns(df)
    df = clean_dates(df)
    df = convert_days_allowed(df)
    df = drop_missing_essentials(df)
    df = remove_bad_dates(df)
    df = calculate_borrow_stats(df)
    save_cleaned_data(df, output_file)


if __name__ == "__main__":
    main()
