# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:22:33 2020

@author: kathy
"""

"""Part II ­ Stock Data - I CAN'T FIGURE IT OUT BUT HERE'S AN ALTERNATIVE!"""

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

def retrieve_nasdaq_prices(ticker, start_date, end_date):
    url = f'https://www.nasdaq.com/api/v1/historical/{ticker}/stocks/{start_date}/{end_date}'
    df = pd.read_csv(str(url))

    print(df)

ticker = 'AAPL'
raw_start = datetime.datetime.today() - relativedelta(months = 1)
start_date = str(raw_start.strftime('%Y-%m-%d'))
end_date = str(datetime.datetime.today().strftime('%Y-%m-%d'))


retrieve_nasdaq_prices('AAPL', start_date, end_date)