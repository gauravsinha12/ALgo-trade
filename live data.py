# import yfinance as yf
# from datetime import datetime, timedelta
# from time import sleep

# symbol = 'BTC-USD'

# end_time = datetime.now()
# start_time = end_time - timedelta(minutes=5)

# while start_time < end_time:
#     data = yf.download(tickers=symbol, interval='1m', period='1d')
#     ohlc = data.iloc[-1]

#     print(f'Time: {ohlc.name}, Open: {ohlc["Open"]:.2f}, High: {ohlc["High"]:.2f}, Low: {ohlc["Low"]:.2f}, Close: {ohlc["Close"]:.2f}')

#     # Wait for 1 minute before fetching the next data point
#     sleep(62)

#     # Set the start time to the end of the previous 1 minute interval
#     start_time = end_time
#     end_time = datetime.now()

