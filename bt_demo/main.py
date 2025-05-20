import backtrader as bt
import pandas as pd
import ccxt
import MyStrategy as ms
if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.broker.setcash(100001.0)
    cerebro.addstrategy(ms.MyStrategy)


    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    #加载数据
    exchange=ccxt.binance({
        "enableRateLimit": True,
        "proxies": {
        "http": "127.0.0.1:12334",
        "https": "127.0.0.1:12334"
        }
    })
    # markets=exchange.load_markets()
    # print(markets)
    bars=exchange.fetch_ohlcv('BTC/USDT', timeframe='1d', limit=100)
    df = pd.DataFrame(bars, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    df['Date'] = pd.to_datetime(df['Date'], unit='ms')
    df['Adj Close'] = df['Close']
    data = bt.feeds.PandasData(dataname=df, datetime='Date')
    cerebro.adddata(data)
    cerebro.run()
    
    # print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    print('Final Portfolio Value: {:.2f}'.format(cerebro.broker.getvalue()))