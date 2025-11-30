"""
Pandas Lesson 19: Working with JSON Files
Learn how to read from and write to JSON files in different formats
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 19: Working with JSON Files"""
    print("\n" + "="*60)
    print("LESSON 19: JSON OPERATIONS")
    print("="*60)
    
    # Create sample data
    df = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'scores': [[85, 90, 88], [92, 87, 91], [88, 85, 89]]
    })
    
    print("\n1. Sample DataFrame:")
    print(df)
    
    # Save to JSON
    print("\n2. Saving to JSON (records format)...")
    df.to_json('data_records.json', orient='records', indent=2)
    print("✓ Saved as records format!")
    
    print("\n3. Saving to JSON (columns format)...")
    df.to_json('data_columns.json', orient='columns', indent=2)
    print("✓ Saved as columns format!")
    
    # Read from JSON
    print("\n4. Reading from JSON:")
    df_read = pd.read_json('data_records.json')
    print(df_read)


if __name__ == "__main__":
    main()
