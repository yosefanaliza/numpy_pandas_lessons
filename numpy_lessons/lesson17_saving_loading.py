"""
Lesson 17: Saving and Loading Arrays
"""
# type: ignore

import numpy as np
import os


def main():
    """Lesson 17: Saving and Loading Arrays"""
    print("\n" + "="*60)
    print("LESSON 17: SAVING AND LOADING ARRAYS")
    print("="*60)
    
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    
    # Save to binary file
    print("\n1. Saving to .npy file:")
    np.save('temp_array.npy', arr)
    print(f"Saved array:\n{arr}")
    
    # Load from binary file
    print("\n2. Loading from .npy file:")
    loaded = np.load('temp_array.npy')
    print(f"Loaded array:\n{loaded}")
    
    # Save multiple arrays
    print("\n3. Saving multiple arrays:")
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    np.savez('temp_arrays.npz', first=arr1, second=arr2)
    
    # Load multiple arrays
    print("\n4. Loading multiple arrays:")
    data = np.load('temp_arrays.npz')
    print(f"First: {data['first']}")
    print(f"Second: {data['second']}")
    data.close()  # Close the file handle
    
    # Save to text file
    print("\n5. Saving to text file:")
    np.savetxt('temp_array.txt', arr, fmt='%d')
    loaded_txt = np.loadtxt('temp_array.txt', dtype=int)
    print(f"Loaded from text:\n{loaded_txt}")
    
    # Clean up
    try:
        os.remove('temp_array.npy')
        os.remove('temp_arrays.npz')
        os.remove('temp_array.txt')
        print("\nTemporary files cleaned up")
    except Exception as e:
        print(f"\nNote: Some temp files may still exist: {e}")


if __name__ == "__main__":
    main()
