import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Load Tesla dataset
file_path = 'tesla_data.csv'
df_tesla = pd.read_csv(file_path)
df_tesla['Date'] = pd.to_datetime(df_tesla['Date'], format='%m/%d/%y')  # Adjusted date format
df_tesla.set_index('Date', inplace=True)

# Major news events in 2023-2024 with approximate dates
events = {
    '2024-01-15': 'New Model Launch',
    '2024-04-20': 'Earnings Report Q1',
    '2024-07-20': 'Earnings Report Q2',
    '2024-10-20': 'Earnings Report Q3',
    '2024-11-05': 'US Presidential Election',
    '2023-03-01': 'Investor Day Event',
    '2023-10-01': 'Cybertruck Production Announcement'
}

# Filter Tesla data for 2023-2024
df_tesla = df_tesla[(df_tesla.index.year >= 2023) & (df_tesla.index.year <= 2024)]

# Adjust event dates to the nearest available trading day
adjusted_events = {}
for date, event in events.items():
    event_date = pd.to_datetime(date, format='%Y-%m-%d')
    if event_date in df_tesla.index:
        adjusted_events[event_date] = event
    else:
        nearest_index = df_tesla.index.get_indexer([event_date], method='nearest')[0]
        adjusted_events[df_tesla.index[nearest_index]] = event

# Generate unique colors for each event
colors = cm.tab10(np.linspace(0, 1, len(adjusted_events)))

# Plot stock prices with unique colors for each event
plt.figure(figsize=(12, 6))
plt.plot(df_tesla['Close'], label='Tesla Stock Price', color='blue')
for (date, event), color in zip(adjusted_events.items(), colors):
    plt.axvline(date, color=color, linestyle='--', alpha=1.0, label=event)

plt.title('Tesla Stock Prices with Major Events (2023-2024)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.5), ncol=2, frameon=False)  # Legend at the bottom
plt.grid()
plt.tight_layout()
plt.show()
