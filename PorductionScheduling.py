# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from pulp import *
# param = pd.read_excel("C:\\Users\\Khush Bhuta\\Desktop\\python_workspace\\data\\Production_scheduling (1).xlsx")
# param = param.rename(columns={'Unnamed: 0':'period'})
# param['t'] = range(1,13)
# param = param.set_index('t')

# inventory = LpVariable.dicts('inv',[0,1,2,3,4,5,6,7,8,9,10,11,12],0,None,'Integer')
# inventory[0] = 200

# production = LpVariable.dicts('Prod',[0,1,2,3,4,5,6,7,8,9,10,11,12],0,None,'Integer')
# binary = inventory = LpVariable.dicts('inv',[0,1,2,3,4,5,6,7,8,9,10,11,12],0,None,'Binary')

# time = [1,2,3,4,5,6,7,8,9,10,11,12]

# model = LpProblem('Production',LpMinimize)
# model += lpSum([inventory[t]* param.loc[t,'storage cost'] 
#                 + production[t]*param.loc[t,'var']
#                 + binary[t]*param.loc[t,'fixed cost'] for t in time])

# for t in time:
#     model += production[t] - inventory[t] + inventory[t-1] >= param.loc[t,'demand']
#     model += production[t] <= binary[t]*param.loc[t,'Capacity']
    
# model.solve()

# for i in production:
#     print(production[i],production[i].varValue)



import pandas as pd
from pulp import *

param = pd.read_excel("C:\\Users\\Khush Bhuta\\Desktop\\python_workspace\\data\\assignment_ps.xlsx")

param = param.rename(columns = {'Unnamed: 0':'Period'})
param['t'] = range(1,13)
param = param.set_index('t')
param

inventory = LpVariable.dicts('inv',[0,1,2,3,4,5,6,7,8,9,10,11,12],0,None,'Integer')
inventory[0] = 0

production = LpVariable.dicts('Prod',[0,1,2,3,4,5,6,7,8,9,10,11,12],0,None,'Integer')
binary = LpVariable.dicts('binary',[0,1,2,3,4,5,6,7,8,9,10,11,12],0,None,'Binary')

time = [1,2,3,4,5,6,7,8,9,10,11,12]
t = [1,2,3,4,5,6,7,8,9,10,11,12]
model = LpProblem('Production',LpMinimize)

model += lpSum(inventory[t]*param.loc[t,'storage cost'] 
               + production[t]* param.loc[t,'var']
               + binary[t]* param.loc[t,'fixed cost'])
for t in time:
    model+=production[t]-inventory[t]+inventory[t-1] >= param.loc[t,'demand']
    model+=production[t]<=binary[t]*param.loc[t,'Capacity']

model.solve()

for v in model.variables():
    print(v,v.varValue)
optimization_data = pd.DataFrame({'demand': param['demand'],
                                  'production': [production[i].varValue for i in production],
                                  'inventory': [inventory[i].varValue for i in range(1,13)],
                                  'opening': [binary[i].varValue for i in binary]
                                  })
