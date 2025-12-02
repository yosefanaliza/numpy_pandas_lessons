import pandas as pd
import numpy as np


"""
Types:
- pd.Timestamp: single timestamp
- pd.DatetimeIndex: index of timestamps
- pd.Series with dtype datetime64[ns]: series of timestamps
- pd.DataFrame with datetime columns
"""


# Create sample data ==================================================

# NOTE: pd.date_range creates a range of dates as a DatetimeIndex
date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
df = pd.DataFrame({
    'date': date_range,
    'sales': np.random.randint(100, 1000, len(date_range)),
    'temperature': np.random.randint(15, 35, len(date_range)),
    'customers': np.random.randint(10, 100, len(date_range))
})


# Creating datetime from string ==========================================
date_string = '2024-12-01'
date = pd.to_datetime(date_string)
print(f"Date: {date}")
print(f"Type: {type(date)}")

# Creating datetime from multiple strings ================================
dates = pd.to_datetime(['2024-01-01', '2024-06-15', '2024-12-31'])
print(dates)


# Accessing datetime components ==========================================
raw_dates = pd.date_range('20230101', periods=7)
print(f"First date year: {raw_dates[0].year}")
print(f"All dates:\n{raw_dates}")

dates_series = pd.Series(raw_dates)
# NOTE: Accessed via .dt accessor
print(f"Day names:\n{dates_series.dt.day_name()}")

# Parsing dates from csv ======================================
df_loaded = pd.read_csv(
    "sales_data.csv",
    parse_dates=["date"],
    date_format="%m/%d/%Y"
)
# NOTE: df_loaded['date'] is a pd.Series of timestamps
print(f"get list of years:\n{df_loaded['date'].dt.year}")
print(f"get specific index year {df_loaded['date'][0].year}")

