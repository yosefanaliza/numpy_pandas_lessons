"""
Lesson 20: Practical Examples
"""
# type: ignore

import numpy as np


def main():
    """Lesson 20: Practical Examples"""
    print("\n" + "="*60)
    print("LESSON 20: PRACTICAL EXAMPLES")
    print("="*60)
    
    # Example 1: Image processing basics
    print("\n1. Image Processing Basics (simulated):")
    image = np.random.randint(0, 256, (5, 5))
    print(f"Simulated grayscale image:\n{image}")
    normalized = image / 255.0
    print(f"Normalized [0,1]:\n{normalized}")
    
    # Example 2: Matrix operations
    print("\n2. Covariance Matrix:")
    data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Data:\n{data}")
    cov_matrix = np.cov(data, rowvar=False)
    print(f"Covariance matrix:\n{cov_matrix}")
    
    # Example 3: Polynomial fitting
    print("\n3. Polynomial Fitting:")
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])
    coeffs = np.polyfit(x, y, 1)
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"Linear fit coefficients: {coeffs}")
    print(f"Equation: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
    
    # Example 4: Moving average
    print("\n4. Moving Average:")
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    window = 3
    moving_avg = np.convolve(data, np.ones(window)/window, mode='valid')
    print(f"Data: {data}")
    print(f"Moving average (window={window}): {moving_avg}")
    
    # Example 5: Finding peaks
    print("\n5. Finding Local Maxima:")
    data = np.array([1, 3, 7, 1, 2, 6, 0, 1])
    peaks = (data[1:-1] > data[:-2]) & (data[1:-1] > data[2:])
    peak_indices = np.where(peaks)[0] + 1
    print(f"Data: {data}")
    print(f"Peak indices: {peak_indices}")
    print(f"Peak values: {data[peak_indices]}")


if __name__ == "__main__":
    main()
