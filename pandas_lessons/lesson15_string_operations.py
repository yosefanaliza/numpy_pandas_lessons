"""
Pandas Lesson 15: String Operations
Learn how to manipulate and transform text data using string methods
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 15: String Operations"""
    print("\n" + "="*60)
    print("LESSON 15: STRING OPERATIONS")
    print("="*60)
    
    # Create DataFrame with text data
    df = pd.DataFrame({
        'Name': ['  alice  ', 'BOB', 'charlie', 'DAVID'],
        'Email': ['alice@email.com', 'bob@EMAIL.COM', 'charlie@email.com', 'david@EMAIL.COM'],
        'Phone': ['123-456-7890', '234-567-8901', '345-678-9012', '456-789-0123']
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # String methods
    print("\n2. Convert to lowercase:")
    print(df['Name'].str.lower())
    
    print("\n3. Convert to uppercase:")
    print(df['Name'].str.upper())
    
    print("\n4. Strip whitespace:")
    print(df['Name'].str.strip())
    
    print("\n5. Title case:")
    print(df['Name'].str.strip().str.title())
    
    print("\n6. Check if string contains pattern:")
    print(df['Email'].str.contains('alice'))
    
    print("\n7. Replace substring:")
    print(df['Email'].str.replace('@EMAIL.COM', '@email.com'))
    
    print("\n8. Split string:")
    print(df['Phone'].str.split('-'))
    
    print("\n9. Extract parts using split:")
    print(df['Phone'].str.split('-').str[0])  # Area code
    
    print("\n10. String length:")
    print(df['Name'].str.len())


if __name__ == "__main__":
    main()
