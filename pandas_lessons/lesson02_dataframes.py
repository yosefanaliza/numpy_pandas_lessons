"""
Pandas Lesson 2: Working with DataFrames
Learn how to create and work with DataFrames - the core data structure in Pandas
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 2: Working with DataFrames"""
    print("\n" + "="*60)
    print("LESSON 2: WORKING WITH DATAFRAMES")
    print("="*60)
    
    # Creating a DataFrame from a dictionary
    print("\n1. Creating DataFrame from dictionary:")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'Paris', 'London', 'Tokyo'],
        'Salary': [70000, 80000, 75000, 90000]
    }
    df = pd.DataFrame(data)
    print(df)
    
    # Creating DataFrame from list of dictionaries
    print("\n2. DataFrame from list of dictionaries:")
    students = [
        {'Name': 'Emma', 'Math': 85, 'Science': 92},
        {'Name': 'Frank', 'Math': 90, 'Science': 87},
        {'Name': 'Grace', 'Math': 88, 'Science': 91}
    ]
    df_students = pd.DataFrame(students)
    print(df_students)
    
    # DataFrame attributes
    print("\n3. DataFrame attributes:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(f"Index: {df.index.tolist()}")
    print(f"\nData types:\n{df.dtypes}")
    
    # Basic information
    print("\n4. DataFrame info:")
    print(df.info())
    
    # Statistical summary
    print("\n5. Statistical summary:")
    print(df.describe())
    
    # Accessing columns
    print("\n6. Accessing columns:")
    print(df['Name'])
    print("\n7. Multiple columns:")
    print(df[['Name', 'Age']])
    
    # First and last rows
    print("\n8. First 2 rows:")
    print(df.head(2))
    print("\n9. Last 2 rows:")
    print(df.tail(2))


if __name__ == "__main__":
    main()
