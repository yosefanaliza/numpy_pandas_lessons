"""
Lesson 6: Basic Array Operations
"""
# type: ignore

import numpy as np


def main():
    """Lesson 6: Basic Array Operations"""
    print("\n" + "="*60)
    print("LESSON 6: BASIC ARRAY OPERATIONS")
    print("="*60)
    
    arr1 = np.array([1, 2, 3, 4])
    arr2 = np.array([10, 20, 30, 40])
    
    # Arithmetic operations
    print("\n1. Arithmetic Operations:")
    print(f"arr1: {arr1}")
    print(f"arr2: {arr2}")
    print(f"Addition: {arr1 + arr2}")
    print(f"Subtraction: {arr2 - arr1}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Division: {arr2 / arr1}")
    print(f"Power: {arr1 ** 2}")
    print(f"Modulo: {arr2 % 3}")
    
    # Broadcasting
    print("\n2. Broadcasting:")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Array:\n{arr}")
    print(f"Add 10:\n{arr + 10}")
    print(f"Multiply by 2:\n{arr * 2}")
    
    # Comparison operations
    print("\n3. Comparison Operations:")
    print(f"arr1 > 2: {arr1 > 2}")
    print(f"arr1 == 3: {arr1 == 3}")


    # =========================
    arr = np.array([11, 23, 54, 65, 76, 87, 1, 334, 90, 99])
    print(arr[arr > 50])

if __name__ == "__main__":
    main()
