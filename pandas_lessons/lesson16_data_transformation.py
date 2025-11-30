"""
Pandas Lesson 16: Data Transformation
Learn how to apply functions, map values, bin data, and normalize values
"""
# type: ignore

import pandas as pd
import numpy as np


def main():
    """Lesson 16: Data Transformation"""
    print("\n" + "="*60)
    print("LESSON 16: DATA TRANSFORMATION")
    print("="*60)
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Score': [85, 92, 78, 95, 88],
        'Age': [25, 30, 35, 28, 32]
    })
    
    print("\n1. Original DataFrame:")
    print(df)
    
    # Apply function to column
    print("\n2. Apply function to Score (add 5 bonus points):")
    df['Adjusted_Score'] = df['Score'].apply(lambda x: x + 5)
    print(df)
    
    # Map values
    print("\n3. Map scores to grades:")
    def score_to_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'D'
    
    df['Grade'] = df['Score'].apply(score_to_grade)
    print(df)
    
    # Replace values
    print("\n4. Replace values using replace:")
    df_copy = df.copy()
    df_copy['Grade'] = df_copy['Grade'].replace({'A': 'Excellent', 'B': 'Good', 'C': 'Fair'})
    print(df_copy)
    
    # Binning
    print("\n5. Binning Age into categories:")
    bins = [0, 25, 30, 100]
    labels = ['Young', 'Middle', 'Senior']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    print(df)
    
    # Ranking
    print("\n6. Rank scores:")
    df['Rank'] = df['Score'].rank(ascending=False)
    print(df)
    
    # Normalize values
    print("\n7. Normalize scores (0-1 scale):")
    df['Normalized_Score'] = (df['Score'] - df['Score'].min()) / (df['Score'].max() - df['Score'].min())
    print(df)


if __name__ == "__main__":
    main()
