import yfinance as yf
import ta
import time

while True:
    # get bitcoin data
    btc = yf.download('BTC-USD', interval='1m', period='1d')
    
    # calculate MACD and signal line
    macd = ta.trend.MACD(btc['Close'])
    signal = ta.trend.MACD(btc['Close']).macd_signal()
    
    # calculate difference between MACD and signal line
    macd_diff = macd.macd() - signal
    
    # print MACD and signal line values and the difference
    print('MACD:', macd.macd()[-1])
    print('Signal Line:', signal[-1])
    print('MACD - Signal Line:', macd_diff[-1])
    
    # wait for 1 minute
    time.sleep(60)
