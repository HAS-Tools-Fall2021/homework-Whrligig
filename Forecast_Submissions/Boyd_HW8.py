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
# The path should work, but modify file name and path as needed to
# access streamflow data for Week 8.
filename = 'streamflow_week8.txt'
filepath = os.path.join('../working_drafts/data', filename)
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

print('----------')

print('Avg flow for last week was:', last_week['flow'].mean())

print('----------')

# Summary chart of all October flows from 1989 to 2021.
print('Summary statistics for all October flows, \
        1989-2021, are as follows:')
past_oct = data[(data.index.month == 10)]['flow'].describe()
print(past_oct)

# %%
# Observed flow for Week 7 Forecast period.
date_format = mdates.DateFormatter("%m/%d")
fig, ax = plt.subplots()
ax.plot(data['flow'], label='Daily Flow', marker='o',
        color='darkturquoise')
ax.set(title="Observed Flow for Week 10/10/21 - 10/16/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 10, 10), datetime.date(2021, 10, 16)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()
# Figures were saved in advance, but the code used is listed below.
# fig.savefig('../Forecast_Submissions/images/Wk7_Obs.png',
#             dpi=300, bbox_inches='tight')

# %%
# Create function that generates plots of historical flows
# for any given forecast window.


def historical_weekly_flow(startyear, endyear, month, daystart, dayend):
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
        daystart: int
                Input the starting day of the future forecast week window.
                Ex: Want flows for 03/20/89-03/26/89? daystart=20
        dayend: int
                Input the ending day of the future forecast week window.
                Ex: Want flows for 03/20/89-03/26/89? dayend=26

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
    fig, ax = plt.subplots(2, 1, sharex=True)
    for i in range(startyear, endyear):
        plot_data = data[(data.index.year == i) &
                         (data.index.month == month) &
                         (data.index.day >= daystart)
                         & (data.index.day <= dayend)]
        ax[0].plot(plot_data.index.day, plot_data['flow'],
                   color=line_pal[clr_choose], label=i)
        ax[0].set(title='Flow History of Forecast Week',
                  yscale='log', ylabel='Flow (cfs) [log scale]')
        ax[0].legend(loc='upper right')
        ax[0].grid(None, 'major', 'both', alpha=0.15)
        plot_data2 = data[(data.index.year == i) &
                          (data.index.year != 2018) &
                          (data.index.month == month) &
                          (data.index.day >= daystart) &
                          (data.index.day <= dayend)]
        ax[1].plot(plot_data2.index.day, plot_data2['flow'],
                   color=line_pal[clr_choose], label=i)
        ax[1].set(title='Same Plot (Excluding 2018)',
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
fcst_month = 10
fcst_st = 17
fcst_end = 23

fig = historical_weekly_flow(start_year, end_year, fcst_month, fcst_st,
                             fcst_end)
# Figures were saved in advance, but the code used is listed below.
# fig.savefig('../Forecast_Submissions/images/1Wk_Flow_History.png',
#             dpi=300, bbox_inches='tight')

# Run new function for 2 Week forecast period, create plot
# of 5 year history.
start_year = 2016
end_year = 2021
fcst_month = 10
fcst_st = 24
fcst_end = 30

fig = historical_weekly_flow(start_year, end_year, fcst_month, fcst_st,
                             fcst_end)
# Figures were saved in advance, but the code used is listed below.
# fig.savefig('../Forecast_Submissions/images/2Wk_Flow_History.png',
#             dpi=300, bbox_inches='tight')

# %%
# Print histogram of October flows for the whole dataset, 1989-2021.
fig, ax = plt.subplots()

m = 10
month = data[data.index.month == m]
plot_title = 'October Flow Histogram'
ax.hist(np.log10(month['flow']), bins=30,
        edgecolor='grey', color='aquamarine')
ax.set(xlabel='Flow (cfs) [log scale]', ylabel='count', title=plot_title)
ax.grid(None, 'major', 'both', alpha=0.15)
fig.set(facecolor='lightgrey')
# Figures were saved in advance, but the code used is listed below.
# fig.savefig('../Forecast_Submissions/images/Month_Histogram.png',
#             dpi=300, bbox_inches='tight')

# %%
print('1 Week Forecast:', 148, 'cfs')
print('2 Week Forecast:', 150, 'cfs')
