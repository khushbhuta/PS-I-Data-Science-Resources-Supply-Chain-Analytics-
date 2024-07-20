# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:04:10 2024

@author: Khush Bhuta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/twentyeleven.csv')
data.head()
data.columns
data = data.drop_duplicates()
data.info()
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['week'] = data.InvoiceDate.dt.isocalendar().week
data['dayofweek'] = data.InvoiceDate.dt.dayofweek
data['month'] = data.InvoiceDate.dt.month
data[['week','month','dayofweek','InvoiceDate']]

data['Month-Year'] = data['InvoiceDate'].dt.strftime('%B-%Y')

# Last purchase date per customer
data['date'] = data['InvoiceDate'].dt.strftime('%Y-%m-%d')
data['date'] = pd.to_datetime(data['date'])
max_date = data['date'].max()
customer_last = data.groupby('Customer ID').agg(last_purchase_date = ('date','max'))

#recency per customer
customer_last['recency'] = max_date - customer_last['last_purchase_date']
customer_last['recency'] = customer_last['recency'].astype('string').str.replace('days 00:00:00.00000000',' ')
plt.hist(customer_last['recency'])
data.columns

#2 week and 1 week SMA on sales data
data[['sales','InvoiceDate']].head()
sales_per_day = data.groupby('date').agg(total_sales = ('Quantity','sum'))
sales_per_day['moving_7'] = sales_per_day.rolling(window = 7).mean()
sales_per_day['moving_14'] = sales_per_day.total_sales.rolling(window = 14).mean()
sales_per_day['date']
sales_per_day['Aug-2011-01':'Aug-2011-31'].plot()


sales_resample = sales_per_day.resample('W').sum()
