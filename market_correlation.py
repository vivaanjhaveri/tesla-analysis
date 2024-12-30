import pandas as pd
import matplotlib.pyplot as plt

# Load Tesla dataset
file_path_tesla = 'tesla_data.csv'
df_tesla = pd.read_csv(file_path_tesla)
df_tesla['Date'] = pd.to_datetime(df_tesla['Date'])
df_tesla.set_index('Date', inplace=True)

# Load S&P 500 dataset
file_path_sp500 = 'sp500_data.csv'
df_sp500 = pd.read_csv(file_path_sp500)
df_sp500['Date'] = pd.to_datetime(df_sp500['Date'], format='%m/%d/%Y')
df_sp500.rename(columns={'Price': 'S&P 500 Price'}, inplace=True)
df_sp500['S&P 500 Price'] = df_sp500['S&P 500 Price'].str.replace(',', '').astype(float)
df_sp500.set_index('Date', inplace=True)

# Align datasets by date range
df_tesla = df_tesla['Close']
df_sp500 = df_sp500['S&P 500 Price']
df_combined = pd.concat([df_tesla, df_sp500], axis=1, join='inner')
df_combined.columns = ['Tesla', 'S&P 500']

# Calculate Yearly Percentage Change
df_combined['Tesla Yearly Change'] = df_combined['Tesla'].resample('Y').ffill().pct_change() * 100
df_combined['S&P 500 Yearly Change'] = df_combined['S&P 500'].resample('Y').ffill().pct_change() * 100

# Drop NaN values resulting from percentage change
df_yearly = df_combined[['Tesla Yearly Change', 'S&P 500 Yearly Change']].dropna()

# Plot Yearly Percentage Change
plt.figure(figsize=(12, 6))
plt.plot(df_yearly.index, df_yearly['Tesla Yearly Change'], label='Tesla Yearly Change', marker='o', color='blue')
plt.plot(df_yearly.index, df_yearly['S&P 500 Yearly Change'], label='S&P 500 Yearly Change', marker='o', color='orange')
plt.title('Yearly Percentage Change: Tesla vs S&P 500')
plt.xlabel('Year')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid()
plt.show()

# Save Yearly Percentage Change to CSV
df_yearly.to_csv('/mnt/data/tesla_sp500_yearly_change.csv')