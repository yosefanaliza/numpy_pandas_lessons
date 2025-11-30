"""
Pandas Lesson 8: GroupBy and Aggregation
Learn how to group data and perform aggregation operations
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 8: GroupBy and Aggregation"""
    print("\n" + "="*60)
    print("LESSON 8: GROUPBY AND AGGREGATION")
    print("="*60)
    
    # Create sales dataset
    df = pd.DataFrame({
        'Region': ['North', 'South', 'North', 'East', 'South', 'West', 'North', 'East'],
        'Product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Phone', 'Tablet'],
        'Salesperson': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'David', 'Charlie', 'David'],
        'Sales': [120000, 95000, 45000, 110000, 98000, 52000, 89000, 47000],
        'Units': [100, 150, 90, 95, 160, 105, 145, 98]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Basic groupby
    print("\n2. Total sales by Region:")
    print(df.groupby('Region')['Sales'].sum())
    
    print("\n3. Average sales by Product:")
    print(df.groupby('Product')['Sales'].mean())
    
    # Multiple aggregations
    print("\n4. Multiple aggregations on Sales:")
    print(df.groupby('Region')['Sales'].agg(['sum', 'mean', 'count']))
    
    # Groupby with multiple columns
    print("\n5. Sales by Region and Product:")
    print(df.groupby(['Region', 'Product'])['Sales'].sum())
    
    # Custom aggregations
    print("\n6. Custom aggregations:")
    result = df.groupby('Region').agg({
        'Sales': ['sum', 'mean', 'max'],
        'Units': ['sum', 'mean']
    })
    print(result)
    
    # Using transform
    print("\n7. Add column with region total:")
    df['Region_Total'] = df.groupby('Region')['Sales'].transform('sum')
    print(df)


if __name__ == "__main__":
    main()
