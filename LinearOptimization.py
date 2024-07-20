from pulp import *
# product1 = 25
# product2 = 35
# model = LpProblem('Pillows',LpMaximize)
# X1 = LpVariable('X1',0,None,'Integer')
# X2 = LpVariable('X2',0,None,'Integer')
# model += X1*product1 + X2*product2
# model += X1*0.3 + X2*0.5 <= 20
# model += X1*0.5 + X2*0.5 <= 35
# model.solve()

# X1.varValue
# X2.varValue

## Problem 2
# product1 = 33
# product2 = 40
# product3 = 34

# model = LpProblem('MorePillows',LpMaximize)
# X1 = LpVariable('X1',0,None,'Integer')
# X2 = LpVariable('X2',0,None,'Integer')
# X3 = LpVariable('X3',0,None,'Integer')

# model += X1*product1 + X2*product2 + X3*product3

# model += 0.4*X1 + 0.7*X2 + 0.4*X3 <= 40
# model += 0.2*X1 + 0.5*X2 + 0.6*X3 <= 40
# model += 0.3*X1 + 0.3*X2 + 0.2*X3 <= 40

# model.solve()

# X1.varValue
# X2.varValue
# X3.varValue

## TRANSPORTATION PROBLEM

from pulp import *

model= LpProblem('shipping',LpMinimize)

customers=['Australia','Sweeden','Brazil']
factory= ['Factory1','Factory2']
products= ['Chair','Table','Beds']

keys= [(f,p,c) for f in factory for p in products for c in customers]

var= LpVariable.dicts('shipment', keys,0,None,cat='Integer')

costs_value= [50,80,50,
        60,90,60,
        70,90,70,
        80,50,80,
        90,60,90,
        90,70,90]

costs= dict(zip(keys,costs_value))


demand_keys= [(p,c)for c in customers
              for p in products]
demand_values=[90,65,700,
               120,450,40,
               78,52,500]
demand= dict(zip(demand_keys,demand_values))


model+= lpSum(var[(f,p,c)]*costs[(f,p,c)]
   for f in factory for p in products for c in customers )

model += lpSum(var[('Factory1',p,c)]
               for p in products for c in customers)<= 1500
model += lpSum(var[('Factory2',p,c)]
               for p in products for c in customers)<= 2500

for c in customers:
    for p in products:
        model += var[('Factory1',p,c)]+var[('Factory2',p,c)]>=demand[(p,c)]

model.solve()

for i in var: 
    print('{} shipping {}'.format(i,var[i].varValue))
