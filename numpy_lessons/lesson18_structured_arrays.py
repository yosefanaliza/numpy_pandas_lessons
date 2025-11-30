"""
Lesson 18: Structured Arrays
"""
# type: ignore

import numpy as np


def main():
    """Lesson 18: Structured Arrays"""
    print("\n" + "="*60)
    print("LESSON 18: STRUCTURED ARRAYS")
    print("="*60)
    
    # Creating structured arrays
    print("\n1. Creating Structured Arrays:")
    dt = np.dtype([('name', 'U10'), ('age', 'i4'), ('salary', 'f8')])
    employees = np.array([
        ('Alice', 25, 50000.0),
        ('Bob', 30, 60000.0),
        ('Charlie', 35, 75000.0)
    ], dtype=dt)
    
    print(f"Employees:\n{employees}")
    print(f"Names: {employees['name']}")
    print(f"Ages: {employees['age']}")
    print(f"Salaries: {employees['salary']}")
    
    # Accessing and modifying
    print("\n2. Accessing Individual Records:")
    print(f"First employee: {employees[0]}")
    print(f"Bob's salary: {employees[1]['salary']}")
    
    # Filtering
    print("\n3. Filtering Structured Arrays:")
    high_earners = employees[employees['salary'] > 55000]
    print(f"High earners:\n{high_earners}")


if __name__ == "__main__":
    main()
