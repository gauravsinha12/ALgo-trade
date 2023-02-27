import yfinance as yf
import pandas as pd
import ta

# Get BTC data from Yahoo Finance
btc = yf.download('BTC-USD', period='5d', interval='1m')

# Calculate ATR
btc['ATR'] = ta.volatility.average_true_range(btc['High'], btc['Low'], btc['Close'], window=14)

# Calculate stop loss level based on ATR
btc['ATR_stoploss'] = btc['Close'] - (3 * btc['ATR'])

# Calculate buy and sell signals
btc['Signal'] = 0
btc['Signal'][btc['Close'] > btc['ATR_stoploss']] = 1
btc['Signal'][btc['Close'] < btc['ATR_stoploss']] = -1

# Print the last few rows of data
atrr = list(round(btc.tail()['ATR_stoploss']))
close = list(round(btc.tail()['Close']))
print(atrr)
print(close)
