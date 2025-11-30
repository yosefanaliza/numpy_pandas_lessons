"""
Lesson 9: Array Manipulation
"""
# type: ignore

import numpy as np


def main():
    """Lesson 9: Array Manipulation"""
    print("\n" + "="*60)
    print("LESSON 9: ARRAY MANIPULATION")
    print("="*60)
    
    # Concatenate
    print("\n1. Concatenating arrays:")
    arr1 = np.array([[1, 2], [3, 4]])
    arr2 = np.array([[5, 6], [7, 8]])
    print(f"Array 1:\n{arr1}")
    print(f"Array 2:\n{arr2}")
    print(f"Concatenate vertically:\n{np.concatenate([arr1, arr2], axis=0)}")
    print(f"Concatenate horizontally:\n{np.concatenate([arr1, arr2], axis=1)}")
    
    # Stack
    print("\n2. Stacking arrays:")
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    print(f"vstack:\n{np.vstack([arr1, arr2])}")
    print(f"hstack: {np.hstack([arr1, arr2])}")
    
    # Split
    print("\n3. Splitting arrays:")
    arr = np.arange(12)
    print(f"Array: {arr}")
    split = np.split(arr, 3)
    print(f"Split into 3: {split}")
    
    # Append, Insert, Delete
    print("\n4. Append, Insert, Delete:")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Original: {arr}")
    print(f"Append 6: {np.append(arr, 6)}")
    print(f"Insert 99 at index 2: {np.insert(arr, 2, 99)}")
    print(f"Delete index 2: {np.delete(arr, 2)}")
    
    # Unique
    print("\n5. Finding unique elements:")
    arr = np.array([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    print(f"Array: {arr}")
    print(f"Unique: {np.unique(arr)}")
    unique, counts = np.unique(arr, return_counts=True)
    print(f"Unique with counts: {dict(zip(unique, counts))}")


if __name__ == "__main__":
    main()
