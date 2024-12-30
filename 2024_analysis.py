import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tesla_data.csv'
df = pd.read_csv(file_path)

# Data Cleaning
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for the year 2024
df_2024 = df[df['Date'].dt.year == 2024]

# Basic Statistics for 2024
stats_2024 = df_2024.describe()
print("Tesla Stock Statistics for 2024:")
print(stats_2024)

# Plotting Trends for 2024
plt.figure(figsize=(12, 6))
plt.plot(df_2024['Date'], df_2024['Close'], label='Closing Price', color='blue')
plt.title('Tesla Stock Closing Prices in 2024')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(df_2024['Date'], df_2024['Volume'], color='purple')
plt.title('Tesla Stock Trading Volume in 2024')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid()
plt.show()

# Moving Average Analysis (30-day and 90-day)
df_2024.set_index('Date', inplace=True)
df_2024['30_MA'] = df_2024['Close'].rolling(window=30).mean()
df_2024['90_MA'] = df_2024['Close'].rolling(window=90).mean()

plt.figure(figsize=(12, 6))
plt.plot(df_2024['Close'], label='Closing Price', color='blue')
plt.plot(df_2024['30_MA'], label='30-Day MA', color='orange')
plt.plot(df_2024['90_MA'], label='90-Day MA', color='green')
plt.title('Tesla Stock Price with Moving Averages in 2024')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# Save Filtered Data for 2024
df_2024.to_csv('/mnt/data/tesla_2024_analysis.csv')
