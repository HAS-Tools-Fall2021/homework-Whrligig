# %%
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# %%
# Add in streamflow data
filename = 'streamflow_week15.txt'
filepath = os.path.join(filename)
print(os.getcwd())
print(filepath)

flow_data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime']
                     )

# %%
# Create plot of streamflow behavior during last forecast period
date_format = mdates.DateFormatter("%m/%d")
fig, ax = plt.subplots()
ax.plot(flow_data['flow'], label='Daily Flow', marker='o',
        color='lightgray',
        markerfacecolor='steelblue',
        markeredgecolor='steelblue')
ax.set(title="Observed Flow for Week 11/28/21 - 12/04/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 11, 21), datetime.date(2021, 11, 27)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()
fig.savefig('Wk14_Obs.png', dpi=300, bbox_inches='tight')

# %%
# Print flow data for last week
print('Flow during the last forecast period:')
last_week = flow_data[['flow']].tail(7)
print(last_week)
print('Avg flow for last week was:', last_week.mean())

print('1 week forecast = 178')
print('2 week forecast = 195')
