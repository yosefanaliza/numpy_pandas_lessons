"""
Lesson 3: Array Attributes and Properties
"""
# type: ignore

import numpy as np


def main():
    """Lesson 3: Array Attributes and Properties"""
    print("\n" + "="*60)
    print("LESSON 3: ARRAY ATTRIBUTES")
    print("="*60)
    
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    
    print(f"Array:\n{arr}")
    print(f"\nShape: {arr.shape}")
    print(f"Dimensions: {arr.ndim}")
    print(f"Size (total elements): {arr.size}")
    print(f"Data type: {arr.dtype}")
    print(f"Item size (bytes): {arr.itemsize}")
    print(f"Total bytes: {arr.nbytes}")
    print(f"Strides: {arr.strides}")


if __name__ == "__main__":
    main()
