"""
Pandas Lesson 1: Working with Series
Learn the basics of Pandas Series - one-dimensional labeled arrays
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 1: Working with Series"""
    print("\n" + "="*60)
    print("LESSON 1: WORKING WITH SERIES")
    print("="*60)
    
    # Creating a Series from a list
    print("\n1. Creating a Series from a list:")
    fruits = pd.Series(['Apple', 'Banana', 'Cherry', 'Date'])
    print(fruits)
    
    # Creating a Series with custom index
    print("\n2. Series with custom index:")
    prices = pd.Series([1.50, 0.75, 2.00, 3.50], index=['Apple', 'Banana', 'Cherry', 'Date'])
    print(prices)
    
    # Creating a Series from a dictionary
    print("\n3. Series from a dictionary:")
    stock = pd.Series({'Apple': 100, 'Banana': 150, 'Cherry': 75})
    print(stock)
    
    # Accessing elements
    print("\n4. Accessing elements:")
    print(f"Price of Apple: ${prices['Apple']}")
    print(f"First item: {fruits[0]}")
    
    # Series operations
    print("\n5. Series operations (10% discount):")
    discounted_prices = prices * 0.9
    print(discounted_prices)
    
    # Series attributes
    print("\n6. Series attributes:")
    print(f"Values: {prices.values}")
    print(f"Index: {prices.index}")
    print(f"Size: {prices.size}")


if __name__ == "__main__":
    main()
