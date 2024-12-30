import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tesla_data.csv'
df = pd.read_csv(file_path)

# Data Cleaning and Preprocessing
# Remove unnecessary columns
df.drop(columns=['Unnamed: 0'], inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set 'Date' as the index for time series analysis
df.set_index('Date', inplace=True)

# Display basic information about the dataset
print("Dataset Information:")
df.info()
print("\nBasic Statistics:")
print(df.describe())

# Plotting Stock Prices
plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.title('Tesla Stock Closing Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# Analyze Moving Averages
# 50-day and 200-day moving averages
df['50_MA'] = df['Close'].rolling(window=50).mean()
df['200_MA'] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.plot(df['50_MA'], label='50-Day MA', color='orange')
plt.plot(df['200_MA'], label='200-Day MA', color='green')
plt.title('Tesla Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# Volume Analysis
plt.figure(figsize=(12, 6))
plt.bar(df.index, df['Volume'], color='purple')
plt.title('Tesla Stock Trading Volume Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.grid()
plt.show()

# Save cleaned dataset for further analysis
df.to_csv('/mnt/data/cleaned_tesla_stock.csv')
