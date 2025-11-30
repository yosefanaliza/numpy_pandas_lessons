"""
Lesson 8: Statistical Functions
"""
# type: ignore

import numpy as np


def main():
    """Lesson 8: Statistical Functions"""
    print("\n" + "="*60)
    print("LESSON 8: STATISTICAL FUNCTIONS")
    print("="*60)
    
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print(f"Array:\n{arr}")
    
    # Basic statistics
    print("\n1. Basic Statistics:")
    print(f"Sum: {np.sum(arr)}")
    print(f"Sum by column: {np.sum(arr, axis=0)}")
    print(f"Sum by row: {np.sum(arr, axis=1)}")
    print(f"Mean: {np.mean(arr)}")
    print(f"Median: {np.median(arr)}")
    print(f"Standard deviation: {np.std(arr)}")
    print(f"Variance: {np.var(arr)}")

    # Min/Max
    print("\n2. Min/Max:")
    print(f"Min: {np.min(arr)}")
    print(f"Max: {np.max(arr)}")
    print(f"Argmin (index of min): {np.argmin(arr)}")
    print(f"Argmax (index of max): {np.argmax(arr)}")
    
    # Percentiles
    print("\n3. Percentiles:")
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Data: {data}")
    print(f"25th percentile: {np.percentile(data, 25)}")
    print(f"50th percentile: {np.percentile(data, 50)}")
    print(f"75th percentile: {np.percentile(data, 75)}")
    
    # Cumulative operations
    print("\n4. Cumulative Operations:")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Array: {arr}")
    print(f"Cumulative sum: {np.cumsum(arr)}")
    print(f"Cumulative product: {np.cumprod(arr)}")


if __name__ == "__main__":
    main()
