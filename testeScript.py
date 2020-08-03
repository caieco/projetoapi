# -*- coding: utf-8 -*-

#ASK = Compra (verde)
#BID = Venda (vermelho)
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import requests
import json


baseBinance = 'https://api.binance.com'
endpointBinance = '/api/v3/depth'
payload = {'symbol': 'BTCUSDT', 'limit': '5'}

r = requests.get(baseBinance + endpointBinance, params=payload)
resposta1 = json.loads(r.text)
volumeBTCBids = 0
for bid in resposta1['bids']:
    volumeBTCBids += float(bid[1])
    
volumeBTCAsks = 0
for ask in resposta1['asks']:
    volumeBTCAsks += float(ask[1])
# lastBid = resposta1['bids'][4]
# lastAsk = resposta1['asks'][4]

endpointBinance = '/api/v3/ticker/24hr'
payload = {'symbol': 'BTCUSDT'}   

r = requests.get(baseBinance + endpointBinance, params=payload)
resposta = json.loads(r.text)
volumeDolar = resposta['quoteVolume']
volumeBTC = resposta['volume']


