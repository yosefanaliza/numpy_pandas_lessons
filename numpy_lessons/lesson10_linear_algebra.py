"""
Lesson 10: Linear Algebra Operations
"""
# type: ignore

import numpy as np


def main():
    """Lesson 10: Linear Algebra Operations"""
    print("\n" + "="*60)
    print("LESSON 10: LINEAR ALGEBRA")
    print("="*60)
    
    # Matrix multiplication
    print("\n1. Matrix Multiplication:")
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(f"Matrix A:\n{A}")
    print(f"Matrix B:\n{B}")
    print(f"A @ B (matrix product):\n{A @ B}")
    print(f"np.matmul(A, B):\n{np.matmul(A, B)}")
    
    # Dot product
    print("\n2. Dot Product:")
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"Dot product: {np.dot(v1, v2)}")
    
    # Matrix determinant
    print("\n3. Matrix Determinant:")
    A = np.array([[1, 2], [3, 4]])
    print(f"Matrix:\n{A}")
    print(f"Determinant: {np.linalg.det(A)}")
    
    # Matrix inverse
    print("\n4. Matrix Inverse:")
    print(f"Inverse:\n{np.linalg.inv(A)}")
    
    # Eigenvalues and eigenvectors
    print("\n5. Eigenvalues and Eigenvectors:")
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(f"Eigenvalues: {eigenvalues}")
    print(f"Eigenvectors:\n{eigenvectors}")
    
    # Solving linear equations
    print("\n6. Solving Linear Equations (Ax = b):")
    A = np.array([[3, 1], [1, 2]])
    b = np.array([9, 8])
    x = np.linalg.solve(A, b)
    print(f"A:\n{A}")
    print(f"b: {b}")
    print(f"Solution x: {x}")
    print(f"Verification (A @ x): {A @ x}")


if __name__ == "__main__":
    main()
