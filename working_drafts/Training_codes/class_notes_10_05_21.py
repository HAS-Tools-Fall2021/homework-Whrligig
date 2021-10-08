# %%

import os
import numpy as np
import pandas as pd

filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

oct_avgs = np.zeros(31)

for i in range(0, 31):
    day = i + 1
    data_loop = data[(data['day'] == day) & (data['month'] == 10)]
    oct_avgs[i] = np.mean(data_loop['flow'])

print(oct_avgs)

# Class Solution
oct_mean = np.zeros(31)
for d in range(31):
    daytemp = d + 1
    tempdata = data[(data['month'] == 10) & (data['day'] == daytemp)]
    oct_mean[d] = np.mean(tempdata['flow'])
    print('Iteration', d, 'Day=', daytemp, 'Flow=', oct_mean[d])


# Example of creating a function
def day_mean(month, days_in_month, data):
    month_mean = np.zeros(days_in_month)
    for d in range(days_in_month):
        daytemp = d+1
        tempdata = data[(data['month'] == month) & (data['day'] == daytemp)]
        month_mean[d] = np.mean(tempdata['flow'])
        # print('Iteration', d, 'Day=', daytemp, 'Flow=', oct_mean[d])

    return month_mean


day_mean(1, 28, data)
