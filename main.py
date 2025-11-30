"""
Pandas Learning Project - Main Module
This file covers the basics of pandas: Series, DataFrames, and fundamental operations
"""
# type: ignore

import pandas as pd
import numpy as np

def lesson1_series():
    """Lesson 1: Working with Pandas Series"""
    print("\n" + "="*60)
    print("LESSON 1: PANDAS SERIES")
    print("="*60)
    
    # Creating a Series from a list
    print("\n1. Creating a Series from a list:")
    s1 = pd.Series([10, 20, 30, 40, 50])
    print(s1)
    
    # Creating a Series with custom index
    print("\n2. Creating a Series with custom index:")
    s2 = pd.Series([10, 20, 30, 40, 50], ['a', 'b', 'c', 'd', 'e'])
    print(s2)
    
    # Creating a Series from a dictionary
    print("\n3. Creating a Series from a dictionary:")
    data = {'apple': 5, 'banana': 3, 'orange': 8, 'grape': 12}
    s3 = pd.Series(data)
    print(s3)
    
    # Basic Series operations
    print("\n4. Basic Series operations:")
    print(f"Mean: {s3.mean()}")
    print(f"STD: {s3.std()}")
    print(f"Sum: {s3.sum()}")
    print(f"Max: {s3.max()}")
    print(f"Min: {s3.min()}")
    print(f"Count: {s3.count()}")

    
    # Accessing elements
    print("\n5. Accessing elements:")
    print(f"First element: {s3.iloc[0]}")
    print(f"Element at 'banana': {s3['banana']}")
    print(f"Get from index 'banana': {s3.loc['banana']}")
    print(f"First 3 elements:\n{s3.head(3)}")


def lesson2_dataframes():
    """Lesson 2: Working with DataFrames"""
    print("\n" + "="*60)
    print("LESSON 2: PANDAS DATAFRAMES")
    print("="*60)
    
    # Creating a DataFrame from a dictionary
    print("\n1. Creating a DataFrame from a dictionary:")
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney'],
        'Salary': [70000, 80000, 75000, 90000, 85000]
    }
    df = pd.DataFrame(data)

    # df = pd.read_csv('dummy_data.csv')
    print(df)
    
    # DataFrame info
    print("\n2. DataFrame information:")
    print(df.info())
    
    print("\n3. DataFrame statistics:")
    print(df.describe())
    
    # Selecting columns
    print("\n4. Selecting a single column:")
    print(df['Name'])
    
    print("\n5. Selecting multiple columns:")
    print(df[['Name', 'Salary']])
    
    # Selecting rows
    print("\n6. Selecting rows by position (iloc):")
    print(df.iloc[0:3])
    
    print("\n7. Selecting rows by label (loc):")
    print(df.loc[df['Age'] > 30])
    
    return df


def lesson3_adding_modifying():
    """Lesson 3: Adding and Modifying Data"""
    print("\n" + "="*60)
    print("LESSON 3: ADDING AND MODIFYING DATA")
    print("="*60)
    
    # Create a sample DataFrame
    df = pd.DataFrame({
        'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
        'Price': [1200, 800, 400, 300],
        'Stock': [15, 30, 25, 20]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Adding a new column
    print("\n2. Adding a new column (Total Value):")
    df['Total_Value'] = df['Price'] * df['Stock']
    print(df)
    
    # Modifying existing values
    print("\n3. Applying a discount (10% off prices):")
    df['Price'] = df['Price'] * 0.9
    print(df)
    
    # Adding a new row
    print("\n4. Adding a new row:")
    new_row = pd.DataFrame({
        'Product': ['Keyboard'],
        'Price': [90],
        'Stock': [40],
        'Total_Value': [90 * 40]
    })
    df = pd.concat([df, new_row], ignore_index=True)
    print(df)
    
    # Dropping a column
    print("\n5. Dropping the Total_Value column:")
    df = df.drop('Total_Value', axis=1)
    print(df)
    
    return df


def lesson4_indexing():
    """Lesson 4: Advanced Indexing and Selection"""
    print("\n" + "="*60)
    print("LESSON 4: ADVANCED INDEXING AND SELECTION")
    print("="*60)
    
    # Create a sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT'],
        'Age': [25, 30, 35, 28, 32, 27],
        'Salary': [70000, 60000, 75000, 90000, 65000, 72000],
        'Experience': [2, 5, 8, 4, 6, 3]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Boolean indexing
    print("\n2. Filter employees in IT department:")
    print(df[df['Department'] == 'IT'])
    
    print("\n3. Filter employees with salary > 70000:")
    print(df[df['Salary'] > 70000])
    
    # Multiple conditions
    print("\n4. Filter IT employees with experience > 2:")
    print(df[(df['Department'] == 'IT') & (df['Experience'] > 2)])
    
    # Using query method
    print("\n5. Using query method (Age < 30 and Salary >= 70000):")
    print(df.query('Age < 30 and Salary >= 70000'))
    
    # Setting index
    print("\n6. Setting 'Name' as index:")
    df_indexed = df.set_index('Name')
    print(df_indexed)
    
    print("\n7. Accessing row by index:")
    print(df_indexed.loc['Alice'])


def lesson5_basic_operations():
    """Lesson 5: Basic DataFrame Operations"""
    print("\n" + "="*60)
    print("LESSON 5: BASIC DATAFRAME OPERATIONS")
    print("="*60)
    
    # Create sample data
    df = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Arithmetic operations
    print("\n2. Add 10 to column A:")
    print(df['A'] + 10)
    
    print("\n3. Multiply all values by 2:")
    print(df * 2)
    
    print("\n4. Column-wise operations:")
    print(df['A'] + df['B'])
    
    # Applying functions
    print("\n5. Applying square root to all values:")
    print(df.apply(np.sqrt))
    
    print("\n6. Applying custom function to each row:")
    df['Sum'] = df.apply(lambda row: row['A'] + row['B'] + row['C'], axis=1)
    print(df)
    
    # Aggregation
    print("\n7. Column-wise aggregation:")
    print(f"Column A mean: {df['A'].mean()}")
    print(f"Column B sum: {df['B'].sum()}")
    print(f"Column C max: {df['C'].max()}")


def lesson6_dataframe_from_csv():
    """Lesson 6: Creating DataFrames from CSV Files"""
    print("\n" + "="*60)
    print("LESSON 6: DATAFRAME FROM CSV FILES")
    print("="*60)
    
    # Create sample CSV data
    # data = {
    #     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    #     'Age': [25, 30, 35, 28, 32],
    #     'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney'],
    #     'Salary': [70000, 80000, 75000, 90000, 85000]
    # }
    # df = pd.DataFrame(data)
    # df.to_csv('dummy_data1.csv', index=False)
    # print("\n1. Sample CSV file 'dummy_data1.csv' created.")
    
    # Reading from CSV
    print("\n2. Reading from CSV file:")
    df = pd.read_csv('dummy_data.csv')
    print(df)
    
    # Displaying info and statistics
    print("\n3. DataFrame information:")
    print(df.info())
    
    print("\n4. DataFrame statistics:")
    print(df.describe())

if __name__ == "__main__":
    print("\n" + "="*60)
    print("WELCOME TO PANDAS LEARNING PROJECT")
    print("="*60)
    
    # Run all lessons
    lesson1_series()
    # lesson2_dataframes()
    # lesson3_adding_modifying()
    # lesson4_indexing()
    # lesson5_basic_operations()
    # lesson6_dataframe_from_csv()

    print("\n" + "="*60)
    print("ALL LESSONS COMPLETED!")
    print("="*60)
