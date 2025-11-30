# Pandas Learning Project

A comprehensive, hands-on project to learn pandas from basics to advanced concepts.

## 📚 Project Structure

```
pandas/
├── main.py                    # Lessons 1-5: Pandas Basics
├── data_manipulation.py       # Lessons 6-10: Data Manipulation
├── data_cleaning.py          # Lessons 11-15: Data Cleaning
├── file_operations.py        # Lessons 16-18: File I/O
├── exercises.py              # Practice Exercises
└── README.md                 # This file
```

## 🎯 Learning Path

### Phase 1: Pandas Basics (main.py)
**Lessons 1-5** - Start here if you're new to pandas

- **Lesson 1**: Pandas Series - Creating and working with one-dimensional data
- **Lesson 2**: DataFrames - Understanding two-dimensional data structures
- **Lesson 3**: Adding & Modifying Data - Creating columns, rows, and updating values
- **Lesson 4**: Advanced Indexing - Boolean indexing, filtering, and selection
- **Lesson 5**: Basic Operations - Arithmetic, aggregation, and applying functions

Run: `python main.py`

### Phase 2: Data Manipulation (data_manipulation.py)
**Lessons 6-10** - Essential data analysis skills

- **Lesson 6**: Filtering & Sorting - Complex filtering and multi-level sorting
- **Lesson 7**: GroupBy & Aggregation - Grouping data and calculating statistics
- **Lesson 8**: Pivot Tables - Creating pivot tables for data summarization
- **Lesson 9**: Merging & Joining - Combining multiple DataFrames
- **Lesson 10**: Reshaping Data - Converting between wide and long formats

Run: `python data_manipulation.py`

### Phase 3: Data Cleaning (data_cleaning.py)
**Lessons 11-15** - Prepare data for analysis

- **Lesson 11**: Missing Data - Detecting, dropping, and filling missing values
- **Lesson 12**: Duplicates - Finding and removing duplicate records
- **Lesson 13**: Data Types - Converting between different data types
- **Lesson 14**: String Operations - Text manipulation and cleaning
- **Lesson 15**: Data Transformation - Applying functions, binning, and normalization

Run: `python data_cleaning.py`

### Phase 4: File Operations (file_operations.py)
**Lessons 16-18** - Reading and writing data

- **Lesson 16**: CSV Operations - Reading and writing CSV files
- **Lesson 17**: Excel Operations - Working with Excel files (requires openpyxl)
- **Lesson 18**: JSON Operations - Handling JSON data
- **Bonus**: Sample dataset creation for practice

Run: `python file_operations.py`

### Phase 5: Practice Exercises (exercises.py)
**7 Exercises** - Test your skills

Complete hands-on exercises covering all topics learned.

Edit: `exercises.py` (add your solutions, then run to check)

## 🚀 Getting Started

### Prerequisites

1. **Install Python** (3.8 or higher)
2. **Install required packages**:

```powershell
pip install pandas numpy openpyxl
```

### Quick Start

1. **Start with the basics**:
   ```powershell
   python main.py
   ```

2. **Progress through each module** in order:
   ```powershell
   python data_manipulation.py
   python data_cleaning.py
   python file_operations.py
   ```

3. **Practice with exercises**:
   - Open `exercises.py`
   - Complete each exercise
   - Run to test your solutions

## 📖 How to Use This Project

### For Beginners
1. Run each lesson file sequentially
2. Read the code comments carefully
3. Experiment by modifying the code
4. Try the exercises after completing all lessons

### For Practice
1. Use the sample datasets created by `file_operations.py`
2. Complete exercises in `exercises.py`
3. Try creating your own analysis scripts
4. Experiment with real-world datasets

### For Reference
- Each lesson is self-contained
- Use CTRL+F to search for specific topics
- Run individual lessons as needed

## 📊 Sample Datasets

Running `file_operations.py` creates these practice files:

- `sample_sales.csv` - 100 sales orders with products, regions, dates
- `sample_customers.csv` - 50 customer records
- `sample_employees_missing.csv` - 30 employee records (with missing data)
- `sample_timeseries.csv` - 365 days of time series data

## 🔑 Key Concepts Covered

### Data Structures
- Series (1D labeled arrays)
- DataFrames (2D labeled data structures)
- Index manipulation

### Data Selection
- Position-based (iloc)
- Label-based (loc)
- Boolean indexing
- Query method

### Data Operations
- Filtering and sorting
- GroupBy aggregation
- Pivot tables
- Merging and joining
- Reshaping (melt, stack, unstack)

### Data Cleaning
- Handling missing values (dropna, fillna)
- Removing duplicates
- Type conversions
- String operations
- Data transformation

### File I/O
- CSV files (read_csv, to_csv)
- Excel files (read_excel, to_excel)
- JSON files (read_json, to_json)

## 💡 Tips for Success

1. **Run the code** - Don't just read it, execute each lesson
2. **Experiment** - Modify parameters and see what happens
3. **Use print()** - Add print statements to understand the flow
4. **Read errors** - Error messages teach you what went wrong
5. **Practice regularly** - Use pandas daily for best retention
6. **Use real data** - Apply what you learn to actual datasets

## 📚 Next Steps

After completing this project:

1. **Learn data visualization** with matplotlib/seaborn
2. **Explore advanced pandas** (MultiIndex, time zones, categories)
3. **Work with large datasets** (chunking, optimization)
4. **Combine with other libraries** (NumPy, scikit-learn)
5. **Build real projects** with actual datasets

## 🔗 Additional Resources

- [Official Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

## ⚙️ Troubleshooting

### Import Errors
If you see "Import pandas could not be resolved":
```powershell
pip install pandas numpy
```

### Excel Errors
If Excel operations fail:
```powershell
pip install openpyxl
```

### File Not Found
Make sure you're in the correct directory:
```powershell
cd path\to\pandas
```

## 📝 Exercise Checklist

- [ ] Complete Exercise 1: DataFrame Basics
- [ ] Complete Exercise 2: Data Analysis
- [ ] Complete Exercise 3: Data Cleaning
- [ ] Complete Exercise 4: GroupBy Operations
- [ ] Complete Exercise 5: Merging DataFrames
- [ ] Complete Exercise 6: Time Series Analysis
- [ ] Complete Exercise 7: Advanced Challenge

---

**Happy Learning! 🐼**

Start with `python main.py` and work your way through each module. Remember: the best way to learn is by doing!
