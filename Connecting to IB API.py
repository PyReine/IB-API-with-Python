import numpy as np
import pandas as pd
from ib_insync import *
ib = IB()

ib.connect('127.0.0.1', 7496, clientId=2)

# IMPORT STOCK DATA, taking Apple for example

code = "AAPL"
timeseries='1 day'
dur='3 M'

contract = Stock(code, 'SMART','USD')
bars = ib.reqHistoricalData(contract, endDateTime='', durationStr=dur,
        barSizeSetting=timeseries, whatToShow='ADJUSTED_LAST', useRTH=True)

df=util.df(bars)

#Save the data to csv file
pathout='/Users/.../History price/'
df.to_csv(pathout+'Historyprice'.csv')

