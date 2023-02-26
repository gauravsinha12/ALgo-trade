import yfinance as yf
import ta

# Set the stock symbol and the time interval
symbol = 'BTC-USD'
interval = '1m'

# Fetch historical data
data = yf.download(tickers=symbol, interval=interval, period='7d')

# Calculate ATR
atr = ta.volatility.AverageTrueRange(data['High'], data['Low'], data['Close'], window=14)

# Calculate MACD
macd = ta.trend.MACD(data['Close']).macd()

# Calculate the signal line
signal = ta.trend.MACD(data['Close']).macd_signal()

# Generate buy/sell signals
signals = []
prev_signal = 0
for i in range(len(macd)):
    if macd[i] > signal[i] and prev_signal <= 0 and data['Close'][i] > data['Open'][i] and data['Close'][i] > (data['Close'][i-1] + atr[i-1]):
        signals.append(1) # Buy signal
        prev_signal = 1
    elif macd[i] < signal[i] and prev_signal >= 0 and data['Close'][i] < data['Open'][i] and data['Close'][i] < (data['Close'][i-1] - atr[i-1]):
        signals.append(-1) # Sell signal
        prev_signal = -1
    else:
        signals.append(0) # No signal

# Print the signals
print(signals)
