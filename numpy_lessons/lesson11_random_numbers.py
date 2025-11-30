"""
Lesson 11: Random Number Generation
"""
# type: ignore

import numpy as np


def main():
    """Lesson 11: Random Number Generation"""
    print("\n" + "="*60)
    print("LESSON 11: RANDOM NUMBER GENERATION")
    print("="*60)
    
    # Set seed for reproducibility
    print("\n1. Setting Random Seed:")
    np.random.seed(42)
    print(f"Random with seed 42: {np.random.rand(3)}")
    np.random.seed(42)
    print(f"Same seed, same result: {np.random.rand(3)}")
    
    # Random floats
    print("\n2. Random Floats [0, 1):")
    print(f"3 random floats: {np.random.rand(3)}")
    print(f"2x3 random array:\n{np.random.rand(2, 3)}")
    
    # Random integers
    print("\n3. Random Integers:")
    print(f"5 integers [0, 10): {np.random.randint(0, 10, 5)}")
    print(f"2x3 integers [1, 100]:\n{np.random.randint(1, 101, (2, 3))}")
    
    # Random choice
    print("\n4. Random Choice:")
    arr = np.array(['apple', 'banana', 'cherry', 'date'])
    print(f"Array: {arr}")
    print(f"Random choice: {np.random.choice(arr)}")
    print(f"3 random choices: {np.random.choice(arr, 3)}")
    print(f"Without replacement: {np.random.choice(arr, 3, replace=False)}")
    
    # Normal distribution
    print("\n5. Normal Distribution:")
    normal = np.random.randn(5)
    print(f"5 values from N(0,1): {normal}")
    custom_normal = np.random.normal(10, 2, 5)
    print(f"5 values from N(10,2): {custom_normal}")
    
    # Shuffle
    print("\n6. Shuffling:")
    arr = np.arange(10)
    print(f"Original: {arr}")
    np.random.shuffle(arr)
    print(f"Shuffled: {arr}")


if __name__ == "__main__":
    main()
