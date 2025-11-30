"""
Lesson 19: Masked Arrays (Handling Missing Data)
"""
# type: ignore

import numpy as np


def main():
    """Lesson 19: Masked Arrays (Handling Missing Data)"""
    print("\n" + "="*60)
    print("LESSON 19: MASKED ARRAYS")
    print("="*60)
    
    # Creating masked arrays
    print("\n1. Creating Masked Arrays:")
    data = np.array([1, 2, -999, 4, -999, 6])
    masked_arr = np.ma.masked_equal(data, -999)
    print(f"Original data: {data}")
    print(f"Masked array: {masked_arr}")
    
    # Operations with masked arrays
    print("\n2. Operations with Masked Arrays:")
    print(f"Mean (ignoring masked): {masked_arr.mean()}")
    print(f"Sum (ignoring masked): {masked_arr.sum()}")
    
    # Custom masking
    print("\n3. Custom Masking:")
    data = np.array([1, 2, 3, 4, 5, 6])
    mask = np.array([False, False, True, False, True, False])
    masked_arr = np.ma.array(data, mask=mask)
    print(f"Data: {data}")
    print(f"Mask: {mask}")
    print(f"Masked array: {masked_arr}")
    print(f"Mean: {masked_arr.mean()}")


if __name__ == "__main__":
    main()
