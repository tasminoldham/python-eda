import unittest
import pandas as pd
from clean_library_books import calculate_borrow_stats
from clean_library_customers import standardize_columns


class TestCalculateBorrowStats(unittest.TestCase):

    def test_borrow_stats(self):
        # Sample data
        data = {
            'book_checkout': [pd.to_datetime('2023-01-01'), pd.to_datetime('2023-01-10')],
            'book_returned': [pd.to_datetime('2023-01-15'), pd.to_datetime('2023-01-12')],
            'days_allowed_to_borrow': [10, 1]
        }
        df = pd.DataFrame(data)

        # Expected outputs:
        # Row 1: 14 days borrowed, allowed 10 → overdue: True
        # Row 2: 2 days borrowed, allowed 1 → overdue: True
        expected_days_borrowed = [14, 2]
        expected_is_overdue = [True, True]

        # Run the function
        result_df = calculate_borrow_stats(df)

        # Check days_borrowed
        self.assertListEqual(result_df['days_borrowed'].tolist(), expected_days_borrowed)

        # Check is_overdue
        self.assertListEqual(result_df['is_overdue'].tolist(), expected_is_overdue)

class TestStandardizeColumns(unittest.TestCase):

    def test_column_standardization(self):
        # Create sample dataframe with messy column names
        data = {
            ' Book Title ': ['Python 101'],
            'Checked Out By': ['Alice'],
            'Return Date ': ['2023-01-10']
        }
        df = pd.DataFrame(data)

        # Expected column names after standardizing
        expected_columns = ['book_title', 'checked_out_by', 'return_date']

        # Run the function
        result_df = standardize_columns(df)

        # Check if columns match
        self.assertListEqual(
            result_df.columns.tolist(),
            expected_columns,
            msg="Test failed: Column names were not standardized correctly"
        )

if __name__ == '__main__':
    unittest.main()