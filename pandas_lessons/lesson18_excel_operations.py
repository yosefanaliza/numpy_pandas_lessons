"""
Pandas Lesson 18: Working with Excel Files
Learn how to read from and write to Excel files with multiple sheets
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 18: Working with Excel Files"""
    print("\n" + "="*60)
    print("LESSON 18: EXCEL OPERATIONS")
    print("="*60)
    
    # Create multiple DataFrames for different sheets
    sales_q1 = pd.DataFrame({
        'Product': ['Laptop', 'Phone', 'Tablet'],
        'Q1_Sales': [120000, 95000, 45000]
    })
    
    sales_q2 = pd.DataFrame({
        'Product': ['Laptop', 'Phone', 'Tablet'],
        'Q2_Sales': [130000, 98000, 52000]
    })
    
    print("\n1. Q1 Sales Data:")
    print(sales_q1)
    print("\n2. Q2 Sales Data:")
    print(sales_q2)
    
    # Write to Excel (multiple sheets)
    print("\n3. Writing to Excel file with multiple sheets...")
    try:
        with pd.ExcelWriter('sales_data.xlsx', engine='openpyxl') as writer:
            sales_q1.to_excel(writer, sheet_name='Q1', index=False)
            sales_q2.to_excel(writer, sheet_name='Q2', index=False)
        print("✓ Excel file created with Q1 and Q2 sheets!")
        
        # Read from Excel
        print("\n4. Reading from Excel (Q1 sheet):")
        df_q1 = pd.read_excel('sales_data.xlsx', sheet_name='Q1')
        print(df_q1)
        
        # Read all sheets
        print("\n5. Reading all sheets:")
        all_sheets = pd.read_excel('sales_data.xlsx', sheet_name=None)
        for sheet_name, df in all_sheets.items():
            print(f"\n{sheet_name} sheet:")
            print(df)
    except ImportError:
        print("\n⚠ Excel operations require openpyxl. Install with: pip install openpyxl")


if __name__ == "__main__":
    main()
