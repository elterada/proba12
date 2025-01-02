import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis

# Fetch data using yfinance
stock_symbol = 'AAPL'  # Example stock symbol
data = yf.download(stock_symbol, period='1y', interval='1d')

# Descriptive Statistics
mean_price = data['Close'].mean()
median_price = data['Close'].median()
std_dev = data['Close'].std()
variance = std_dev ** 2
min_price = data['Close'].min()
max_price = data['Close'].max()

# Skewness and Kurtosis
price_skewness = skew(data['Close'])
price_kurtosis = kurtosis(data['Close'])

# Daily Returns
data['Daily_Returns'] = data['Close'].pct_change() * 100

# Moving Averages
data['50_MA'] = data['Close'].rolling(window=50).mean()
data['200_MA'] = data['Close'].rolling(window=200).mean()

# RSI - Relative Strength Index
def compute_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

data['RSI'] = compute_rsi(data)

# MACD - Moving Average Convergence Divergence
exp12 = data['Close'].ewm(span=12, adjust=False).mean()
exp26 = data['Close'].ewm(span=26, adjust=False).mean()
data['MACD'] = exp12 - exp26
data['MACD_Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

# Plotting Price and Moving Averages
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Closing Price')
plt.plot(data['50_MA'], label='50-Day Moving Average')
plt.plot(data['200_MA'], label='200-Day Moving Average')
plt.title(f'{stock_symbol} Price and Moving Averages')
plt.legend()
plt.show()

# Exporting to Excel
save_to_excel = input("Do you want to export the data to an Excel file? (yes/no): ").strip().lower()
if save_to_excel == 'yes':
    data.to_excel(f'{stock_symbol}_analysis.xlsx')

# Displaying Results
print(f"\nDescriptive Statistics for {stock_symbol}:")
print(f"Mean: {mean_price}")
print(f"Median: {median_price}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
print(f"Min: {min_price}")
print(f"Max: {max_price}")
print(f"Skewness: {price_skewness}")
print(f"Kurtosis: {price_kurtosis}")
