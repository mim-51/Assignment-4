import numpy as np
from scipy.optimize import linear_sum_assignment
#Profit matrix
profit=np.array([
    [16,10,14,11],
    [14,11,15,15],
    [15,15,13,12],
    [13,12,14,15]
])
#For maximization
cost=profit.max()-profit
#Solve using Hungarian algorithm
row_ind,col_ind=linear_sum_assignment(cost)
#Output result
total_profit=profit[row_ind,col_ind].sum()
print('Optimal Assignment:')
for i in range(len(row_ind)):
    print(f'Salesman {chr(65+row_ind[i])} \u2192 City {col_ind[i]+1} (profit:{profit[row_ind[i]][col_ind[i]]})')

print('Total maximum profit',total_profit)
