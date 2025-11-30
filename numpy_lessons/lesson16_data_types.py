"""
Lesson 16: Working with Data Types
"""
# type: ignore

import numpy as np


def main():
    """Lesson 16: Working with Data Types"""
    print("\n" + "="*60)
    print("LESSON 16: DATA TYPES")
    print("="*60)
    
    # Different data types
    print("\n1. Different Data Types:")
    int_arr = np.array([1, 2, 3], dtype=np.int32)
    float_arr = np.array([1, 2, 3], dtype=np.float64)
    bool_arr = np.array([True, False, True], dtype=np.bool_)
    str_arr = np.array(['a', 'b', 'c'], dtype=np.str_)
    
    print(f"int32: {int_arr}, dtype: {int_arr.dtype}")
    print(f"float64: {float_arr}, dtype: {float_arr.dtype}")
    print(f"bool: {bool_arr}, dtype: {bool_arr.dtype}")
    print(f"str: {str_arr}, dtype: {str_arr.dtype}")
    
    # Type conversion
    print("\n2. Type Conversion:")
    float_arr = np.array([1.5, 2.7, 3.9])
    print(f"Float array: {float_arr}")
    int_arr = float_arr.astype(int)
    print(f"Converted to int: {int_arr}")
    
    # Checking types
    print("\n3. Checking Types:")
    arr = np.array([1, 2, 3])
    print(f"Is integer type: {np.issubdtype(arr.dtype, np.integer)}")
    print(f"Is float type: {np.issubdtype(arr.dtype, np.floating)}")


if __name__ == "__main__":
    main()
