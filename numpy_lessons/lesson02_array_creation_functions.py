"""
Lesson 2: Array Creation Functions
"""
# type: ignore

import numpy as np


def main():
    """Lesson 2: Array Creation Functions"""
    print("\n" + "="*60)
    print("LESSON 2: ARRAY CREATION FUNCTIONS")
    print("="*60)
    
    # zeros
    print("\n1. Creating arrays of zeros:")
    zeros = np.zeros(5)
    print(f"1D zeros: {zeros}")
    zeros_2d = np.zeros((3, 4))
    print(f"2D zeros:\n{zeros_2d}")
    
    # ones
    print("\n2. Creating arrays of ones:")
    ones = np.ones((2, 3), dtype=int)
    print(f"2D ones:\n{ones}")
    
    # full
    print("\n3. Creating arrays with a specific value:")
    full = np.full((2, 3), 7)
    print(f"Array filled with 7:\n{full}")
    
    # arange
    print("\n4. Creating ranges:")
    range_arr = np.arange(0, 10, 2)
    print(f"Range 0-10 step 2: {range_arr}")
    
    # linspace
    print("\n5. Creating linearly spaced arrays:")
    linear = np.linspace(0, 10, 4)
    print(f"5 values from 0 to 1: {linear}")
    
    # eye (identity matrix)
    print("\n6. Creating identity matrix:")
    identity = np.eye(6)
    print(f"6x6 Identity matrix:\n{identity}")
    
    # random arrays
    print("\n7. Creating random arrays:")
    random_arr = np.random.rand(3, 3)
    print(f"Random 3x3 array:\n{random_arr}")
    random_int = np.random.randint(0, 10, (2, 3))
    print(f"Random integers:\n{random_int}")


if __name__ == "__main__":
    main()
