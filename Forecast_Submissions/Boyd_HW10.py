# %%
# Import the modules used in the code
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# %%
# Setting the file name and path to where I have stored the data.
filename = 'streamflow_week10.txt'
filepath = os.path.join('..', 'working_drafts', 'data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe.
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime']
                     )

# %%
# Find mean flow for Week 7 forecast period

# Tail function is set to pull last seven values in dataset.
# The dataset contains data up to the previous week of flow.
print('Flow for each day of the previous forecast period:')
last_week = data[['flow']].tail(7)
print(last_week)
print('Avg flow for last week was:', last_week['flow'].mean())

print('----------')

# Summary chart of all November flows from 1989 to 2021.
print('Summary statistics for all November flows, \
        1989-2021, are as follows:')
past_nov = data[(data.index.month == 11)]['flow'].describe()
print(past_nov)

# %%
# Observed flow for Week 9 Forecast period.
date_format = mdates.DateFormatter("%m/%d")
fig, ax = plt.subplots()
ax.plot(data['flow'], label='Daily Flow', marker='o',
        color='darkturquoise')
ax.set(title="Observed Flow for Week 10/24/21 - 10/30/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 10, 24), datetime.date(2021, 10, 30)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

# fig.savefig('../../Forecast_Submissions/images/Wk9_Obs.png',
#            dpi=300, bbox_inches='tight')

# %%
# Create function that generates plots of historical flows
# for any given forecast window.


def historical_weekly_flow(startyear, endyear, month, first_fcst_st_day,
                           first_fcst_end_day, scnd_fcst_st_day,
                           scnd_fcst_end_day):
    '''Creates line plots of flow for any streamflow forecast period.

        This function will plot a line for each year within
        the forecast window that is specified by the input parameters.

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
        first_fcst_st_day: int
                Input the starting day of the 1 week forecast window.
                Ex: Want flows for 03/10/89-03/16/89? first_fcst_st_day=10
        first_fcst_end_day: int
                Input the ending day of the 1 week forecast window.
                Ex: Want flows for 03/10/89-03/16/89? first_fcst_end_day=16
        scnd_fcst_st_day: int
                Input the starting day of the 2 week forecast window.
                Ex: Want flows for 03/17/89-03/23/89? scnd_fcst_st_day=17
        scnd_fcst_end_day: int
                Input the ending day of the 1 week forecast window.
                Ex: Want flows for 03/17/89-03/23/89? scnd_fcst_end_day=23

        Returns
        ------
        plt.show(): graph
                Function creates plot of all flows meeting function
                criteria within time frame.
        fig: figure variable
                Function returns figure variable so users can specify
                additional plot attributes for the generated graph
                during individual use of the function.
        '''

    line_pal = sns.color_palette('viridis', 5)
    clr_choose = 0
    fig, ax = plt.subplots(2, 1)
    for i in range(startyear, endyear):
        fcst_1_plot = data[(data.index.year == i) &
                           (data.index.month == month) &
                           (data.index.day >= first_fcst_st_day)
                           & (data.index.day <= first_fcst_end_day)]
        ax[0].plot(fcst_1_plot.index.day, fcst_1_plot['flow'],
                   color=line_pal[clr_choose], label=i)
        ax[0].set(title='Flow History of 1 Week Forecast Window',
                  ylabel='Flow (cfs)')
        ax[0].legend(loc='upper left')
        ax[0].grid(None, 'major', 'both', alpha=0.15)
        fcst_2_plot = data[(data.index.year == i) &
                           (data.index.month == month) &
                           (data.index.day >= scnd_fcst_st_day) &
                           (data.index.day <= scnd_fcst_end_day)]
        ax[1].plot(fcst_2_plot.index.day, fcst_2_plot['flow'],
                   color=line_pal[clr_choose], label=i)
        ax[1].set(title='Flow History of 2 Week Forecast Window',
                  xlabel='Day in Month', ylabel='Flow (cfs)')
        ax[1].grid(None, 'major', 'both', alpha=0.15)
        clr_choose = clr_choose+1
    fig.set(facecolor='lightgrey', tight_layout=True)
    plt.show()

    return fig


# %%
# The new function will generate a line plot with lines for each of the years
# within the forecast range between the starting year and ending year.
# Flows in 2018 are excluded on the second subplot to make the plot
# more readable.

# Run new function for 1 Week forecast period, create plot
# of 5 year history.
start_year = 2016
end_year = 2021
fcst_month = 11
one_wk_st = 1
one_wk_end = 6
two_wk_st = 7
two_wk_end = 13


fig = historical_weekly_flow(start_year, end_year, fcst_month, one_wk_st,
                             one_wk_end, two_wk_st, two_wk_end)

# %%
# Print histogram of November flows for the whole dataset, 1989-2021.
fig, ax = plt.subplots()

m = 11
month = data[data.index.month == m]
plot_title = 'October Flow Histogram'
ax.hist(np.log10(month['flow']), bins=30,
        edgecolor='grey', color='aquamarine')
ax.set(xlabel='Flow (cfs) [log scale]', ylabel='count', title=plot_title)
ax.grid(None, 'major', 'both', alpha=0.15)
fig.set(facecolor='lightgrey')

# %%
print('1 Week Forecast:', 125, 'cfs')
print('2 Week Forecast:', 120, 'cfs')
