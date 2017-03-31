## AlphaVantage library

This package wraps access to the alpha vantage library

#### Setup
Be sure to set the environment variable <b>AV_API_KEY</b> to your API KEY
You can get this key from [http://www.alphavantage.co](http://www.alphavantage.co)

```python

from alphavantage.timeseries import TimeSeries

msft = TimeSeries("MSFT")

df = msft.daily()

```
