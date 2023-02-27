import yfinance as yf
import ta
import time
import pandas as pd

def get_live_data():
    btc = yf.download('KPITTECH', period='1d', interval='1m')
    return btc

def calculate_indicators(df):

    macd = ta.trend.MACD(df['Close'], window_slow=26, window_fast=12, window_sign=9)
    
    atr = ta.volatility.AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14)
    multiplier = 2
    atr_stoploss = df['Close'] - (multiplier * atr.average_true_range())
    
    indicators = df[['Close']].copy()
    indicators['MACD'] = macd.macd_diff()
    indicators['ATR Stoploss'] = atr_stoploss
    
    return indicators

def make_decision(indicators):
    last_row = indicators.iloc[-1]
    if last_row['MACD'] > 0 and last_row['MACD'] > pd.Series(last_row['MACD']).shift(1).all() and last_row['Close'] > last_row['ATR Stoploss']:
        return 'Buy'
    elif last_row['MACD'] < 0 and last_row['MACD'] < pd.Series(last_row['MACD']).shift(1).all() and last_row['Close'] < last_row['ATR Stoploss']:
        return 'Sell'
    else:
        return 'Hold'

while True:
    data = get_live_data()
    print(data.tail(1))
    indicators = calculate_indicators(data)
    decision = make_decision(indicators)
    print('Current decision:', decision)
    time.sleep(60) 
