import yfinance as yf
from datetime import datetime, timedelta

def fetch_prices(tickers, years=5):
    end = datetime.now()
    start = end - timedelta(days=years * 365)
    return yf.download(list(tickers), start=start, end=end)['Adj Close']
