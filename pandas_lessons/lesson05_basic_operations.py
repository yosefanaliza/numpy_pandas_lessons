"""
Pandas Lesson 5: Basic DataFrame Operations
Learn essential operations like sorting, filtering, and statistical calculations
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 5: Basic DataFrame Operations"""
    print("\n" + "="*60)
    print("LESSON 5: BASIC DATAFRAME OPERATIONS")
    print("="*60)
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
        'Price': [1200, 800, 500, 300, 100],
        'Quantity': [5, 10, 15, 8, 20],
        'Category': ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Accessories']
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Sorting
    print("\n2. Sort by Price (ascending):")
    print(df.sort_values('Price'))
    
    print("\n3. Sort by Price (descending):")
    print(df.sort_values('Price', ascending=False))
    
    # Calculations
    print("\n4. Add Total Value column:")
    df['Total_Value'] = df['Price'] * df['Quantity']
    print(df)
    
    # Statistical operations
    print("\n5. Statistical summary:")
    print(f"Average Price: ${df['Price'].mean():.2f}")
    print(f"Total Quantity: {df['Quantity'].sum()}")
    print(f"Max Price: ${df['Price'].max():.2f}")
    print(f"Min Price: ${df['Price'].min():.2f}")
    
    # Unique values
    print("\n6. Unique categories:")
    print(df['Category'].unique())
    
    # Value counts
    print("\n7. Count by category:")
    print(df['Category'].value_counts())


if __name__ == "__main__":
    main()
