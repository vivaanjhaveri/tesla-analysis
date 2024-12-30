import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tesla_data.csv'
df = pd.read_csv(file_path)

# Data Cleaning
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Extract Year and Month
df['Year'] = df.index.year

# Year-wise Aggregates
yearly_aggregates = df.groupby('Year').agg({
    'Open': 'mean',
    'High': 'mean',
    'Low': 'mean',
    'Close': 'mean',
    'Volume': 'mean'
}).rename(columns={
    'Open': 'Average Open',
    'High': 'Average High',
    'Low': 'Average Low',
    'Close': 'Average Close',
    'Volume': 'Average Volume'
})

# Generate Year-wise Comparison Report
print("Year-wise Comparison Report")
print(yearly_aggregates)

# Visualization: Average Close Price by Year
plt.figure(figsize=(12, 6))
plt.plot(yearly_aggregates.index, yearly_aggregates['Average Close'], marker='o', label='Average Close Price', color='blue')
plt.title('Year-wise Average Close Price')
plt.xlabel('Year')
plt.ylabel('Average Price (USD)')
plt.grid()
plt.legend()
plt.show()

# Visualization: Average Volume by Year
plt.figure(figsize=(12, 6))
plt.bar(yearly_aggregates.index, yearly_aggregates['Average Volume'], color='purple')
plt.title('Year-wise Average Trading Volume')
plt.xlabel('Year')
plt.ylabel('Average Volume')
plt.grid()
plt.show()

# Save Report to CSV
yearly_aggregates.to_csv('/mnt/data/yearly_comparison_report.csv')