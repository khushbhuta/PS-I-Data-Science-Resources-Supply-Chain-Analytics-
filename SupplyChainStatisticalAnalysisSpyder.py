# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 21:20:26 2024

@author: Khush Bhuta
"""

import numpy as np
sales = np.array([5,8,10,20,100,2,65,18,32,25,200,9,15])

def outlier(x):
    first_quartile = np.percentile(sales,25)
    third_quartile = np.percentile(sales,75)
    iqr = third_quartile-first_quartile
    upper_threshold = third_quartile + (1.5*iqr)
    lower_threshold = first_quartile - (1.5*iqr)
    
    outliers = {'upper outliers':x[x>upper_threshold],
                'lower outliers':x[x<lower_threshold]}
    return outliers    
outlier(sales)