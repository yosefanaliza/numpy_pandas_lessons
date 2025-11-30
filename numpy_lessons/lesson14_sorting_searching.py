"""
Lesson 14: Sorting and Searching
"""
# type: ignore

import numpy as np


def main():
    """Lesson 14: Sorting and Searching"""
    print("\n" + "="*60)
    print("LESSON 14: SORTING AND SEARCHING")
    print("="*60)
    
    # Sorting
    print("\n1. Sorting Arrays:")
    arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
    print(f"Original: {arr}")
    print(f"Sorted: {np.sort(arr)}")
    
    # Argsort
    print("\n2. Argsort (indices of sorted array):")
    indices = np.argsort(arr)
    print(f"Indices: {indices}")
    print(f"Sorted using indices: {arr[indices]}")
    
    # Sorting 2D arrays
    print("\n3. Sorting 2D Arrays:")
    arr2d = np.array([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
    print(f"Original:\n{arr2d}")
    print(f"Sort each row:\n{np.sort(arr2d, axis=1)}")
    print(f"Sort each column:\n{np.sort(arr2d, axis=0)}")
    
    # Searching
    print("\n4. Searching:")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(f"Array: {arr}")
    print(f"Index where value is 5: {np.where(arr == 5)}")
    print(f"Indices where value > 5: {np.where(arr > 5)}")
    
    # Max/Min with axis
    print("\n5. Max/Min with axis:")
    arr2d = np.array([[1, 5, 3], [4, 2, 6]])
    print(f"Array:\n{arr2d}")
    print(f"Max in each column: {np.max(arr2d, axis=0)}")
    print(f"Max in each row: {np.max(arr2d, axis=1)}")


if __name__ == "__main__":
    main()
