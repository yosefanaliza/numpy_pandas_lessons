"""
Lesson 7: Mathematical Functions
"""
# type: ignore

import numpy as np


def main():
    """Lesson 7: Mathematical Functions"""
    print("\n" + "="*60)
    print("LESSON 7: MATHEMATICAL FUNCTIONS")
    print("="*60)
    
    arr = np.array([1, 4, 9, 16, 25])
    
    # Basic math functions
    print("\n1. Basic Math Functions:")
    print(f"Array: {arr}")
    print(f"Square root: {np.sqrt(arr)}")
    print(f"Exponential: {np.exp([1, 2, 3])}")
    print(f"Logarithm: {np.log([1, 2.718, 7.389])}")
    print(f"Log10: {np.log10([1, 10, 100])}")
    
    # Trigonometric functions
    print("\n2. Trigonometric Functions:")
    angles = np.array([0, np.pi/2, np.pi])
    print(f"Angles: {angles}")
    print(f"Sine: {np.sin(angles)}")
    print(f"Cosine: {np.cos(angles)}")
    print(f"Tangent: {np.tan([0, np.pi/4])}")
    
    # Rounding functions
    print("\n3. Rounding Functions:")
    arr = np.array([1.2, 2.5, 3.7, 4.9])
    print(f"Array: {arr}")
    print(f"Round: {np.round(arr)}")
    print(f"Floor: {np.floor(arr)}")
    print(f"Ceil: {np.ceil(arr)}")
    
    # Absolute value
    print("\n4. Absolute Value:")
    arr = np.array([-1, -2, 3, -4])
    print(f"Array: {arr}")
    print(f"Absolute: {np.abs(arr)}")


if __name__ == "__main__":
    main()
