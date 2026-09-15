# Project 2: Student Data EDA - BCA 5th Sem
# Author: Stephen Ogeti - For MSc Data Science
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {'Name': ['Amit', 'Ravi', 'Sneha'], 'Marks': [85, 90, 78], 'Subject': ['Math', 'Math', 'Science']}
df = pd.DataFrame(data)

print(df.head())
print(df.describe())
print("EDA Project Completed")
