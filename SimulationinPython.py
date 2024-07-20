# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 18:59:31 2024

@author: Khush Bhuta
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lambda1 = 1
mean_service = 1
sd = 0.2

arrival_time = np.random.exponential(1,400).cumsum()
service_time = np.random.normal(1,0.2,400)
def waiting_mean(arrival_time,service_time):
    waiting_time = []
    leaving_time = []
    
    waiting_time.append(0)
    leaving_time.append(arrival_time[0]+service_time[0]+waiting_time[0])
    for i in range(1,len(arrival_time)):
        waiting_time.append(max(0,(leaving_time[i-1]-arrival_time[i])))
        leaving_time.append(arrival_time[i]+waiting_time[i]+service_time[i])
    
    mean_waiting = np.mean(waiting_time)
    return mean_waiting

waiting_mean(arrival_time,service_time)

average_Sim = []
for i in range(0,1000):
    arrival_time = np.random.exponential(1,400).cumsum()
    service_time = np.random.normal(1,0.2,400)
    waiting_time = waiting_mean(arrival_time,service_time)
    average_Sim.append(waiting_time)
    
np.mean(average_Sim)
np.median(average_Sim)
plt.hist(average_Sim)
