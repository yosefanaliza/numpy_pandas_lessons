# Pandas Lessons

A comprehensive collection of 20 Pandas lessons organized into separate, executable modules. Each lesson focuses on a specific aspect of the Pandas library, from basic Series and DataFrames to advanced data manipulation and file I/O operations.

## 📚 Lesson Overview

### Basics (Lessons 1-6)
1. **Working with Series** - Learn the basics of Pandas Series
2. **Working with DataFrames** - Create and work with DataFrames
3. **Adding and Modifying Data** - Add new columns, modify values, delete data
4. **Advanced Indexing and Selection** - Use loc, iloc, and boolean indexing
5. **Basic DataFrame Operations** - Sorting, filtering, statistical calculations
6. **Creating DataFrames from CSV Files** - Read and explore CSV data

### Data Manipulation (Lessons 7-11)
7. **Filtering and Sorting Data** - Advanced filtering and sorting techniques
8. **GroupBy and Aggregation** - Group data and perform aggregations
9. **Pivot Tables and Cross-tabulation** - Create pivot tables for summarization
10. **Merging and Joining DataFrames** - Combine multiple DataFrames
11. **Reshaping Data** - Melt, stack, pivot between wide and long formats

### Data Cleaning (Lessons 12-16)
12. **Handling Missing Data** - Detect, remove, and fill missing values
13. **Handling Duplicates** - Detect and remove duplicate rows
14. **Data Type Conversion** - Convert between numeric, datetime, and boolean types
15. **String Operations** - Manipulate and transform text data
16. **Data Transformation** - Apply functions, map values, bin and normalize data

### File I/O (Lessons 17-19)
17. **Working with CSV Files** - Read from and write to CSV files
18. **Working with Excel Files** - Work with Excel files and multiple sheets
19. **Working with JSON Files** - Read from and write to JSON files

### Advanced Topics (Lesson 20)
20. **Date & Time Manipulation** - Work with dates, times, and time series data

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas numpy openpyxl
```

### Running Individual Lessons

Each lesson is a standalone Python file that can be executed directly:

```bash
# Run from the pandas_lessons directory
python lesson01_series.py
python lesson02_dataframes.py
# ... and so on
```

Or from the parent directory:

```bash
python pandas_lessons/lesson01_series.py
```

### Running All Lessons

To run all lessons sequentially:

```bash
python pandas_lessons/run_all.py
```

Or from within the pandas_lessons directory:

```bash
python run_all.py
```

## 📁 Directory Structure

```
pandas_lessons/
├── __init__.py                      # Package initialization
├── README.md                        # This file
├── run_all.py                       # Script to run all lessons
├── lesson01_series.py               # Lesson 1: Working with Series
├── lesson02_dataframes.py           # Lesson 2: Working with DataFrames
├── lesson03_adding_modifying.py     # Lesson 3: Adding and Modifying Data
├── lesson04_indexing.py             # Lesson 4: Advanced Indexing
├── lesson05_basic_operations.py     # Lesson 5: Basic Operations
├── lesson06_csv_files.py            # Lesson 6: CSV Files
├── lesson07_filtering_sorting.py    # Lesson 7: Filtering and Sorting
├── lesson08_groupby.py              # Lesson 8: GroupBy
├── lesson09_pivot_tables.py         # Lesson 9: Pivot Tables
├── lesson10_merging_joining.py      # Lesson 10: Merging/Joining
├── lesson11_reshaping.py            # Lesson 11: Reshaping Data
├── lesson12_missing_data.py         # Lesson 12: Missing Data
├── lesson13_duplicates.py           # Lesson 13: Duplicates
├── lesson14_data_types.py           # Lesson 14: Data Types
├── lesson15_string_operations.py    # Lesson 15: String Operations
├── lesson16_data_transformation.py  # Lesson 16: Data Transformation
├── lesson17_csv_operations.py       # Lesson 17: CSV Operations
├── lesson18_excel_operations.py     # Lesson 18: Excel Operations
├── lesson19_json_operations.py      # Lesson 19: JSON Operations
└── lesson20_datetime.py             # Lesson 20: Date & Time Manipulation
```

## 💡 Features

- **Self-contained lessons**: Each lesson is independent and can be run separately
- **Comprehensive coverage**: From basics to advanced Pandas operations
- **Practical examples**: Real-world data scenarios and use cases
- **Clear output**: Each lesson prints detailed explanations and results
- **Type annotations**: Code includes type hints for better IDE support

## 📖 Learning Path

**Beginners** should start with lessons 1-6 to build a foundation.

**Intermediate users** can focus on lessons 7-11 for data manipulation techniques.

**Advanced topics** like data cleaning (12-16) and file I/O (17-19) build on earlier concepts.

## 🔧 Notes

- Lesson 18 (Excel Operations) requires the `openpyxl` package
- Some lessons create temporary files (CSV, Excel, JSON) for demonstration
- All lessons include `# type: ignore` to suppress type checking warnings
- Each lesson has a `main()` function for easy importing and testing

## 📝 Example Usage

```python
# Import and run a specific lesson
from pandas_lessons.lesson01_series import main as lesson01
lesson01()

# Or run directly
python pandas_lessons/lesson05_basic_operations.py
```

## 🎯 Learning Objectives

After completing all lessons, you will be able to:
- Create and manipulate Pandas Series and DataFrames
- Filter, sort, and aggregate data effectively
- Handle missing data and duplicates
- Transform and reshape data for analysis
- Merge and join multiple datasets
- Read and write data in various formats (CSV, Excel, JSON)
- Apply advanced string operations and data transformations

Happy learning! 🐼
