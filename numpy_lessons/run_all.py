"""
Run All NumPy Lessons
Execute all 20 NumPy lessons in sequence
"""
# type: ignore

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from numpy_lessons import (
    lesson01_numpy_arrays,
    lesson02_array_creation_functions,
    lesson03_array_attributes,
    lesson04_array_indexing,
    lesson05_array_reshaping,
    lesson06_array_operations,
    lesson07_mathematical_functions,
    lesson08_statistical_functions,
    lesson09_array_manipulation,
    lesson10_linear_algebra,
    lesson11_random_numbers,
    lesson12_broadcasting,
    lesson13_advanced_indexing,
    lesson14_sorting_searching,
    lesson15_performance_tips,
    lesson16_data_types,
    lesson17_saving_loading,
    lesson18_structured_arrays,
    lesson19_masked_arrays,
    lesson20_practical_examples,
)


def main():
    """Run all NumPy lessons"""
    lessons = [
        ("Lesson 1: Creating NumPy Arrays", lesson01_numpy_arrays),
        ("Lesson 2: Array Creation Functions", lesson02_array_creation_functions),
        ("Lesson 3: Array Attributes", lesson03_array_attributes),
        ("Lesson 4: Array Indexing and Slicing", lesson04_array_indexing),
        ("Lesson 5: Reshaping and Transposing", lesson05_array_reshaping),
        ("Lesson 6: Basic Array Operations", lesson06_array_operations),
        ("Lesson 7: Mathematical Functions", lesson07_mathematical_functions),
        ("Lesson 8: Statistical Functions", lesson08_statistical_functions),
        ("Lesson 9: Array Manipulation", lesson09_array_manipulation),
        ("Lesson 10: Linear Algebra", lesson10_linear_algebra),
        ("Lesson 11: Random Number Generation", lesson11_random_numbers),
        ("Lesson 12: Broadcasting", lesson12_broadcasting),
        ("Lesson 13: Advanced Indexing", lesson13_advanced_indexing),
        ("Lesson 14: Sorting and Searching", lesson14_sorting_searching),
        ("Lesson 15: Performance Tips", lesson15_performance_tips),
        ("Lesson 16: Data Types", lesson16_data_types),
        ("Lesson 17: Saving and Loading", lesson17_saving_loading),
        ("Lesson 18: Structured Arrays", lesson18_structured_arrays),
        ("Lesson 19: Masked Arrays", lesson19_masked_arrays),
        ("Lesson 20: Practical Examples", lesson20_practical_examples),
    ]
    
    print("\n" + "="*60)
    print("NUMPY LEARNING PROJECT - ALL LESSONS")
    print("="*60)
    print(f"Total lessons: {len(lessons)}")
    print("="*60)
    
    for i, (name, lesson_module) in enumerate(lessons, 1):
        try:
            print(f"\n[{i}/20] {name}")
            lesson_module.main()
        except Exception as e:
            print(f"\n❌ Error in {name}: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "="*60)
    print("✅ ALL LESSONS COMPLETED!")
    print("="*60)


if __name__ == "__main__":
    main()
