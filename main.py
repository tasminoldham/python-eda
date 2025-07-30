from clean_library_books import *
from clean_library_customers import *
from import_csvs_to_database import *

def main():
    pass

    # Load cleaned books data
    clean_books("03_Library Systembook.csv", "cleaned_library_books.csv")

    # Load cleaned customers data
    clean_customers("03_Library SystemCustomers.csv", "cleaned_library_customers.csv")

    # Load clean books to SQL Server
    load_csv_to_sqlalchemy("cleaned_library_books.csv", "CleanedLibraryBooks")

    # Load clean customers to SQL Server
    load_csv_to_sqlalchemy("cleaned_library_customers.csv", "CleanedLibraryCustomers")

if __name__ == '__main__':
    main()