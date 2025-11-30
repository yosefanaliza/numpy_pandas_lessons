"""
Pandas Lesson 6: Creating DataFrames from CSV Files
Learn how to read CSV files and explore the data
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 6: Creating DataFrames from CSV Files"""
    print("\n" + "="*60)
    print("LESSON 6: CREATING DATAFRAMES FROM CSV FILES")
    print("="*60)
    
    # Check if dummy_data.csv exists, if not create it
    try:
        df = pd.read_csv('dummy_data.csv')
    except FileNotFoundError:
        print("Creating dummy_data.csv...")
        dummy_data = {
            'ID': range(1, 11),
            'Name': [f'Person_{i}' for i in range(1, 11)],
            'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
            'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney', 
                    'Berlin', 'Madrid', 'Rome', 'Toronto', 'Dubai'],
            'Salary': [50000, 60000, 55000, 70000, 65000, 58000, 62000, 59000, 61000, 68000]
        }
        dummy_df = pd.DataFrame(dummy_data)
        dummy_df.to_csv('dummy_data.csv', index=False)
        df = pd.read_csv('dummy_data.csv')
    
    print("\n1. Reading CSV file:")
    print(df)
    
    print("\n2. DataFrame info:")
    print(df.info())
    
    print("\n3. First 3 rows:")
    print(df.head(3))
    
    print("\n4. Last 3 rows:")
    print(df.tail(3))
    
    print("\n5. Statistical summary:")
    print(df.describe())
    
    print("\n6. Column names:")
    print(df.columns.tolist())
    
    print("\n7. Filter: Age > 30:")
    print(df[df['Age'] > 30])


if __name__ == "__main__":
    main()
