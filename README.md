# Tesla Stock Analysis Project

This project analyzes Tesla's stock performance and compares it with market indices, key events, and forecasts future trends using time series models. Below is a detailed description of each file included in the project.

---

## Files and Descriptions

### `2024_analysis.py`
- **Description**: Analyzes Tesla's stock trends for the year 2024, including statistical summaries and visualizations of price changes and moving averages.
- **Execution**:
  ```bash
  python 2024_analysis.py
  ```
  This script generates plots and saves results for further analysis.

### `2025_time_series_forecasting.py`
- **Description**: Uses ARIMA models to forecast Tesla's stock prices for the year 2025, visualizing predicted trends along with confidence intervals.
- **Execution**:
  ```bash
  python 2025_time_series_forecasting.py
  ```
  Outputs include prediction graphs and a CSV file containing the forecasted values.

### `market_correlation.py`
- **Description**: Compares Tesla's stock performance with the S&P 500, focusing on percentage changes (yearly and monthly). Provides correlation analysis and visualizations.
- **Execution**:
  ```bash
  python market_correlation.py
  ```
  This script calculates correlations and saves the data to CSV.

### `overall_analysis.py`
- **Description**: Combines various analyses to provide an overarching view of Tesla's stock performance, including key statistics and trends.
- **Execution**:
  ```bash
  python overall_analysis.py
  ```
  Outputs include multiple visualizations and summaries.

### `tesla_stock_events_chart.py`
- **Description**: Annotates Tesla's stock price chart with major news events from 2023-2024. Events are represented as vertical lines with labels.
- **Execution**:
  ```bash
  python tesla_stock_events_chart.py
  ```
  Generates a chart with event annotations and saves it as an image.

### `yearwise_comparison.py`
- **Description**: Compares Tesla's stock price changes year-over-year, providing percentage changes and visualizations.
- **Execution**:
  ```bash
  python yearwise_comparison.py
  ```
  Outputs a year-over-year comparison chart and saves the data to CSV.

---

## Data Files

### `sp500_data.csv`
- **Description**: Contains historical data for the S&P 500 index used for market correlation analyses.
- **Usage**: Read by `market_correlation.py` and other scripts for comparative analyses.

### `tesla_data.csv`
- **Description**: Contains Tesla's historical stock price data.
- **Usage**: Primary dataset for all scripts.

---

## How to Run the Project
1. Ensure Python and necessary libraries (`pandas`, `matplotlib`, `numpy`, etc.) are installed.
2. Place all `.py` and `.csv` files in the same directory.
3. Execute the desired script from the command line using:
   ```bash
   python <script_name.py>
   ```

---

## Outputs
- **Visualizations**: Saved as `.png` files in the same directory as the scripts.
- **Data Exports**: Saved as `.csv` files for further analysis.

---

## Requirements
- Python 3.7+
- Required libraries:
  - `pandas`
  - `matplotlib`
  - `numpy`
  - `statsmodels`
