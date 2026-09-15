# Project 3: Sales Data Visualization - BCA 5th Sem
# Author: Stephen Ogeti - For MSc Data Science
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = {'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [200, 250, 300]}
df = pd.DataFrame(data)

plt.plot(df['Month'], df['Sales'])
plt.title("Sales Report")
plt.savefig("sales_chart.png")
print("Visualization Project Completed")
