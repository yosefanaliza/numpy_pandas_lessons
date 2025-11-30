"""
Pandas Lesson 4: Advanced Indexing and Selection
Learn advanced techniques for selecting and indexing data using loc, iloc, and boolean indexing
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 4: Advanced Indexing and Selection"""
    print("\n" + "="*60)
    print("LESSON 4: ADVANCED INDEXING AND SELECTION")
    print("="*60)
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
        'Salary': [70000, 60000, 75000, 90000, 65000]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # loc: label-based indexing
    print("\n2. Using loc (select row 1 and 3):")
    print(df.loc[[1, 3]])
    
    print("\n3. Using loc with column selection:")
    print(df.loc[1:3, ['Name', 'Salary']])
    
    # iloc: integer-based indexing
    print("\n4. Using iloc (select first 3 rows):")
    print(df.iloc[0:3])
    
    print("\n5. Using iloc with specific rows and columns:")
    print(df.iloc[[0, 2, 4], [0, 3]])
    
    # Boolean indexing
    print("\n6. Boolean indexing (Age > 28):")
    print(df[df['Age'] > 28])
    
    print("\n7. Boolean indexing with multiple conditions:")
    print(df[(df['Age'] > 28) & (df['Salary'] > 65000)])
    
    # Setting values using loc
    print("\n8. Setting values using loc:")
    df.loc[df['Department'] == 'IT', 'Salary'] = df.loc[df['Department'] == 'IT', 'Salary'] * 1.1
    print(df)


if __name__ == "__main__":
    main()
