"""
Root Module for the alphavantage python accessor
"""

import logging
import os

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
LOGGER = logging.getLogger(__name__)

API_URI="http://www.alphavantage.co/query"

class AlphaVantageException(Exception):
    pass

API_KEY = os.environ.get('AV_API_KEY', None)
if API_KEY is None:
    LOGGER.warning("Environment Variable AV_API_KEY not set")

from timeseries import *
