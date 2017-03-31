"""
Houses classes to access the Time Series on AlphaVantage
"""
import logging
import pandas as pd
import requests

from alphavantage import API_KEY, API_URI
from alphavantage import AlphaVantageException

LOGGER = logging.getLogger(__name__)

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

    def __init__(self, symbol, api_key = None):
        self.api_key = api_key if api_key else API_KEY
        self._symbol = symbol

    def intraday(self, interval, outputsize="compact"):
        FUNCTION_INTRADAY="TIME_SERIES_INTRADAY"
        data = {
            "function"   : FUNCTION_INTRADAY,
            "symbol"     : self._symbol,
            "interval"   : interval,
            "outputsize" : outputsize,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        resp.raise_for_status()
        if "Error Message" in resp.json().keys():
            raise AlphaVantageException("%s" % resp.json()['Error Message'])
        LOGGER.debug("Got response with keys: %s" % str(resp.json().keys()))
        df = pd.DataFrame.from_dict(resp.json()['Time Series ({})'.format(interval)],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        df[df.columns] = df[df.columns].apply(pd.to_numeric)
        df.name = self._symbol
        return df

    def daily(self, outputsize="compact"):
        FUNCTION_DAILY="TIME_SERIES_DAILY"
        data = {
            "function"   : FUNCTION_DAILY,
            "symbol"     : self._symbol,
            "outputsize" : outputsize,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        resp.raise_for_status()
        if "Error Message" in resp.json().keys():
            raise AlphaVantageException("%s" % resp.json()['Error Message'])
        LOGGER.debug("Got response with keys: %s" % str(resp.json().keys()))
        df = pd.DataFrame.from_dict(resp.json()['Time Series (Daily)'],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        df[df.columns] = df[df.columns].apply(pd.to_numeric)
        df.name = self._symbol
        return df

    def weekly(self):
        FUNCTION_WEEKLY="TIME_SERIES_WEEKLY"
        data = {
            "function"   : FUNCTION_WEEKLY,
            "symbol"     : self._symbol,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        resp.raise_for_status()
        if "Error Message" in resp.json().keys():
            raise AlphaVantageException("%s" % resp.json()['Error Message'])
        LOGGER.debug("Got response with keys: %s" % str(resp.json().keys()))
        df = pd.DataFrame.from_dict(resp.json()['Weekly Time Series'],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        df[df.columns] = df[df.columns].apply(pd.to_numeric)
        df.name = self._symbol
        return df

    
    def monthly(self):
        FUNCTION_MONTHLY="TIME_SERIES_MONTHLY"
        data = {
            "function"   : FUNCTION_MONTHLY,
            "symbol"     : self._symbol,
            "apikey"     : self.api_key
        }
        resp = requests.get(API_URI, params=data)
        resp.raise_for_status()
        if "Error Message" in resp.json().keys():
            raise AlphaVantageException("%s" % resp.json()['Error Message'])
        LOGGER.debug("Got response with keys: %s" % str(resp.json().keys()))
        df = pd.DataFrame.from_dict(resp.json()['Monthly Time Series'],
                    orient='index')
        df.index = pd.to_datetime(df.index)
        df = df.rename(columns={'5. volume': 'volume',
                                '4. close' : 'close',
                                '2. high'  : 'high',
                                '1. open'  : 'open',
                                '3. low'   : 'low'})
        df[df.columns] = df[df.columns].apply(pd.to_numeric)
        df.name = self._symbol
        return df
