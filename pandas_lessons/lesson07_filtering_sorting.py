"""
Pandas Lesson 7: Filtering and Sorting Data
Learn advanced filtering techniques and sorting operations
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 7: Filtering and Sorting Data"""
    print("\n" + "="*60)
    print("LESSON 7: FILTERING AND SORTING DATA")
    print("="*60)
    
    # Create sample dataset
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
        'Age': [25, 30, 35, 28, 32, 27, 29, 31],
        'Salary': [70000, 60000, 75000, 90000, 65000, 72000, 88000, 62000],
        'Rating': [4.5, 3.8, 4.2, 4.7, 4.0, 4.3, 4.6, 3.9]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Sorting
    print("\n2. Sort by Age (ascending):")
    print(df.sort_values('Age'))
    
    print("\n3. Sort by Salary (descending):")
    print(df.sort_values('Salary', ascending=False))
    
    print("\n4. Sort by multiple columns (Department, then Salary):")
    print(df.sort_values(['Department', 'Salary'], ascending=[True, False]))
    
    # Filtering with multiple conditions
    print("\n5. Filter: IT department AND salary > 70000:")
    print(df[(df['Department'] == 'IT') & (df['Salary'] > 70000)])
    
    print("\n6. Filter: Age < 30 OR Rating >= 4.5:")
    print(df[(df['Age'] < 30) | (df['Rating'] >= 4.5)])
    
    # Using isin()
    print("\n7. Filter employees in IT or Finance:")
    print(df[df['Department'].isin(['IT', 'Finance'])])
    
    # String filtering
    print("\n8. Filter names starting with 'A' or 'C':")
    print(df[df['Name'].str.startswith(('A', 'C'))])


if __name__ == "__main__":
    main()
