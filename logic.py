# import yfinance as yf
# import ta
# import pandas as pd

# def get_atr_stoploss(symbol):
#     btc = yf.download('BTC-USD', period='5d', interval='1m')

#     # Calculate ATR
#     btc['ATR'] = ta.volatility.average_true_range(btc['High'], btc['Low'], btc['Close'], window=14)

#     # Calculate stop loss level based on ATR
#     btc['ATR_stoploss'] = btc['Close'] - (3 * btc['ATR'])

#     # Calculate buy and sell signals
#     btc['Signal'] = 0
#     btc['Signal'][btc['Close'] > btc['ATR_stoploss']] = 1
#     btc['Signal'][btc['Close'] < btc['ATR_stoploss']] = -1

#     # Print the last few rows of data
#     print(btc.tail())

# def get_macd(symbol):
#     # Get the data from Yahoo Finance
#     data = yf.download(symbol, period='7d', interval='1m')

#     # Calculate the MACD
#     macd = ta.trend.MACD(data['Close']).macd()

#     # Print the MACD data
#     print("MACD Data for {}:".format(symbol))
#     print(macd)

# # Example usage
# symbol = 'BTC-USD'
# get_atr_stoploss(symbol)
# get_macd(symbol)

import yfinance as yf
import time
import ta

# Define function to get ATR stoploss
def get_atr_stoploss(symbol, interval='1d', atr_length=14, atr_multiplier=2):
    # Get historical price data
    df = yf.download(symbol, interval=interval)
    
    # Calculate ATR
    atr = ta.average_true_range(df['High'], df['Low'], df['Close'], window=atr_length)
    
    # Calculate ATR stoploss
    atr_stoploss = df['Close'] - (atr_multiplier * atr.values)
    
    # Return ATR stoploss and closing price
    return atr_stoploss[-1], df['Close'][-1]


# Define function to get MACD
def get_macd(df):
    macd = ta.trend.MACD(df['Close']).macd()
    return macd

# Get BTC data
btc = yf.download('BTC-USD', period='1d', interval='1m')

# Continuously print closing price and ATR stoploss every minute
while True:
    latest_data = btc.tail(1)
    atr_stoploss = get_atr_stoploss(btc)
    macd = get_macd(btc)
    print("Closing Price:", latest_data['Close'].iloc[0])
    print("ATR Stoploss:", atr_stoploss.iloc[-1])
    print("MACD:", macd.iloc[-1])
    print("-----------------------------")
    time.sleep(60)
