"""
Pandas Lesson 17: Working with CSV Files
Learn how to read from and write to CSV files with various options
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 17: Working with CSV Files"""
    print("\n" + "="*60)
    print("LESSON 17: CSV OPERATIONS")
    print("="*60)
    
    # Create sample data
    df = pd.DataFrame({
        'EmployeeID': [1, 2, 3, 4, 5],
        'Name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Lee', 'Eve Wilson'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
        'Salary': [70000, 60000, 75000, 90000, 65000],
        'JoinDate': pd.date_range('2020-01-01', periods=5, freq='6M')
    })
    
    print("\n1. Sample DataFrame to save:")
    print(df)
    
    # Save to CSV
    print("\n2. Saving to CSV (employees.csv)...")
    df.to_csv('employees.csv', index=False)
    print("✓ Saved successfully!")
    
    # Read from CSV
    print("\n3. Reading from CSV:")
    df_read = pd.read_csv('employees.csv')
    print(df_read)
    
    # CSV with custom delimiter
    print("\n4. Save with semicolon delimiter:")
    df.to_csv('employees_semicolon.csv', sep=';', index=False)
    df_semicolon = pd.read_csv('employees_semicolon.csv', sep=';')
    print(df_semicolon.head())
    
    # Read specific columns
    print("\n5. Read only specific columns:")
    df_subset = pd.read_csv('employees.csv', usecols=['Name', 'Department', 'Salary'])
    print(df_subset)
    
    # Read with date parsing
    print("\n6. Read with date parsing:")
    df_dates = pd.read_csv('employees.csv', parse_dates=['JoinDate'])
    print(df_dates.dtypes)


if __name__ == "__main__":
    main()
