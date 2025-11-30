"""
Lesson 12: Broadcasting in Detail
"""
# type: ignore

import numpy as np


def main():
    """Lesson 12: Broadcasting in Detail"""
    print("\n" + "="*60)
    print("LESSON 12: BROADCASTING")
    print("="*60)
    
    # Scalar and array
    print("\n1. Scalar and Array:")
    arr = np.array([1, 2, 3, 4])
    print(f"Array: {arr}")
    print(f"Array + 10: {arr + 10}")
    
    # 1D and 2D
    print("\n2. 1D and 2D Broadcasting:")
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    arr1d = np.array([10, 20, 30])
    print(f"2D Array:\n{arr2d}")
    print(f"1D Array: {arr1d}")
    print(f"2D + 1D:\n{arr2d + arr1d}")
    
    # Column broadcasting
    print("\n3. Column Broadcasting:")
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    col = np.array([[10], [20]])
    print(f"2D Array:\n{arr2d}")
    print(f"Column:\n{col}")
    print(f"2D + Column:\n{arr2d + col}")
    
    # Complex broadcasting
    print("\n4. Complex Broadcasting:")
    a = np.arange(3).reshape(3, 1)
    b = np.arange(3)
    print(f"a (3x1):\n{a}")
    print(f"b (3,): {b}")
    print(f"a + b:\n{a + b}")


if __name__ == "__main__":
    main()
