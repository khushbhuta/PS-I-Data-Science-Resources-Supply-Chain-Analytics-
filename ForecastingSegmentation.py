# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 02:38:37 2024

@author: Khush Bhuta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

retail = pd.read_csv('retail_clean (1).csv')
retail = retail.drop(columns='Unnamed: 0')
retail.head()

retail['InvoiceDate'] = pd.to_datetime(retail['InvoiceDate'])
retail['daysofweek'] = retail['InvoiceDate'].dt.dayofweek
retail['daysofweek'].value_counts
retail['date'] = retail['InvoiceDate'].dt.strftime('%Y-%m-%d')
retail['date'] = pd.to_datetime(retail['date'])

retail_grouped = retail.groupby(['Description','date']).agg(total_sales = ('Quantity','sum')).reset_index()
cv_data = retail_grouped.groupby('Description').agg(average = ('total_sales','mean'),
                                                   standard_dev = ('total_sales','std')).reset_index()
cv_data['cv_squared'] = (cv_data['standard_dev']/cv_data['average'])**2
product_by_date = retail.groupby(['Description','date']).agg(count=('Description','count')).reset_index()

cv_data

skus = product_by_date.Description.unique()
empty_dataframe = pd.DataFrame()

for sku in skus:
    a = product_by_date[product_by_date.Description == sku]
    a['previous_date'] = a['date'].shift(1)
    empty_dataframe = pd.concat([empty_dataframe,a],axis=0)
    
empty_dataframe['Duration'] = empty_dataframe['date'] - empty_dataframe['previous_date']

empty_dataframe['Duration'] = empty_dataframe['Duration'].astype('string').str.replace('days','') 
empty_dataframe['Duration'] = pd.to_numeric(empty_dataframe['Duration'],errors='coerce')

ADI = empty_dataframe.groupby('Description').agg(ADI = ('Duration','mean')).reset_index()
adi_cv = pd.merge(ADI,cv_data)

def category(dataframe):
    a=0
    if((dataframe['ADI']<=1.34) & (dataframe['cv_squared']<=0.49)):
        a = 'smooth'
    if((dataframe['ADI']<1.34) & (dataframe['cv_squared']>0.49)):
        a = 'erratic'
    if((dataframe['ADI']>=1.34) & (dataframe['cv_squared']>=0.49)):
        a = 'lumpy'
    if((dataframe['ADI']>1.34) & (dataframe['cv_squared']<0.49)):
        a = 'intermittent'
    return a

adi_cv['category'] = adi_cv.apply(category, axis=1) 
adi_cv[adi_cv.category == 0]

adi_cv.category.value_counts()
