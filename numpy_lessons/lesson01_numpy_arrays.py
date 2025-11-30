"""
Lesson 1: Creating NumPy Arrays
"""
# type: ignore



import numpy as np


def main():
    """Lesson 1: Creating NumPy Arrays"""
    print("\n" + "="*60)
    print("LESSON 1: CREATING NUMPY ARRAYS")
    print("="*60)
    
    # From Python lists
    print("\n1. Creating arrays from lists:")

    arr1 = np.array([1, 2, 3, 4, 5])
    
    print(f"1D Array: {arr1}")
    print(f"Type: {type(arr1)}")
    print(f"Data type: {arr1.dtype}")
    
    # 2D arrays
    print("\n2. Creating 2D arrays:")
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2D Array:\n{arr2}")
    print(f"Shape: {arr2.shape}")
    print(f"Dimensions: {arr2.ndim}")
    
    # 3D arrays
    print("\n3. Creating 3D arrays:")
    arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    print(f"3D Array:\n{arr3}")
    print(f"Shape: {arr3.shape}")
    
    # Specifying data types
    print("\n4. Specifying data types:")
    float_arr = np.array([1, 2, 3], dtype=float)
    print(f"Float array: {float_arr}")
    int_arr = np.array([1.5, 2.7, 3.9], dtype=int)
    print(f"Int array (truncated): {int_arr}")


if __name__ == "__main__":
    main()
