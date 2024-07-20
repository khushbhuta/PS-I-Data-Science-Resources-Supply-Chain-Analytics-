# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 03:30:47 2024

@author: Khush Bhuta
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

retail = pd.read_csv("C:\\Users\\Khush Bhuta\\Desktop\\python_workspace\\data\\twentyeleven.csv")
retail.info()
retail['InvoiceDate'] = pd.to_datetime(retail['InvoiceDate'])
retail['daysofweek']=retail['InvoiceDate'].dt.dayofweek

retail['daysofweek'].value_counts()
retail['date'] = retail['InvoiceDate'].dt.strftime('%Y-%m-%d')
retail['date'] = pd.to_datetime(retail['date'])


