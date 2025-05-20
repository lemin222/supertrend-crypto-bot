import ccxt
import pandas as pd


exchange=ccxt.binance({
        "enableRateLimit": True,
        "proxies": {
        "http": "127.0.0.1:12334",
        "https": "127.0.0.1:12334"
        }
    })
    # markets=exchange.load_markets()
    # print(markets)
bars=exchange.fetch_ohlcv('BTC/USDT', timeframe='1d', limit=2)
df = pd.DataFrame(bars, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
print("---------")
print(df['Date'])
df['Date'] = pd.to_datetime(df['Date'], unit='ms')
print("---------")
print(df['Date'])
