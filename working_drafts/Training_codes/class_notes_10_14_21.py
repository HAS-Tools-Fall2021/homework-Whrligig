# %%
import os
import pandas as pd
import matplotlib.pyplot as plt

# %%
filename = 'streamflow_week7.txt'
filepath = os.path.join('../../working_drafts/data', filename)
print(os.getcwd())
print(filepath)

# %%
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime']
                     )

data_time = data.set_index('datetime')

# %%
oct_flow = data_time[data_time.index.month == 10]
oct_median = data_time.groupby(data_time.index.day).median()
# could also do the line above as oct_median = data.groupby('day').median()
oct_min = data_time.groupby(data_time.index.day).min()
oct_max = data_time.groupby(data_time.index.day).max()

fig, ax = plt.subplots()
ax.plot(oct_median['flow'], color='r')
ax.fill_between(oct_median.index, oct_min['flow'], oct_max['flow'], alpha=0.7)
ax.set(yscale='log')
