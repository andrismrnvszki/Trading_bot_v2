from webbrowser import get
import yfinance as yf
import datetime as date
import pandas as pd
import talib


def getData():
    now = date.datetime.today()
    data = yf.download("BTC", period="max")
    return data



df = getData()
print(type(df))
print(df)



data_DF = pd.DataFrame(data)
data_DF.to_csv('Data/BTC-USD_alltime.csv', index=False)
#data_DF.to_excel('Data/BTC-USD_alltime.xls', index=False)
