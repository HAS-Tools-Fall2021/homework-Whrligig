# %%
# Import the modules used in the code
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# %%
# Set the file name and path to where you have stored the data
# Modify file name and path as needed to access streamflow data for Week 7
filename = 'streamflow_week7.txt'
filepath = os.path.join(r'C:\Users\conna\Documents\HAS_Tools_Repo_Dump\homework\working_drafts\data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe (Should not need to change this)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %%

# Find mean flow for Week 6 forecast period

# Tail function is set to pull last six values in dataset. So if
# data downloaded on Saturday, October 9th there should only be
# 6 days of flow data available for the last forecast period.
print('Flow for the past 6 days of the last forecast period:')
last_week = data[['flow']].tail(6)
print(last_week)
print('Avg flow for last week was:', last_week.mean())

print('----------')

# Summary chart of all October flows from 1989 to 2021
print('Summary statistics for all October flows, \
        1989-2021, are as follows:')
past_oct = data[(data['month'] == 10)]['flow'].describe()
print(past_oct)

# Observed flow for Week 6 Forecast period
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], label='Daily Flow', marker='o',
        color='darkturquoise')
ax.set(title="Observed Flow for Week 10/03/21 - 10/08/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 10, 3), datetime.date(2021, 10, 8)])
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig('../images/Wk6_Obs.png')

# %%
# Create function that generates plots of historical flows
# for any given forecast window

def historical_weekly_flow(startyear, endyear, month, daystart, dayend):
        '''This function can be used to generate a plot of multiple years of flow data
        for a given week of any month of the Verde River streamflow dataset.

        Parameters
        ----------
        startyear: int
                Input the beginning year of the time frame desired.
                Ex: Want flows from 1990-1997? startyear=1990
        endyear: int
                Input the ending year of the time frame desired.
                Ex: Want flows from 1990-1997? endyear=1997
        month: int
                Input the month of flows desired.
                Ex: Want flows from each April 1990-1997? month=4
        daystart: int
                Input the starting day of the future forecast week window.
                Ex: Want flows for 03/20/89-03/26/89? daystart=20
        dayend: int
                Input the ending day of the future forecast week window.
                Ex: Want flows for 03/20/89-03/26/89? dayend=26

        Returns
        ------
        plt.show(): graph
                Function creates graph of all flows meeting function
                criteria within time frame.
        '''

        line_pal = sns.color_palette('inferno', 5)
        line_pal
        clr_choose = 0
        fig, ax = plt.subplots(2, 1, sharex=True)
        for i in range(startyear, endyear):
                plot_data = data[(data['year'] == i) &
                                 (data['month'] == month) &
                                 (data['day'] >= daystart)
                                 & (data['day'] <= dayend)]
                ax[0].plot(plot_data['day'], plot_data['flow'],
                           color=line_pal[clr_choose], label=i)
                ax[0].set(title='Flow History of Forecast Week',
                          yscale='log', ylabel='Flow (cfs)')
                ax[0].legend(loc='upper right')
                ax[0].grid(None, 'major', 'both', alpha=0.15)
                clr_choose = clr_choose+1

        clr_choose2 = 0
        for i in range(startyear, endyear):
                plot_data=data[(data['year'] == i) & (data['year'] != 2018) &
                               (data['month'] == month) &
                               (data['day'] >= daystart) &
                               (data['day'] <= dayend)]
                ax[1].plot(plot_data['day'], plot_data['flow'],
                           color=line_pal[clr_choose2], label=i)
                ax[1].set(title='Same Plot (Excluding 2018)',
                          xlabel='Day in Month', ylabel='Flow (cfs)')
                ax[1].grid(None, 'major', 'both', alpha=0.15)
                clr_choose2 = clr_choose2+1
        fig.tight_layout()
        fig.set(facecolor='lightgrey')

        return plt.show()


# %%
# Run new function with 1 Week forecast period
start_year = 2016
end_year = 2021
fcst_month = 10
fcst_st = 10
fcst_end = 16

historical_weekly_flow(start_year, end_year, fcst_month, fcst_st, fcst_end)

# Run new function with 2 Week forecast period
start_year = 2016
end_year = 2021
fcst_month = 10
fcst_st = 17
fcst_end = 23

historical_weekly_flow(start_year, end_year, fcst_month, fcst_st, fcst_end)

# Print histogram of October flows for the whole dataset
fig, ax = plt.subplots()

m = 10
month = data[data['month'] == m]
plot_title = 'October Flow Histogram'
ax.hist(np.log10(month['flow']), bins=30,
        edgecolor='grey', color='aquamarine')
ax.set(xlabel='Flow (cfs) [log scale]', ylabel='count', title=plot_title)
ax.grid(None, 'major', 'both', alpha=0.15)
fig.set(facecolor='lightgrey')
fig.savefig('../images/Oct_Hist.png')

# %%
print('1 Week Forecast:', 168, 'cfs')
print('2 Week Forecast:', 157, 'cfs')
