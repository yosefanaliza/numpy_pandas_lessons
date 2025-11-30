"""
Pandas Lesson 11: Reshaping Data - Melt and Stack
Learn how to reshape data between wide and long formats
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 11: Reshaping Data - Melt and Stack"""
    print("\n" + "="*60)
    print("LESSON 11: RESHAPING DATA")
    print("="*60)
    
    # Create wide format data
    wide_df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Math': [85, 90, 88],
        'Science': [92, 87, 91],
        'English': [88, 85, 89]
    })
    
    print("\n1. Wide format DataFrame:")
    print(wide_df)
    
    # Melt (wide to long)
    print("\n2. Melt to long format:")
    long_df = pd.melt(wide_df, id_vars=['Name'], var_name='Subject', value_name='Score')
    print(long_df)
    
    # Pivot (long to wide)
    print("\n3. Pivot back to wide format:")
    wide_again = long_df.pivot(index='Name', columns='Subject', values='Score')
    print(wide_again)
    
    # Stack and unstack
    print("\n4. Using stack (wide to long):")
    stacked = wide_df.set_index('Name').stack()
    print(stacked)
    
    print("\n5. Using unstack (long to wide):")
    unstacked = stacked.unstack()
    print(unstacked)


if __name__ == "__main__":
    main()
