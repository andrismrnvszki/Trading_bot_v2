from webbrowser import get
import yfinance as yf
import datetime as date
import pandas as pd

def getData():
    now = date.datetime.today()
    data = yf.download("BTC", start="2015-07-30", end=now)
    return data



data = getData()
print(data)


data_DF = pd.DataFrame(data)
data_DF.to_csv('ETH-USD_alltime.csv', index=False)
data_DF.to_excel('ETH-USD_alltime.xls', index=False)
