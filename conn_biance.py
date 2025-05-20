from weakref import proxy
import pandas as pd
import ccxt 

exchange=ccxt.binance({
    "enableRateLimit": True,
    "proxies": {
        "http": "127.0.0.1:12334",
        "https": "127.0.0.1:12334"
    }
})
# markets=exchange.load_markets()
# print(markets)
bars=exchange.fetch_ohlcv('BTC/USDT', timeframe='1m', limit=2)
df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp']=pd.to_datetime(df['timestamp'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('Asia/Shanghai')

#打印df指定行数据
print(df)
dfdf.shift(1,axis=1)
print(df)