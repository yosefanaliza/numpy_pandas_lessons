"""
Pandas Lesson 14: Data Type Conversion
Learn how to convert between different data types (numeric, datetime, boolean)
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 14: Data Type Conversion"""
    print("\n" + "="*60)
    print("LESSON 14: DATA TYPE CONVERSION")
    print("="*60)
    
    # Create DataFrame with various types
    df = pd.DataFrame({
        'ID': ['1', '2', '3', '4', '5'],
        'Value': ['100', '200', '300', '400', '500'],
        'Date': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01'],
        'Flag': ['True', 'False', 'True', 'True', 'False']
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    print("\n2. Original data types:")
    print(df.dtypes)
    
    # Convert to numeric
    print("\n3. Convert ID to integer:")
    df['ID'] = pd.to_numeric(df['ID'])
    print(df.dtypes)
    
    print("\n4. Convert Value to float:")
    df['Value'] = df['Value'].astype(float)
    print(df.dtypes)
    
    # Convert to datetime
    print("\n5. Convert Date to datetime:")
    df['Date'] = pd.to_datetime(df['Date'])
    print(df.dtypes)
    
    # Convert to boolean
    print("\n6. Convert Flag to boolean:")
    df['Flag'] = df['Flag'].map({'True': True, 'False': False})
    print(df)
    print(df.dtypes)
    
    # Handle conversion errors
    print("\n7. Handling conversion errors:")
    bad_data = pd.Series(['1', '2', 'three', '4'])
    print(f"Original: {bad_data.values}")
    converted_series = pd.to_numeric(bad_data, errors='coerce')
    print(f"Converted (coerce): {converted_series.values}")


if __name__ == "__main__":
    main()
