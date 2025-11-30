"""
Lesson 4: Array Indexing and Slicing
"""
# type: ignore

import numpy as np


def main():
    """Lesson 4: Array Indexing and Slicing"""
    print("\n" + "="*60)
    print("LESSON 4: ARRAY INDEXING AND SLICING")
    print("="*60)
    
    # 1D indexing
    print("\n1. 1D Array Indexing:")
    arr1d = np.array([10, 20, 30, 40, 50])
    print(f"Array: {arr1d}")
    print(f"First element: {arr1d[0]}")
    print(f"Last element: {arr1d[-1]}")
    print(f"Slice [1:4]: {arr1d[1:4]}")
    print(f"Every other element: {arr1d[::2]}")
    
    # 2D indexing
    print("\n2. 2D Array Indexing:")
    arr2d = np.array(
        [[1, 2, 3], # 0
         [4, 5, 6], # 1
         [7, 8, 9]] # 2
        )
    print(f"Array:\n{arr2d}")
    print(f"Element at [1,2]: {arr2d[1, 2]}")
    print(f"First row: {arr2d[0]}")
    print(f"First column: {arr2d[:, 0]}")
    print(f"Subarray [0:2, 1:3]:\n{arr2d[0:2, 1:3]}")
    
    # Boolean indexing
    print("\n3. Boolean Indexing:")
    arr = np.array([1, 2, 3, 4, 5, 6])
    print(f"Array: {arr}")
    mask = arr > 3
    print(f"Mask (arr > 3): {mask}")
    print(f"Elements > 3: {arr[mask]}")
    
    # Fancy indexing
    print("\n4. Fancy Indexing:")
    arr = np.array([10, 20, 30, 40, 50])
    indices = [0, 2, 4]
    print(f"Array: {arr}")
    print(f"Elements at indices {indices}: {arr[indices]}")


if __name__ == "__main__":
    main()
