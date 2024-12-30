import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'tesla_data.csv'
df = pd.read_csv(file_path)

# Data Cleaning
# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Use 'Close' prices for forecasting
series = df['Close']

# Train-Test Split
train = series[series.index.year < 2025]  # Use data before 2025 for training

# ARIMA Model Training
model = ARIMA(train, order=(5, 1, 0))  # Adjust order based on diagnostics
model_fit = model.fit()

# Forecast for the months of 2025
forecast_steps = 12  # Monthly forecast for 2025 (1 step per month)
forecast_index = pd.date_range(start='2025-01-01', periods=forecast_steps, freq='M')
forecast = model_fit.get_forecast(steps=forecast_steps)
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Plot Forecast
plt.figure(figsize=(12, 6))
plt.plot(series, label='Historical Data', color='blue')
plt.plot(forecast_index, forecast_mean, label='Forecast', color='orange')
plt.fill_between(forecast_index, 
                 forecast_ci.iloc[:, 0], 
                 forecast_ci.iloc[:, 1], 
                 color='orange', alpha=0.3, label='Confidence Interval')
plt.title('Tesla Stock Price Forecast for 2025')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid()
plt.show()

# Create Table of Predicted Prices
forecast_results = pd.DataFrame({
    'Date': forecast_index,
    'Forecasted Price': forecast_mean,
    'Lower Bound': forecast_ci.iloc[:, 0],
    'Upper Bound': forecast_ci.iloc[:, 1]
})
print("Monthly Predicted Prices for 2025:")
print(forecast_results)

# Save Forecast Results
forecast_results = pd.DataFrame({
    'Date': forecast_index,
    'Forecasted Price': forecast_mean,
    'Lower Bound': forecast_ci.iloc[:, 0],
    'Upper Bound': forecast_ci.iloc[:, 1]
})
forecast_results.to_csv('/mnt/data/tesla_forecast_2025.csv', index=False)