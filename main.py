import requests
from bs4 import BeautifulSoup


def get_stock_price(stock_symbol):
    # URL to fetch stock data from Yahoo Finance
    url = f'https://finance.yahoo.com/quote/{stock_symbol}'

    # Send a GET request to fetch the page content
    response = requests.get(url)

    # If the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        try:
            # Find the 'fin-streamer' element with the appropriate class and attribute
            price_element = soup.find('fin-streamer', {'data-symbol': stock_symbol, 'data-testid': 'qsp-price'})

            # Extract the price from the 'data-value' attribute
            price = price_element['data-value']

            print(f"The current price of {stock_symbol} is {price}")
        except AttributeError:
            print(f"Could not find the price for {stock_symbol}")
    else:
        print(f"Failed to retrieve data for {stock_symbol}. Status code: {response.status_code}")


# Example usage
get_stock_price('AAPL')
get_stock_price('GOOG')
get_stock_price('AMZN')
