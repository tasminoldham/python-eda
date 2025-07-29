from sqlalchemy import create_engine
import pandas as pd

def load_csv_to_sqlalchemy(file_path, table_name):
    # Load cleaned CSV
    df = pd.read_csv(file_path)

    # SQLAlchemy connection string
    connection_url = (
        "mssql+pyodbc://localhost/library"
        "?driver=ODBC+Driver+17+for+SQL+Server"
        "&trusted_connection=yes"
    )

    # Create SQLAlchemy engine
    engine = create_engine(connection_url)

    # Upload to SQL Server
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded into SQL Server table: {table_name}")


if __name__ == "__main__":
    # Load books
    load_csv_to_sqlalchemy("cleaned_library_books.csv", "CleanedLibraryBooks")

    # Load customers
    load_csv_to_sqlalchemy("cleaned_library_customers.csv", "CleanedLibraryCustomers")