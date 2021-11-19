# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
least_dif = []
greatest_dif = []

for x in range(1, 12):
    filename = 'forecast_week' + str(x) + '_results.csv'
    filepath = os.path.join('..', 'data', filename)
    temp = pd.read_csv(filepath, index_col='name')
    minval = temp['1week_difference'].idxmin()
    least_dif.append(minval)
    maxval = temp['1week_difference'].idxmax()
    greatest_dif.append(maxval)

print('Smallest Difference Between Observed\n and Forecasted Flow', least_dif)
print('---------------------------------')
print('Largest Difference Between Observed\n and Forecasted Flow', 
      greatest_dif)

