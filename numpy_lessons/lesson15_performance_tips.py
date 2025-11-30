"""
Lesson 15: Performance Tips and Vectorization
"""
# type: ignore

import numpy as np
import time


def main():
    """Lesson 15: Performance Tips and Vectorization"""
    print("\n" + "="*60)
    print("LESSON 15: PERFORMANCE TIPS")
    print("="*60)
    
    # Vectorization vs loops
    print("\n1. Vectorization Performance:")
    size = 1000000
    arr = np.random.rand(size)
    
    # Using loops (slow)
    start = time.time()
    result_loop = []
    for x in arr:
        result_loop.append(x ** 2)
    loop_time = time.time() - start
    
    # Using vectorization (fast)
    start = time.time()
    result_vec = arr ** 2
    vec_time = time.time() - start
    
    print(f"Loop time: {loop_time:.6f} seconds")
    print(f"Vectorization time: {vec_time:.6f} seconds")
    print(f"Speedup: {loop_time / vec_time:.2f}x")
    
    # Memory views
    print("\n2. Views vs Copies:")
    arr = np.array([1, 2, 3, 4, 5])
    view = arr[1:4]
    copy = arr[1:4].copy()
    
    print(f"Original: {arr}")
    view[0] = 999
    print(f"After modifying view: {arr}")
    arr[2] = 3  # Reset
    copy[0] = 888
    print(f"After modifying copy: {arr}")
    
    # In-place operations
    print("\n3. In-place Operations:")
    arr = np.array([1, 2, 3, 4, 5])
    print(f"Original: {arr}")
    arr += 10
    print(f"After += 10: {arr}")


if __name__ == "__main__":
    main()
