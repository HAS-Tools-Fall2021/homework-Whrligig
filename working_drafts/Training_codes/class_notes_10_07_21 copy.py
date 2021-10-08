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
# %%
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%
oct_median = np.empty(31)

for i in range(31):
    day = i + 1
    data_loop = data[(data['year'] >= 2016) & (data['month'] == 10) & (data['day'] == day)]
    oct_median[i] = np.median(data_loop['flow'])


# Example of creating a function
def day_median(days_in_month, month, startyear, data):
    month_median = np.zeros(days_in_month)
    for i in range(days_in_month):
        day = i + 1
        data_loop = data[(data['year'] >= startyear) & (data['month'] == month)
                         & (data['day'] == day)]
        month_median[i] = np.median(data_loop['flow'])
    return month_median


day_median(31, 10, 2016, data)

# %%
