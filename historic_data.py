import yfinance as yf
import pandas as pd

# stock
ticker = "AAPL"

# start and end date obv
start_date = "2024-01-01"
end_date = "2024-12-29"

# yfinance
stock_data = yf.download(ticker, start=start_date, end=end_date)

# IMPORTANT!! customize this part
file_name = r'C:\Users\Dingo\Desktop\egyetem\apple_stock_prices.xlsx'

# saves it to an excel file
stock_data.to_excel(file_name)

