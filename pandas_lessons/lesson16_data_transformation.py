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
    
    # Drop columns
    print("\n8. Drop columns using .drop():")
    df_dropped = df.drop(columns=['Adjusted_Score', 'Normalized_Score'])
    print(df_dropped)
    
    print("\n9. Drop multiple columns:")
    df_minimal = df.drop(['Adjusted_Score', 'Normalized_Score', 'Age_Group'], axis=1)
    print(df_minimal)
    
    print("\n10. Drop rows by index:")
    df_drop_rows = df.drop([0, 2])  # Drop rows at index 0 and 2
    print(df_drop_rows)
    
    # Assign new columns
    print("\n11. Create new columns using .assign():")
    df_assigned = df.assign(
        Double_Score=df['Score'] * 2,
        Is_Adult=df['Age'] >= 30
    )
    print(df_assigned[['Name', 'Score', 'Double_Score', 'Age', 'Is_Adult']])
    
    print("\n12. Chain multiple assignments:")
    df_chain = df.assign(
        Score_Plus_Age=lambda x: x['Score'] + x['Age'],
        Name_Upper=lambda x: x['Name'].str.upper()
    )
    print(df_chain[['Name', 'Name_Upper', 'Score', 'Age', 'Score_Plus_Age']])
    
    # Rename columns
    print("\n13. Rename columns using .rename():")
    df_renamed = df.rename(columns={
        'Name': 'Student_Name',
        'Score': 'Test_Score',
        'Age': 'Student_Age'
    })
    print(df_renamed.head())
    
    print("\n14. Rename with a function:")
    df_upper = df.rename(columns=str.upper)
    print(df_upper.head())
    
    print("\n15. Rename index:")
    df_rename_index = df.rename(index={0: 'First', 1: 'Second', 2: 'Third'})
    print(df_rename_index.head())
    
    # Melt (wide to long format)
    print("\n16. Melt - transform wide to long format:")
    df_wide = pd.DataFrame({
        'Student': ['Alice', 'Bob', 'Charlie'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 95],
        'English': [88, 85, 82]
    })
    print("Wide format:")
    print(df_wide)
    
    df_melted = df_wide.melt(id_vars=['Student'], var_name='Subject', value_name='Score')
    print("\nLong format (melted):")
    print(df_melted)
    
    print("\n17. Melt with multiple id columns:")
    df_multi = pd.DataFrame({
        'Name': ['Alice', 'Bob'],
        'Class': ['A', 'B'],
        'Math': [85, 90],
        'Science': [92, 88]
    })
    df_melted_multi = df_multi.melt(
        id_vars=['Name', 'Class'],
        var_name='Subject',
        value_name='Grade'
    )
    print(df_melted_multi)


if __name__ == "__main__":
    main()
