import numpy as np
import talib as tb
import yfinance as yf
import pandas as pd
from datetime import datetime
import websocket, json, pprint
#import config

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
def on_open(ws):
    print('Cpened connection')

def on_close(ws):
    print('Closed connection')

def on_message(ws, message):
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']

    is_candle_closed = candle['x']
    close = candle['c']

ws = websocket.WebSocketApp(SOCKET, on_close=on_close, on_message=on_message)
ws.run_forever()