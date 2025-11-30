# NumPy & Pandas Learning Repository

A comprehensive, hands-on learning resource for mastering NumPy and Pandas - the foundational libraries for data science and analysis in Python.

## 📚 Project Overview

This repository contains structured lessons covering everything from basic array operations to advanced data manipulation techniques. Each lesson is self-contained with clear examples, explanations, and practical exercises.

## 🗂️ Repository Structure

```
├── numpy_lessons/              # 20 comprehensive NumPy lessons
│   ├── lesson01_numpy_arrays.py
│   ├── lesson02_array_creation_functions.py
│   ├── ...
│   ├── lesson20_practical_examples.py
│   ├── numpy_fast.py          # Quick reference guide
│   ├── run_all.py             # Run all lessons sequentially
│   └── README.md              # NumPy-specific documentation
│
├── pandas_lessons/             # 19 comprehensive Pandas lessons
│   ├── lesson01_series.py
│   ├── lesson02_dataframes.py
│   ├── ...
│   ├── lesson19_json_operations.py
│   ├── run_all.py             # Run all lessons sequentially
│   └── README.md              # Pandas-specific documentation
│
├── main.py                     # Main entry point
├── exercises.py                # Practice exercises
├── dummy_data.csv             # Sample dataset
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🎯 Learning Paths

### Path 1: NumPy Fundamentals (20 Lessons)

Master the foundation of numerical computing in Python:

**Basics (Lessons 1-5)**
- Arrays and their creation
- Array attributes and properties
- Indexing and slicing
- Reshaping and manipulation

**Operations (Lessons 6-10)**
- Mathematical operations
- Statistical functions
- Linear algebra
- Random number generation

**Advanced (Lessons 11-20)**
- Broadcasting mechanics
- Advanced indexing techniques
- Sorting and searching
- Performance optimization
- Data types and memory management
- File I/O operations
- Structured and masked arrays
- Real-world applications

**Run all NumPy lessons:**
```powershell
cd numpy_lessons
python run_all.py
```

### Path 2: Pandas Data Analysis (19 Lessons)

Master data manipulation and analysis:

**Fundamentals (Lessons 1-5)**
- Series and DataFrames
- Adding and modifying data
- Indexing and selection
- Basic operations

**Data Manipulation (Lessons 6-11)**
- Reading CSV files
- Filtering and sorting
- GroupBy operations
- Pivot tables
- Merging and joining
- Reshaping data

**Data Cleaning (Lessons 12-16)**
- Handling missing data
- Removing duplicates
- Data type conversions
- String operations
- Data transformation

**File Operations (Lessons 17-19)**
- CSV operations
- Excel file handling
- JSON data processing

**Run all Pandas lessons:**
```powershell
cd pandas_lessons
python run_all.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository** (if using Git):
   ```powershell
   git clone <repository-url>
   cd numpy_pandas_lessons
   ```

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

   Or install manually:
   ```powershell
   pip install numpy pandas openpyxl
   ```

### Quick Start

**Option 1: Run individual lessons**
```powershell
# NumPy lesson
python numpy_lessons/lesson01_numpy_arrays.py

# Pandas lesson
python pandas_lessons/lesson01_series.py
```

**Option 2: Run all lessons in a category**
```powershell
# All NumPy lessons
python numpy_lessons/run_all.py

# All Pandas lessons
python pandas_lessons/run_all.py
```

**Option 3: Use the main entry point**
```powershell
python main.py
```

**Option 4: Practice with exercises**
```powershell
python exercises.py
```

## 📖 How to Learn Effectively

### For Complete Beginners
1. Start with NumPy Lesson 1
2. Work through NumPy lessons 1-10 sequentially
3. Move to Pandas Lesson 1
4. Complete all Pandas lessons in order
5. Practice with `exercises.py`

### For Those with Some Experience
1. Review the quick reference: `numpy_lessons/numpy_fast.py`
2. Jump to specific topics as needed
3. Use CTRL+F to search for specific concepts
4. Focus on advanced lessons (11+)

### Best Practices
- **Run every example**: Don't just read - execute the code
- **Experiment freely**: Modify parameters and observe results
- **Use print statements**: Add debugging to understand data flow
- **Read error messages**: They're teaching tools, not obstacles
- **Practice daily**: Consistency beats intensity

## 🔑 Key Topics Covered

### NumPy
✅ Array creation and manipulation  
✅ Mathematical and statistical operations  
✅ Linear algebra computations  
✅ Broadcasting and vectorization  
✅ Advanced indexing (boolean, fancy)  
✅ Memory optimization techniques  
✅ Random number generation  
✅ File I/O (npy, npz, csv, txt)  
✅ Structured and masked arrays  
✅ Performance best practices  

### Pandas
✅ Series and DataFrame structures  
✅ Data selection and indexing  
✅ Filtering, sorting, and querying  
✅ GroupBy aggregations  
✅ Pivot tables and cross-tabulations  
✅ Merging, joining, and concatenating  
✅ Reshaping (melt, pivot, stack)  
✅ Missing data handling  
✅ Duplicate detection and removal  
✅ Data type conversions  
✅ String manipulation  
✅ File operations (CSV, Excel, JSON)  

## 💡 Pro Tips

1. **Start with NumPy**: It's the foundation for Pandas
2. **Type along**: Don't copy-paste - type the code yourself
3. **Break things**: Try invalid inputs to understand boundaries
4. **Use documentation**: Get comfortable with official docs
5. **Work with real data**: Apply lessons to your own datasets
6. **Time your code**: Use performance lessons to optimize
7. **Join communities**: Stack Overflow, Reddit's r/learnpython

## 📊 Sample Data

The repository includes `dummy_data.csv` for practice. Each file operation lesson also demonstrates how to create sample datasets for experimentation.

## 🛠️ Troubleshooting

### Module Not Found
```powershell
pip install numpy pandas openpyxl
```

### Excel File Errors
```powershell
pip install openpyxl xlrd
```

### Permission Errors
Run your terminal as administrator or check file permissions.

### Path Issues
Ensure you're in the correct directory:
```powershell
Get-Location  # Check current directory
cd path\to\numpy_pandas_lessons
```

## 📚 What's Next?

After mastering this repository:

1. **Data Visualization**: Learn Matplotlib and Seaborn
2. **Machine Learning**: Explore scikit-learn
3. **Big Data**: Study Dask and Apache Spark
4. **Statistics**: Deep dive into SciPy
5. **Real Projects**: Kaggle competitions, personal datasets

## 🔗 Resources

- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/index.html)
- [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

## 🤝 Contributing

This is a learning resource. Feel free to:
- Add more examples
- Improve explanations
- Fix bugs or typos
- Suggest new lessons

## 📝 Progress Tracker

### NumPy Progress
- [ ] Lessons 1-5: Basics
- [ ] Lessons 6-10: Operations
- [ ] Lessons 11-15: Advanced Techniques
- [ ] Lessons 16-20: Professional Skills

### Pandas Progress
- [ ] Lessons 1-5: Fundamentals
- [ ] Lessons 6-11: Data Manipulation
- [ ] Lessons 12-16: Data Cleaning
- [ ] Lessons 17-19: File Operations

### Practice
- [ ] Complete all exercises in `exercises.py`
- [ ] Build a personal data analysis project
- [ ] Contribute to open-source data projects

---

**Happy Learning! 🚀**

*Start your journey with `python numpy_lessons/lesson01_numpy_arrays.py` and remember: mastery comes from consistent practice, not perfection.*
