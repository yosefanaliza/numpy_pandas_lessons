"""
Lesson 5: Reshaping and Transposing Arrays
"""
# type: ignore

import numpy as np


def main():
    """Lesson 5: Reshaping and Transposing Arrays"""
    print("\n" + "="*60)
    print("LESSON 5: RESHAPING AND TRANSPOSING")
    print("="*60)
    
    # Reshape
    print("\n1. Reshaping arrays:")
    arr = np.arange(12)
    print(f"Original: {arr}")
    reshaped = arr.reshape(3, 4)
    print(f"Reshaped to 3x4:\n{reshaped}")
    reshaped_3d = arr.reshape(2, 2, 3)
    print(f"Reshaped to 2x2x3:\n{reshaped_3d}")
    
    # Flatten
    print("\n2. Flattening arrays:")
    arr2d = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr2d}")
    flattened = arr2d.flatten()
    print(f"Flattened: {flattened}")
    raveled = arr2d.ravel()
    print(f"Raveled: {raveled}")
    
    # Transpose
    print("\n3. Transposing arrays:")
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Original:\n{arr}")
    print(f"Transposed:\n{arr.T}")
    
    # Adding dimensions
    print("\n4. Adding dimensions:")
    arr = np.array([1, 2, 3])
    print(f"Original shape: {arr.shape}")
    expanded = arr[np.newaxis, :]
    print(f"After newaxis: {expanded.shape}")
    expanded2 = np.expand_dims(arr, axis=0)
    print(f"After expand_dims: {expanded2.shape}")


if __name__ == "__main__":
    main()
