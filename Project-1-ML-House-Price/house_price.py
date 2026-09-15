# Project 1: House Price Prediction - BCA 5th Sem
# Author: Stephen Ogeti - For MSc Data Science Application
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample Data
data = {'Size': [1000, 1500, 2000, 2500], 'Price': [50, 75, 100, 125]}
df = pd.DataFrame(data)

# Model
X = df[['Size']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)

print("Model Trained Successfully for MSc Project")
