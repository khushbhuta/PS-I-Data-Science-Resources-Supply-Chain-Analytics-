# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:24:45 2024

@author: Khush Bhuta
"""

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
retail = pd.read_csv('C:/Users/Khush Bhuta/Desktop/python_workspace/data/online_retail2.csv')

retail.head()
retail = retail.drop_duplicates()
retail = retail.dropna(axis=0,how='any')
retail.info()
retail['InvoiceDate'] = pd.to_datetime(retail['InvoiceDate'])
retail['InvoiceDate'].dt.day
retail['InvoiceDate'].dt.strftime('%W %Y')
diff = retail['InvoiceDate'].max() - retail['InvoiceDate'].min()
diff
retail.columns
# RECENCY OF PURCHASE
max_date = retail.InvoiceDate.max()
last_purchase_date = retail.groupby('Customer ID',as_index = False)['InvoiceDate'].max()
last_purchase_date['Recency'] = max_date - last_purchase_date['InvoiceDate']
last_purchase_date['Recency'].describe()
last_purchase_date['Recency_days'] = last_purchase_date['Recency'].dt.days
last_purchase_date['Recency_days']
plt.hist(last_purchase_date['Recency_days'])

# modelling

import numpy as np
customers = np.unique(retail['Customer ID'])
len(customers)
retail['date'] = retail['InvoiceDate'].dt.strftime('%Y-%m-%d')
retail['date']
customer_grouped = retail.groupby(['Customer ID','date'],as_index=False).count()[['Customer ID','date']]
customer_grouped

inter_data = pd.DataFrame()
for customer in customers:
    c_d = customer_grouped[customer_grouped['Customer ID']==customer].copy()
    c_d['previous_date'] = c_d['date'].shift(1)
    inter_data = pd.concat([inter_data,c_d],axis=0)

inter_data.reset_index(drop=True,inplace=True)
print(inter_data)

inter_data.info()
inter_data['date'] = pd.to_datetime(inter_data['date'])
inter_data['previous_date'] = pd.to_datetime(inter_data['previous_date'])

inter_data['duration'] = inter_data['date'] - inter_data['previous_date']
inter_data['duration'] = inter_data['duration'].dt.days
inter_arrival = inter_data.groupby('Customer ID')['duration'].mean()
inter_arrival

# RESAMPLING

import pandas as pd
stocks = pd.read_csv('C:/Users/Khush Bhuta/Desktop/python_workspace/data/stocks.csv',index_col = 'Date', parse_dates=True)
stocks['2009':'2011'].plot()
monthly_series_mean = stocks.resample('M').mean()
yearly_series_mean = stocks.resample('Y').mean()
weekly_series_mean = stocks.resample('W').mean()
monthly_series_mean.plot()
weekly_series_mean.plot()
yearly_series_mean.plot()
weekly_series_mean
quarter_series_sum = stocks.resample('W').sum()

# ROLLING TIME SERIES, MOVING AVERAGES
MSFT = stocks[['MSFT']]
MSFT['Rolling_Weekly'] = MSFT.rolling(window = 7).mean()
MSFT['Rolling_Monthly'] = MSFT['MSFT'].rolling(window=30).mean()
MSFT['Aug-2011':'Dec-2011'].plot()
