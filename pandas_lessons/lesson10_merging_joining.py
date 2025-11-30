"""
Pandas Lesson 10: Merging and Joining DataFrames
Learn how to combine multiple DataFrames using merge, join, and concat
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 10: Merging and Joining DataFrames"""
    print("\n" + "="*60)
    print("LESSON 10: MERGING AND JOINING")
    print("="*60)
    
    # Create sample DataFrames
    employees = pd.DataFrame({
        'EmployeeID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'DepartmentID': [101, 102, 101, 103, 102]
    })
    
    departments = pd.DataFrame({
        'DepartmentID': [101, 102, 103, 104],
        'DepartmentName': ['IT', 'HR', 'Finance', 'Marketing'],
        'Location': ['New York', 'London', 'Tokyo', 'Paris']
    })
    
    print("\n1. Employees DataFrame:")
    print(employees)
    
    print("\n2. Departments DataFrame:")
    print(departments)
    
    # Inner join
    print("\n3. Inner join (only matching records):")
    inner = pd.merge(employees, departments, on='DepartmentID', how='inner')
    print(inner)
    
    # Left join
    print("\n4. Left join (all employees):")
    left = pd.merge(employees, departments, on='DepartmentID', how='left')
    print(left)
    
    # Right join
    print("\n5. Right join (all departments):")
    right = pd.merge(employees, departments, on='DepartmentID', how='right')
    print(right)
    
    # Outer join
    print("\n6. Outer join (all records):")
    outer = pd.merge(employees, departments, on='DepartmentID', how='outer')
    print(outer)
    
    # Concatenating DataFrames
    print("\n7. Concatenating DataFrames vertically:")
    df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
    concatenated = pd.concat([df1, df2], ignore_index=True)
    print(concatenated)


if __name__ == "__main__":
    main()
