"""
Pandas Lesson 12: Handling Missing Data
Learn techniques for detecting, removing, and filling missing values
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 12: Handling Missing Data"""
    print("\n" + "="*60)
    print("LESSON 12: HANDLING MISSING DATA")
    print("="*60)
    
    # Create DataFrame with missing values
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, np.nan, 35, 28, np.nan],
        'City': ['New York', 'Paris', None, 'Tokyo', 'Sydney'],
        'Salary': [70000, 80000, np.nan, 90000, 85000]
    })
    
    print("\n1. DataFrame with missing values:")
    print(df)
    
    # Detecting missing values
    print("\n2. Check for missing values:")
    print(df.isnull())
    
    print("\n3. Count missing values per column:")
    print(df.isnull().sum())
    
    print("\n4. Check if any value is missing:")
    print(df.isnull().any())
    
    # Dropping missing values
    print("\n5. Drop rows with any missing value:")
    print(df.dropna())
    
    print("\n6. Drop rows where all values are missing:")
    df_test = df.copy()
    df_test.loc[5] = [None, None, None, None]
    print(df_test.dropna(how='all'))
    
    print("\n7. Drop columns with missing values:")
    print(df.dropna(axis=1))
    
    # Filling missing values
    print("\n8. Fill missing values with 0:")
    print(df.fillna(0))
    
    print("\n9. Fill with column mean:")
    df_filled = df.copy()
    df_filled['Age'] = df_filled['Age'].fillna(df_filled['Age'].mean())
    print(df_filled)
    
    print("\n10. Forward fill (use previous value):")
    print(df.ffill())
    
    print("\n11. Backward fill (use next value):")
    print(df.bfill())
    
    # Interpolation
    print("\n12. Interpolate missing values:")
    series = pd.Series([1, np.nan, np.nan, 4, 5])
    print(f"Original: {series.values}")
    print(f"Interpolated: {series.interpolate().values}")


if __name__ == "__main__":
    main()
