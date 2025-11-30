"""
Pandas Lesson 13: Handling Duplicates
Learn how to detect and remove duplicate rows
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 13: Handling Duplicates"""
    print("\n" + "="*60)
    print("LESSON 13: HANDLING DUPLICATES")
    print("="*60)
    
    # Create DataFrame with duplicates
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David'],
        'Age': [25, 30, 25, 35, 30, 28],
        'City': ['New York', 'Paris', 'New York', 'London', 'Paris', 'Tokyo']
    })
    
    print("\n1. DataFrame with duplicates:")
    print(df)
    
    # Detecting duplicates
    print("\n2. Check for duplicate rows:")
    print(df.duplicated())
    
    print("\n3. Show duplicate rows:")
    print(df[df.duplicated()])
    
    print("\n4. Check duplicates based on specific column:")
    print(df.duplicated(subset=['Name']))
    
    # Removing duplicates
    print("\n5. Remove duplicate rows (keep first):")
    print(df.drop_duplicates())
    
    print("\n6. Remove duplicates (keep last):")
    print(df.drop_duplicates(keep='last'))
    
    print("\n7. Remove duplicates based on Name column:")
    print(df.drop_duplicates(subset=['Name']))
    
    print("\n8. Count of each unique value:")
    print(df['Name'].value_counts())


if __name__ == "__main__":
    main()
