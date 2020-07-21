# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
import pandas as pd
import json
from binance.client import Client
import time
      



g_api_key = ''
g_secret_key = ''
client = Client(g_api_key, g_secret_key)
info = client.get_symbol_info('BTCUSDT')
while True:
    print("Executando")
    depth = client.get_order_book(symbol='BTCUSDT', limit=10)
    asks = pd.DataFrame(depth['asks'], columns=['C Preço do Bitcoin', 'C Quantidade de Bitcoin'])
    asks.insert(2, 'C Valor da Ordem', None)
    for i in asks.index:
        asks.loc[i, 'C Valor da Ordem'] = float(asks.loc[i, 'C Preço do Bitcoin']) * float(asks.loc[i, 'C Quantidade de Bitcoin'])
    
    bids = pd.DataFrame(depth['bids'], columns=['V Preço do Bitcoin', 'V Quantidade de Bitcoin'])
    asks.insert(3, 'VENDA', ' ')
    asks.insert(4, 'V Preço do Bitcoin', bids.loc[:, 'V Preço do Bitcoin'])
    asks.insert(5, 'V Quantidade de Bitcoin', bids.loc[:, 'V Quantidade de Bitcoin'])
    for i in bids.index:
        asks.loc[i, 'V Valor da Ordem'] = float(bids.loc[i, 'V Preço do Bitcoin']) * float(bids.loc[i, 'V Quantidade de Bitcoin'])
    asks.insert(0, 'COMPRA', ' ')
    asks.update(asks)
    for i in asks.index:
        print(asks.loc[i, :])
        trades = client.get_recent_trades(symbol='BNBBTC')
        
    
        
#request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

#result = request_client.get_ticker_price_change_statistics()
#print(str(result[0]))
# result = request_client.get_ticker_price_change_statistics(symbol="BTCUSDT")

#for ticker in result:
    #print(ticker.askPrice)
    #obj = []
    #'askPrice', 'bidPrice', 'closeTime', 'count', 'firstId', 'highPrice', 'json_parse', 'lastId', 'lastPrice', 'lastQty', 'lowPrice', 'openPrice', 'openTime', 'priceChange', 'priceChangePercent', 'quoteVolume', 'symbol', 'volume', 'weightedAvgPrice'
    