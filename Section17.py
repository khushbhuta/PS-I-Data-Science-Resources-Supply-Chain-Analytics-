import pandas as pd
import numpy as np
import array
import inventorize as inv
skus = pd.read_csv("C:\\Users\\Khush Bhuta\\Desktop\\python_workspace\\data\\sku_distributions1.csv")
skus.head()
skus.columns
apple_juice = skus[['apple_juice']]
mean_apple_juice = apple_juice.mean()
std_apple_juice = apple_juice.std()

leadtime=7

inv.sim_min_Q_normal(apple_juice,mean_apple_juice,std_apple_juice,leadtime=7,service_level=0.8,Quantity=100)