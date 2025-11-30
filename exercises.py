"""
Pandas Learning Project - Practice Exercises
Complete these exercises to test your pandas skills!
"""

import pandas as pd
import numpy as np


def exercise1_basics():
    """
    Exercise 1: DataFrame Basics
    
    Tasks:
    1. Create a DataFrame with student data (Name, Math, Science, English scores)
    2. Add a new column 'Average' with the average of the three subjects
    3. Find the student with the highest average
    4. Filter students with Math score > 85
    """
    print("\n" + "="*60)
    print("EXERCISE 1: DataFrame Basics")
    print("="*60)
    
    # TODO: Write your solution here
    # Example structure:
    # data = {
    #     'Name': [...],
    #     'Math': [...],
    #     ...
    # }
    # df = pd.DataFrame(data)
    
    print("\nYOUR TURN: Complete this exercise!")


def exercise2_data_analysis():
    """
    Exercise 2: Data Analysis
    
    Use the sample_sales.csv file created earlier.
    Tasks:
    1. Load the CSV file
    2. Calculate total sales by Region
    3. Find the most popular product
    4. Calculate average order value by Product
    5. Identify the month with highest sales
    """
    print("\n" + "="*60)
    print("EXERCISE 2: Data Analysis")
    print("="*60)
    
    # TODO: Write your solution here
    # df = pd.read_csv('sample_sales.csv')
    
    print("\nYOUR TURN: Complete this exercise!")


def exercise3_data_cleaning():
    """
    Exercise 3: Data Cleaning
    
    Use the sample_employees_missing.csv file.
    Tasks:
    1. Load the CSV file
    2. Identify columns with missing values
    3. Fill missing Age values with the median age
    4. Fill missing Salary values with the mean salary by Department
    5. Remove any remaining rows with missing values
    """
    print("\n" + "="*60)
    print("EXERCISE 3: Data Cleaning")
    print("="*60)
    
    # TODO: Write your solution here
    
    print("\nYOUR TURN: Complete this exercise!")


def exercise4_groupby():
    """
    Exercise 4: GroupBy Operations
    
    Use the sample_customers.csv file.
    Tasks:
    1. Load the CSV file
    2. Group by City and calculate average Age
    3. Group by MembershipLevel and calculate total TotalPurchases
    4. Find the city with the youngest average customer age
    5. Create a pivot table showing average TotalPurchases by City and MembershipLevel
    """
    print("\n" + "="*60)
    print("EXERCISE 4: GroupBy Operations")
    print("="*60)
    
    # TODO: Write your solution here
    
    print("\nYOUR TURN: Complete this exercise!")


def exercise5_merging():
    """
    Exercise 5: Merging DataFrames
    
    Tasks:
    1. Create two DataFrames:
       - Orders: OrderID, CustomerID, Product, Amount
       - Customers: CustomerID, Name, City
    2. Merge them to get complete order information with customer details
    3. Find total purchase amount by City
    4. Identify customers who haven't made any orders (if applicable)
    """
    print("\n" + "="*60)
    print("EXERCISE 5: Merging DataFrames")
    print("="*60)
    
    # TODO: Write your solution here
    
    print("\nYOUR TURN: Complete this exercise!")


def exercise6_timeseries():
    """
    Exercise 6: Time Series Analysis
    
    Use the sample_timeseries.csv file.
    Tasks:
    1. Load the CSV and parse dates
    2. Set Date as the index
    3. Calculate 7-day rolling average of Temperature
    4. Find the month with highest average Sales
    5. Resample data to monthly frequency and calculate mean values
    """
    print("\n" + "="*60)
    print("EXERCISE 6: Time Series Analysis")
    print("="*60)
    
    # TODO: Write your solution here
    
    print("\nYOUR TURN: Complete this exercise!")


def exercise7_advanced():
    """
    Exercise 7: Advanced Challenge
    
    Combine multiple skills:
    1. Load sample_sales.csv
    2. Add a Month column from the Date
    3. Create a pivot table showing TotalAmount by Region and Product
    4. Calculate percentage of total sales for each Region
    5. Identify the top 3 selling products overall
    6. Create a summary report showing:
       - Total sales
       - Average order value
       - Number of orders per region
    """
    print("\n" + "="*60)
    print("EXERCISE 7: Advanced Challenge")
    print("="*60)
    
    # TODO: Write your solution here
    
    print("\nYOUR TURN: Complete this exercise!")


# SOLUTIONS (uncomment to see solutions)
def solutions():
    """
    Uncomment the solution functions below to see example solutions
    """
    pass

# def solution_exercise1():
#     data = {
#         'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Math': [85, 92, 88, 78],
#         'Science': [90, 87, 91, 85],
#         'English': [88, 85, 89, 90]
#     }
#     df = pd.DataFrame(data)
#     df['Average'] = df[['Math', 'Science', 'English']].mean(axis=1)
#     print(df)
#     print(f"\nStudent with highest average: {df.loc[df['Average'].idxmax(), 'Name']}")
#     print(f"\nStudents with Math > 85:\n{df[df['Math'] > 85]}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("PANDAS PRACTICE EXERCISES")
    print("="*60)
    print("\nComplete each exercise by editing this file.")
    print("Uncomment the solution functions at the bottom to check your work!")
    
    exercise1_basics()
    exercise2_data_analysis()
    exercise3_data_cleaning()
    exercise4_groupby()
    exercise5_merging()
    exercise6_timeseries()
    exercise7_advanced()
    
    print("\n" + "="*60)
    print("KEEP PRACTICING!")
    print("="*60)
