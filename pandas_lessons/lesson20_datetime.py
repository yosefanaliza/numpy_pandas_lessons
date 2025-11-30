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
    
    # 4. Extracting date components
    print("\n\n4. Extracting Date Components:")
    print("-" * 40)
    
    # Access datetime properties from DatetimeIndex
    dt_index = pd.DatetimeIndex(df.index)
    df['year'] = dt_index.year
    df['month'] = dt_index.month
    df['day'] = dt_index.day
    df['day_of_week'] = dt_index.dayofweek  # Monday=0, Sunday=6
    df['day_name'] = dt_index.day_name()
    df['quarter'] = dt_index.quarter
    df['week_of_year'] = dt_index.isocalendar().week
    
    print("Date components (first 5 rows):")
    print(df[['sales', 'year', 'month', 'day', 'day_name', 'quarter']].head())
    
    # 5. Filtering by date
    print("\n\n5. Filtering by Date:")
    print("-" * 40)
    
    # Reset for clean example
    df = df[['sales', 'temperature']]
    
    # Select specific month
    january_data = df['2024-01']
    print(f"January data: {len(january_data)} rows")
    print(january_data.head())
    
    # Date range filtering
    feb_march = df['2024-02-01':'2024-03-15']
    print(f"\nFeb-March data: {len(feb_march)} rows")
    
    # Using boolean indexing
    q1_data = df[(df.index >= '2024-01-01') & (df.index < '2024-04-01')]
    print(f"\nQ1 2024 data: {len(q1_data)} rows")
    
    # 6. Resampling (aggregating by time period)
    print("\n\n6. Resampling Time Series:")
    print("-" * 40)
    
    # Weekly average
    weekly_avg = df.resample('W').mean()
    print("Weekly averages (first 5):")
    print(weekly_avg.head())
    
    # Monthly sum
    monthly_sum = df['sales'].resample('M').sum()
    print("\nMonthly sales totals:")
    print(monthly_sum)
    
    # Custom aggregation
    monthly_agg = df.resample('M').agg({
        'sales': ['sum', 'mean', 'max'],
        'temperature': ['mean', 'min', 'max']
    })
    print("\nMonthly aggregations:")
    print(monthly_agg)
    
    # 7. Rolling windows
    print("\n\n7. Rolling Window Calculations:")
    print("-" * 40)
    
    # 7-day moving average
    df['sales_7d_avg'] = df['sales'].rolling(window=7).mean()
    print("7-day moving average (first 10 rows):")
    print(df[['sales', 'sales_7d_avg']].head(10))
    
    # 30-day rolling sum
    df['sales_30d_sum'] = df['sales'].rolling(window=30).sum()
    print("\n30-day rolling sum:")
    print(df[['sales', 'sales_30d_sum']].tail())
    
    # 8. Date arithmetic
    print("\n\n8. Date Arithmetic:")
    print("-" * 40)
    
    # Create sample DataFrame
    orders = pd.DataFrame({
        'order_date': pd.to_datetime(['2024-01-10', '2024-01-15', '2024-01-20']),
        'delivery_days': [3, 5, 2]
    })
    
    # Add days to dates
    orders['delivery_date'] = orders['order_date'] + pd.to_timedelta(orders['delivery_days'], unit='D')
    print("Order and delivery dates:")
    print(orders)
    
    # Calculate time differences
    orders['processing_time'] = orders['delivery_date'] - orders['order_date']
    print("\nProcessing time:")
    print(orders[['order_date', 'delivery_date', 'processing_time']])
    
    # 9. Time zones
    print("\n\n9. Working with Time Zones:")
    print("-" * 40)
    
    # Create timezone-aware dates
    dates_utc = pd.date_range('2024-01-01', periods=5, freq='D', tz='UTC')
    print("UTC dates:")
    print(dates_utc)
    
    # Convert to different timezone
    dates_ny = dates_utc.tz_convert('America/New_York')
    print("\nNew York timezone:")
    print(dates_ny)
    
    dates_tokyo = dates_utc.tz_convert('Asia/Tokyo')
    print("\nTokyo timezone:")
    print(dates_tokyo)
    
    # 10. Period and frequency
    print("\n\n10. Periods and Frequencies:")
    print("-" * 40)
    
    # Create period range
    periods = pd.period_range('2024-01', periods=12, freq='M')
    print("Monthly periods (12 months):")
    print(periods)
    
    # Quarter periods
    quarters = pd.period_range('2024Q1', periods=4, freq='Q')
    print("\nQuarterly periods:")
    print(quarters)
    
    # 11. Shifting and lagging
    print("\n\n11. Shifting and Lagging:")
    print("-" * 40)
    
    # Create sample data
    dates = pd.date_range('2024-01-01', periods=10, freq='D')
    sales_df = pd.DataFrame({
        'date': dates,
        'sales': [100, 120, 115, 130, 125, 140, 135, 150, 145, 160]
    }).set_index('date')
    
    # Shift forward (lag)
    sales_df['sales_prev_day'] = sales_df['sales'].shift(1)
    
    # Shift backward (lead)
    sales_df['sales_next_day'] = sales_df['sales'].shift(-1)
    
    # Calculate change
    sales_df['daily_change'] = sales_df['sales'] - sales_df['sales_prev_day']
    
    print("Shifted data:")
    print(sales_df)
    
    # 12. Practical example: Sales analysis
    print("\n\n12. Practical Example: Sales Analysis:")
    print("-" * 40)
    
    # Create realistic sales data
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=90, freq='D')
    sales = pd.DataFrame({
        'date': dates,
        'sales': np.random.randint(80, 200, 90) + 
                 np.sin(np.arange(90) * 2 * np.pi / 7) * 20  # Weekly pattern
    }).set_index('date')
    
    # Add day of week
    dt_index = pd.DatetimeIndex(sales.index)
    sales['day_of_week'] = dt_index.day_name()
    
    # Calculate weekly statistics
    sales['week'] = dt_index.isocalendar().week
    weekly_stats = sales.groupby('week')['sales'].agg(['mean', 'sum', 'count'])
    
    print("Weekly sales statistics:")
    print(weekly_stats.head())
    
    # Average sales by day of week
    day_avg = sales.groupby('day_of_week')['sales'].mean().sort_values(ascending=False)
    print("\nAverage sales by day of week:")
    print(day_avg)
    
    # Calculate 7-day moving average
    sales['moving_avg_7d'] = sales['sales'].rolling(window=7).mean()
    print("\nRecent sales with 7-day moving average:")
    print(sales[['sales', 'moving_avg_7d', 'day_of_week']].tail(10))
    
    print("\n" + "="*60)
    print("Date & Time Manipulation lesson complete!")
    print("="*60)


if __name__ == "__main__":
    main()
