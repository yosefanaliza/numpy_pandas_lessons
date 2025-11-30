"""
Run all Pandas lessons sequentially
This script executes all 20 Pandas lessons in order.
"""
# type: ignore

import sys
from pathlib import Path

# Add parent directory to path to import lessons
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Import all lessons
from lesson01_series import main as lesson01
from lesson02_dataframes import main as lesson02
from lesson03_adding_modifying import main as lesson03
from lesson04_indexing import main as lesson04
from lesson05_basic_operations import main as lesson05
from lesson06_csv_files import main as lesson06
from lesson07_filtering_sorting import main as lesson07
from lesson08_groupby import main as lesson08
from lesson09_pivot_tables import main as lesson09
from lesson10_merging_joining import main as lesson10
from lesson11_reshaping import main as lesson11
from lesson12_missing_data import main as lesson12
from lesson13_duplicates import main as lesson13
from lesson14_data_types import main as lesson14
from lesson15_string_operations import main as lesson15
from lesson16_data_transformation import main as lesson16
from lesson17_csv_operations import main as lesson17
from lesson18_excel_operations import main as lesson18
from lesson19_json_operations import main as lesson19
from lesson20_datetime import main as lesson20


def run_all_lessons():
    """Execute all Pandas lessons in sequence"""
    lessons = [
        ("Lesson 1: Working with Series", lesson01),
        ("Lesson 2: Working with DataFrames", lesson02),
        ("Lesson 3: Adding and Modifying Data", lesson03),
        ("Lesson 4: Advanced Indexing and Selection", lesson04),
        ("Lesson 5: Basic DataFrame Operations", lesson05),
        ("Lesson 6: Creating DataFrames from CSV Files", lesson06),
        ("Lesson 7: Filtering and Sorting Data", lesson07),
        ("Lesson 8: GroupBy and Aggregation", lesson08),
        ("Lesson 9: Pivot Tables and Cross-tabulation", lesson09),
        ("Lesson 10: Merging and Joining DataFrames", lesson10),
        ("Lesson 11: Reshaping Data - Melt and Stack", lesson11),
        ("Lesson 12: Handling Missing Data", lesson12),
        ("Lesson 13: Handling Duplicates", lesson13),
        ("Lesson 14: Data Type Conversion", lesson14),
        ("Lesson 15: String Operations", lesson15),
        ("Lesson 16: Data Transformation", lesson16),
        ("Lesson 17: Working with CSV Files", lesson17),
        ("Lesson 18: Working with Excel Files", lesson18),
        ("Lesson 19: Working with JSON Files", lesson19),
        ("Lesson 20: Date & Time Manipulation", lesson20),
    ]
    
    print("\n" + "="*80)
    print("PANDAS LEARNING PROJECT - ALL LESSONS")
    print("="*80)
    print(f"\nRunning {len(lessons)} lessons...\n")
    
    for i, (title, lesson_func) in enumerate(lessons, 1):
        try:
            print(f"\n{'='*80}")
            print(f"Running {title}...")
            print(f"{'='*80}")
            lesson_func()
            print(f"\n✓ {title} completed successfully!")
        except Exception as e:
            print(f"\n✗ Error in {title}: {str(e)}")
            print(f"Continuing with remaining lessons...\n")
    
    print("\n" + "="*80)
    print("ALL PANDAS LESSONS COMPLETED!")
    print("="*80)


if __name__ == "__main__":
    run_all_lessons()
