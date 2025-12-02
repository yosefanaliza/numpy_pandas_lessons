"""
Pandas Lesson 20: Working with Date and Time
Learn how to work with dates and times in Pandas
"""
# type: ignore

import pandas as pd
import numpy as np
import time
import os


def main():
    """Lesson 20: Working with Date and Time"""
    print("\n" + "="*60)
    print("LESSON 20: WORKING WITH DATE AND TIME")
    print("="*60)
    
    # Create sample data
    np.random.seed(42)
    date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    df = pd.DataFrame({
        'date': date_range,
        'sales': np.random.randint(100, 1000, len(date_range)),
        'temperature': np.random.randint(15, 35, len(date_range)),
        'customers': np.random.randint(10, 100, len(date_range))
    })
    
    print("\n1. Creating datetime from string:")
    date_string = '2024-12-01'
    date = pd.to_datetime(date_string)
    print(f"Date: {date}")
    print(f"Type: {type(date)}")
    
    print("\n2. Creating datetime from multiple strings:")
    dates = pd.to_datetime(['2024-01-01', '2024-06-15', '2024-12-31'])
    print(dates)
    
    print("\n3. Creating datetime from components:")
    dates_from_dict = pd.to_datetime({
        'year': [2024, 2024, 2024],
        'month': [1, 6, 12],
        'day': [15, 20, 25]
    })
    print(dates_from_dict)
    
    print("\n4. Parsing different date formats:")
    formats = ['2024-12-01', '12/01/2024', 'December 1, 2024']
    for fmt in formats:
        parsed = pd.to_datetime(fmt)
        print(f"{fmt:<20} -> {parsed}")
    
    print("\n5. Sample DataFrame with dates:")
    print(df.head())
    print(f"Shape: {df.shape}")
    
    print("\n6. Loading dates from CSV - Method 1 (convert after load):")
    csv_file = 'temp_datetime_data.csv'
    df.to_csv(csv_file, index=False)
    df_loaded = pd.read_csv(csv_file)
    print(f"Before: {df_loaded['date'].dtype}")
    df_loaded['date'] = pd.to_datetime(df_loaded['date'])
    print(f"After: {df_loaded['date'].dtype}")
    
    print("\n7. Loading dates from CSV - Method 2 (parse during load):")
    df_loaded2 = pd.read_csv(csv_file, parse_dates=['date'])
    print(f"Date dtype: {df_loaded2['date'].dtype}")
    print(df_loaded2.head(3))
    
    print("\n8. Loading custom date format from CSV:")
    df_custom = df.copy()
    df_custom['date'] = df_custom['date'].dt.strftime('%d/%m/%Y')
    df_custom.to_csv('temp_custom_format.csv', index=False)
    df_custom_loaded = pd.read_csv('temp_custom_format.csv', 
                                    parse_dates=['date'],
                                    date_format='%d/%m/%Y')
    print(df_custom_loaded.head(3))
    
    print("\n9. Extracting date components (year, month, day):")
    df_sample = df.head(5).copy()
    df_sample['year'] = df_sample['date'].dt.year
    df_sample['month'] = df_sample['date'].dt.month
    df_sample['day'] = df_sample['date'].dt.day
    print(df_sample[['date', 'year', 'month', 'day']])
    
    print("\n10. Extracting additional date components:")
    df_sample['day_of_week'] = df_sample['date'].dt.dayofweek
    df_sample['day_name'] = df_sample['date'].dt.day_name()
    df_sample['month_name'] = df_sample['date'].dt.month_name()
    df_sample['quarter'] = df_sample['date'].dt.quarter
    df_sample['week_of_year'] = df_sample['date'].dt.isocalendar().week
    print(df_sample[['date', 'day_name', 'month_name', 'quarter']])
    
    print("\n11. Working with time components (hour, minute, second):")
    datetime_range = pd.date_range(start='2024-01-01 00:00:00', periods=12, freq='H')
    df_time = pd.DataFrame({
        'datetime': datetime_range,
        'value': np.random.randint(50, 150, 12)
    })
    df_time['hour'] = df_time['datetime'].dt.hour
    df_time['minute'] = df_time['datetime'].dt.minute
    df_time['time'] = df_time['datetime'].dt.time
    df_time['date_only'] = df_time['datetime'].dt.date
    print(df_time.head(8))


if __name__ == "__main__":
    main()
