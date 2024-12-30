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