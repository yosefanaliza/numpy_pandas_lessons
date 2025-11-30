"""
Pandas Lesson 9: Pivot Tables and Cross-tabulation
Learn how to create pivot tables for data summarization
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 9: Pivot Tables and Cross-tabulation"""
    print("\n" + "="*60)
    print("LESSON 9: PIVOT TABLES")
    print("="*60)
    
    # Create sample data
    df = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=12, freq='M'),
        'Quarter': ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3', 'Q4', 'Q4', 'Q4'],
        'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
        'Sales': [100, 150, 120, 160, 130, 170, 140, 180, 150, 190, 160, 200],
        'Quantity': [10, 15, 12, 16, 13, 17, 14, 18, 15, 19, 16, 20]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Create pivot table
    print("\n2. Pivot table: Sales by Quarter and Product:")
    pivot1 = df.pivot_table(values='Sales', index='Quarter', columns='Product', aggfunc='sum')
    print(pivot1)
    
    print("\n3. Pivot table with multiple aggregations:")
    pivot2 = df.pivot_table(values='Sales', index='Quarter', columns='Product', 
                            aggfunc=['sum', 'mean'])  # type: ignore
    print(pivot2)
    
    print("\n4. Pivot table with margins (totals):")
    pivot3 = df.pivot_table(values='Sales', index='Quarter', columns='Product', 
                            aggfunc='sum', margins=True)
    print(pivot3)
    
    # Cross-tabulation
    print("\n5. Cross-tabulation of Quarter and Product:")
    crosstab = pd.crosstab(df['Quarter'], df['Product'], values=df['Sales'], aggfunc='sum')
    print(crosstab)


if __name__ == "__main__":
    main()
