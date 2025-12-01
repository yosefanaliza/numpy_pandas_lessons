"""
Pandas Lesson 20: Date & Time Manipulation
Learn how to work with dates, times, and time series data in pandas
"""
# type: ignore

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def main():
    """Lesson 20: Date & Time Manipulation"""
    print("\n" + "="*60)
    print("LESSON 20: DATE & TIME MANIPULATION")
    print("="*60)
    
    # 1. Creating datetime objects
    print("\n1. Creating Datetime Objects:")
    print("-" * 40)
    
    # From strings
    dates = pd.to_datetime(['2024-01-01', '2024-02-15', '2024-03-20'])
    print("From strings:")
    print(dates)
    
    # Custom date format
    custom_dates = pd.to_datetime(['01/15/2024', '02/20/2024'], format='%m/%d/%Y')
    print("\nCustom format (MM/DD/YYYY):")
    print(custom_dates)
    
    # From components
    df_dates = pd.DataFrame({
        'year': [2024, 2024, 2024],
        'month': [1, 2, 3],
        'day': [15, 20, 25]
    })
    dates_from_parts = pd.to_datetime(df_dates)
    print("\nFrom components:")
    print(dates_from_parts)
    
    # 2. Date ranges
    print("\n\n2. Creating Date Ranges:")
    print("-" * 40)
    
    # Daily frequency
    daily_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
    print("Daily range:")
    print(daily_range)
    
    # Monthly frequency
    monthly_range = pd.date_range(start='2024-01-01', periods=6, freq='M')
    print("\nMonthly range (6 months):")
    print(monthly_range)
    
    # Business days only
    business_days = pd.date_range(start='2024-01-01', periods=10, freq='B')
    print("\nBusiness days (10 days):")
    print(business_days)
    
    # Hourly frequency
    hourly_range = pd.date_range(start='2024-01-01', periods=24, freq='H')
    print("\nHourly range (24 hours):")
    print(hourly_range[:5], "...")
    
    # 3. Working with time series data
    print("\n\n3. Time Series DataFrame:")
    print("-" * 40)
    
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    df = pd.DataFrame({
        'date': dates,
        'sales': np.random.randint(100, 500, 100),
        'temperature': np.random.uniform(15, 35, 100)
    })
    
    # Set date as index
    df.set_index('date', inplace=True)
    print("Time series data (first 5 rows):")
    print(df.head())
    
    # 4. Reading CSV with Date Parsing
    print("\n\n4. Reading CSV and Parsing Dates:")
    print("-" * 40)
    
    # Create sample CSV data with various date formats
    sample_data = """date,product,sales,quantity
01/15/2024,Widget A,1500.50,25
02/20/2024,Widget B,2300.75,40
03/10/2024,Widget A,1800.25,30"""
    
    # Save to temporary CSV
    with open('temp_sales.csv', 'w') as f:
        f.write(sample_data)
    
    # Method 1: Parse dates while reading CSV
    print("\nMethod 1: Parse dates during CSV read:")
    df_sales = pd.read_csv('temp_sales.csv', parse_dates=['date'])
    print(df_sales)
    print(f"\nDate column type: {df_sales['date'].dtype}")
    
    # Method 2: Specify custom date format
    print("\n\nMethod 2: Custom date format (MM/DD/YYYY):")
    df_sales2 = pd.read_csv('temp_sales.csv', 
                            parse_dates=['date'],
                            date_format='%m/%d/%Y')
    print(df_sales2)
    
    # Method 3: Parse after reading
    print("\n\nMethod 3: Parse dates after reading:")
    df_sales3 = pd.read_csv('temp_sales.csv')
    df_sales3['date'] = pd.to_datetime(df_sales3['date'], format='%m/%d/%Y')
    print(df_sales3)
    
    # Method 4: Set date as index while reading
    print("\n\nMethod 4: Set date as index during read:")
    df_sales4 = pd.read_csv('temp_sales.csv', 
                            parse_dates=['date'],
                            index_col='date')
    print(df_sales4)
    
    # Clean up temporary file
    import os
    if os.path.exists('temp_sales.csv'):
        os.remove('temp_sales.csv')
    
    # 5. Common Date Format Examples
    print("\n\n5. Parsing Different Date Formats:")
    print("-" * 40)
    
    # Various date formats
    date_formats = {
        'MM/DD/YYYY': ['01/15/2024', '12/25/2024'],
        'DD-MM-YYYY': ['15-01-2024', '25-12-2024'],
        'YYYY/MM/DD': ['2024/01/15', '2024/12/25'],
        'YYYY-MM-DD': ['2024-01-15', '2024-12-25'],
        'DD MMM YYYY': ['15 Jan 2024', '25 Dec 2024'],
        'MMM DD, YYYY': ['Jan 15, 2024', 'Dec 25, 2024']
    }
    
    print("\nParsing different date formats:")
    for fmt, dates in date_formats.items():
        parsed = pd.to_datetime(dates[0])
        print(f"{fmt:15} -> {dates[0]:20} -> {parsed}")
    
    # 6. Handling Mixed or Problematic Dates
    print("\n\n6. Handling Problematic Dates:")
    print("-" * 40)
    
    # Mixed formats or invalid dates
    mixed_dates = pd.Series(['2024-01-15', '15/02/2024', 'invalid', '2024-03-20'])
    
    # With errors='coerce' - invalid dates become NaT (Not a Time)
    parsed_dates = pd.to_datetime(mixed_dates, errors='coerce', format='mixed')
    print("\nMixed/invalid dates (errors='coerce'):")
    print(parsed_dates)
    
    # 7. Extracting Date Components
    print("\n\n7. Extracting Date Components:")
    print("-" * 40)
    
    df_extract = pd.DataFrame({
        'date': pd.date_range('2024-01-01', periods=5, freq='D')
    })
    
    df_extract['year'] = df_extract['date'].dt.year
    df_extract['month'] = df_extract['date'].dt.month
    df_extract['day'] = df_extract['date'].dt.day
    df_extract['day_name'] = df_extract['date'].dt.day_name()
    df_extract['quarter'] = df_extract['date'].dt.quarter
    
    print("\nExtracted date components:")
    print(df_extract)
    
    # 8. Practical Example: Complete CSV Workflow
    print("\n\n8. Complete CSV Date Parsing Workflow:")
    print("-" * 40)
    
    # Create a more complex example
    complex_data = """transaction_date,customer_id,amount
2024-01-15,C001,150.50
2024-01-16,C002,230.75
2024-01-17,C001,180.25
2024-01-18,C003,210.00
2024-01-19,C002,195.50"""
    
    with open('temp_transactions.csv', 'w') as f:
        f.write(complex_data)
    
    # Read CSV with date parsing
    df_trans = pd.read_csv('temp_transactions.csv',
                          parse_dates=['transaction_date'],
                          index_col='transaction_date')
    
    print("\nTransaction data with parsed dates:")
    print(df_trans)
    
    # Add time-based features  # type: ignore
    df_trans['day_of_week'] = df_trans.index.day_name()  # type: ignore
    df_trans['month'] = df_trans.index.month  # type: ignore
    df_trans['is_weekend'] = df_trans.index.dayofweek >= 5  # type: ignore
    
    print("\nWith extracted date features:")
    print(df_trans)
    
    # Clean up
    if os.path.exists('temp_transactions.csv'):
        os.remove('temp_transactions.csv')
    
    print("\n" + "="*60)
    print("QUICK REFERENCE: Date Format Codes")
    print("="*60)
    print("%Y - 4-digit year (2024)")
    print("%y - 2-digit year (24)")
    print("%m - Month as number (01-12)")
    print("%d - Day of month (01-31)")
    print("%B - Full month name (January)")
    print("%b - Abbreviated month (Jan)")
    print("%A - Full weekday name (Monday)")
    print("%a - Abbreviated weekday (Mon)")
    print("%H - Hour 24-hour (00-23)")
    print("%I - Hour 12-hour (01-12)")
    print("%M - Minute (00-59)")
    print("%S - Second (00-59)")
    print("%p - AM/PM")
    print("="*60)


if __name__ == "__main__":
    main()
