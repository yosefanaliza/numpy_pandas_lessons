"""
Pandas Lesson 3: Adding and Modifying Data
Learn how to add new columns, modify existing data, and delete data
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 3: Adding and Modifying Data"""
    print("\n" + "="*60)
    print("LESSON 3: ADDING AND MODIFYING DATA")
    print("="*60)
    
    # Create initial DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Salary': [70000, 80000, 75000]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Adding a new column
    print("\n2. Adding a new column (Department):")
    df['Department'] = ['IT', 'HR', 'Finance']
    print(df)
    
    # Adding column with calculation
    print("\n3. Adding calculated column (Annual Bonus = 10% of salary):")
    df['Bonus'] = df['Salary'] * 0.10
    print(df)
    

    # Modifying existing values in specific row
    print("\n4. Modifying values (increase Alice's age by 1):")
    df.loc[df['Name'] == 'Alice', 'Age'] += 1
    print(df)

    # Modifying existing values
    print("\n4. Modifying values (increase all salaries by 5%):")
    df['Salary'] = df['Salary'] * 1.05
    print(df)
    
    # Adding a new row using loc
    print("\n5. Adding a new row:")
    df.loc[3] = ['David', 28, 90000, 'Sales', 9000]
    print(df)
    
    # Deleting a column
    print("\n6. Deleting the Bonus column:")
    df = df.drop('Bonus', axis=1)
    print(df)
    
    # Deleting a row
    print("\n7. Deleting row at index 0:")
    df = df.drop(0)
    print(df)
    
    # Resetting index
    print("\n8. Resetting index:")
    df = df.reset_index(drop=True)
    print(df)


if __name__ == "__main__":
    main()
