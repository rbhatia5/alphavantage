"""
Houses classes to access the Time Series on AlphaVantage
"""

import pandas as pd
import requests

from alphavantage import API_KEY, API_URI


INTRADAY_INTERVAL_1MIN  = "1min"
INTRADAY_INTERVAL_5MIN  = "5min"
INTRADAY_INTERVAL_15MIN = "15min"
INTRADAY_INTERVAL_30MIN = "30min"
INTRADAY_INTERVAL_60MIN = "60min"

class Intraday():
    INTERVAL_1MIN  = "1min"
    INTERVAL_5MIN  = "5min"
    INTERVAL_15MIN = "15min"
    INTERVAL_30MIN = "30min"
    INTERVAL_60MIN = "60min"
    OUTPUTSIZE_COMPACT = "compact"
    OUTPUTSIZE_FULL    = "full"

class Daily():
    OUTPUTSIZE_COMPACT = "compact"
    OUTPUTSIZE_FULL    = "full"

class TimeSeries():

    def __init__(self, api_key = None):
        self.api_key = api_key if api_key else API_KEY

    def intraday(self, symbol, interval, outputsize="compact"):
        FUNCTION_INTRADAY="TIME_SERIES_INTRADAY"
        data = {
            "function"   : FUNCTION_INTRADAY,
            "symbol"     : symbol,
            "interval"   : interval,
            "outputsize" : outputsize,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        df = pd.DataFrame.from_dict(resp.json()['Time Series ({})'.format(interval)],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        return df

    def daily(self, symbol, outputsize="compact"):
        FUNCTION_DAILY="TIME_SERIES_DAILY"
        data = {
            "function"   : FUNCTION_DAILY,
            "symbol"     : symbol,
            "outputsize" : outputsize,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        df = pd.DataFrame.from_dict(resp.json()['Time Series (Daily)'],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        return df

    def weekly(self, symbol):
        FUNCTION_WEEKLY="TIME_SERIES_WEEKLY"
        data = {
            "function"   : FUNCTION_WEEKLY,
            "symbol"     : symbol,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        df = pd.DataFrame.from_dict(resp.json()['Weekly Time Series'],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        return df

    
    def monthly(self, symbol):
        FUNCTION_MONTHLY="TIME_SERIES_MONTHLY"
        data = {
            "function"   : FUNCTION_MONTHLY,
            "symbol"     : symbol,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        df = pd.DataFrame.from_dict(resp.json()['Monthly Time Series'],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        return df
