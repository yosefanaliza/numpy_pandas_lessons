"""
Lesson 13: Advanced Indexing Techniques
"""
# type: ignore

import numpy as np


def main():
    """Lesson 13: Advanced Indexing Techniques"""
    print("\n" + "="*60)
    print("LESSON 13: ADVANCED INDEXING")
    print("="*60)
    
    # Integer array indexing
    print("\n1. Integer Array Indexing:")
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Array:\n{arr}")
    rows = np.array([0, 1, 2])
    cols = np.array([0, 1, 2])
    print(f"Diagonal elements: {arr[rows, cols]}")
    
    # Boolean masking
    print("\n2. Boolean Masking:")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Array: {arr}")
    even_mask = arr % 2 == 0
    print(f"Even numbers: {arr[even_mask]}")
    
    # Combined conditions
    print("\n3. Combined Conditions:")
    print(f"Between 3 and 7: {arr[(arr > 3) & (arr < 7)]}")
    print(f"Less than 3 OR greater than 7: {arr[(arr < 3) | (arr > 7)]}")
    
    # np.where
    print("\n4. Using np.where:")
    arr = np.array([1, 2, 3, 4, 5])
    result = np.where(arr > 3, arr * 2, arr)
    print(f"Original: {arr}")
    print(f"Double if >3, else keep: {result}")
    
    # np.select
    print("\n5. Using np.select:")
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    conditions = [arr < 3, (arr >= 3) & (arr < 7), arr >= 7]
    choices = ['small', 'medium', 'large']
    result = np.select(conditions, choices, default='unknown')
    print(f"Array: {arr}")
    print(f"Categories: {result}")


if __name__ == "__main__":
    main()
