# %%
import os
import pandas as pd
import numpy as np
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset

# %%
# Setting the file name and path to where I have stored the data.
# Filepath for forecast submission folder.

filename = 'streamflow_week11.txt'
filepath = os.path.join('..', '..', 'working_drafts', 'data', filename)
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
# Create functions for analyzing accessed datasets

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
def historical_ET(startyear, endyear, month, first_fcst_st_day,
                  first_fcst_end_day, scnd_fcst_st_day,
                  scnd_fcst_end_day):
    '''Creates line plots of evapotranspiration for any streamflow forecast period.

        This function will plot a line for each year within
        the forecast window that is specified by the input parameters.

        Parameters
        ----------
        startyear: int
                Input the beginning year of the time frame desired.
                Ex: Want ET from 1990-1997? startyear=1990
        endyear: int
                Input the ending year of the time frame desired.
                Ex: Want ET from 1990-1997? endyear=1997
        month: int
                Input the month of flows desired.
                Ex: Want ET from each April 1990-1997? month=4
        first_fcst_st_day: int
                Input the starting day of the 1 week forecast window.
                Ex: Want ET for 03/10/89-03/16/89? first_fcst_st_day=10
        first_fcst_end_day: int
                Input the ending day of the 1 week forecast window.
                Ex: Want ET for 03/10/89-03/16/89? first_fcst_end_day=16
        scnd_fcst_st_day: int
                Input the starting day of the 2 week forecast window.
                Ex: Want ET for 03/17/89-03/23/89? scnd_fcst_st_day=17
        scnd_fcst_end_day: int
                Input the ending day of the 1 week forecast window.
                Ex: Want ET for 03/17/89-03/23/89? scnd_fcst_end_day=23

        Returns
        ------
        plt.show(): graph
                Function creates plot of all ET values meeting function
                criteria within time frame.
        fig: figure variable
                Function returns figure variable so users can specify
                additional plot attributes for the generated graph
                during individual use of the function.
        '''

    line_pal = sns.color_palette('plasma', 5)
    clr_choose = 0
    fig, ax = plt.subplots(2, 1)
    for i in range(startyear, endyear):
        fcst_1_plot = ET_dataframe[(ET_dataframe.index.year == i) &
                           (ET_dataframe.index.month == month) &
                           (ET_dataframe.index.day >= first_fcst_st_day)
                           & (ET_dataframe.index.day <= first_fcst_end_day)]
        ax[0].plot(fcst_1_plot.index.day, fcst_1_plot['et'],
                   color=line_pal[clr_choose], label=i)
        ax[0].set(title='ET History During 1 Week Forecast Window',
                  ylabel='ET [mm/s]', yscale='log')
        ax[0].legend(loc='upper left')
        ax[0].grid(None, 'major', 'both', alpha=0.15)
        fcst_2_plot = ET_dataframe[(ET_dataframe.index.year == i) &
                           (ET_dataframe.index.month == month) &
                           (ET_dataframe.index.day >= scnd_fcst_st_day) &
                           (ET_dataframe.index.day <= scnd_fcst_end_day)]
        ax[1].plot(fcst_2_plot.index.day, fcst_2_plot['et'],
                   color=line_pal[clr_choose], label=i)
        ax[1].set(title='ET History During 2 Week Forecast Window',
                  xlabel='Day in Month', ylabel='ET [mm/s]', yscale='log')
        ax[1].grid(None, 'major', 'both', alpha=0.15)
        clr_choose = clr_choose+1
    fig.set(facecolor='lightgrey', tight_layout=True)
    plt.show()

    return fig

# %%
def annual_precip(startyear, endyear):
    '''Creates line plots of precipitation for 10 year increments in given window.

        This function will plot a line for every 10 years within
        the timeframe that is specified by the input parameters.

        Parameters
        ----------
        startyear: int
                Input the beginning year of the time frame desired.
                Ex: Want precip from 1990-1997? startyear=1990
        endyear: int
                Input the ending year of the time frame desired.
                Ex: Want precip from 1990-1997? endyear=1997

        Returns
        ------
        plt.show(): graph
                Function creates plot of all precip values at 10 year intervals
                meeting function criteria within time frame.
        fig: figure variable
                Function returns figure variable so users can specify
                additional plot attributes for the generated graph
                during individual use of the function.
        '''

    line_pal = sns.color_palette('plasma')
    clr_choose = 0
    fig, ax = plt.subplots()
    for i in np.arange(startyear, endyear, 10):
        plot1 = precip_dataframe[(precip_dataframe.index.year == i)]
        ax.plot(plot1.index, plot1['prate'],
                   color=line_pal[clr_choose+1], label=i)
        ax.set(title='Annual Precipitation',
                  ylabel='Precip Rate [kg/m^2/s]', xlabel='Year')
        ax.legend(loc='upper left')
        ax.grid(None, 'major', 'both', alpha=0.15)
        clr_choose = clr_choose+1
    fig.set(facecolor='lightgrey', tight_layout=True)
    plt.show()

    return fig

# %%
def historical_precip(startyear, endyear, month, first_fcst_st_day,
                  first_fcst_end_day, scnd_fcst_st_day,
                  scnd_fcst_end_day):
    '''Creates line plots of evapotranspiration for any streamflow forecast period.

        This function will plot a line for each year within
        the forecast window that is specified by the input parameters.

        Parameters
        ----------
        startyear: int
                Input the beginning year of the time frame desired.
                Ex: Want ET from 1990-1997? startyear=1990
        endyear: int
                Input the ending year of the time frame desired.
                Ex: Want ET from 1990-1997? endyear=1997
        month: int
                Input the month of flows desired.
                Ex: Want ET from each April 1990-1997? month=4
        first_fcst_st_day: int
                Input the starting day of the 1 week forecast window.
                Ex: Want ET for 03/10/89-03/16/89? first_fcst_st_day=10
        first_fcst_end_day: int
                Input the ending day of the 1 week forecast window.
                Ex: Want ET for 03/10/89-03/16/89? first_fcst_end_day=16
        scnd_fcst_st_day: int
                Input the starting day of the 2 week forecast window.
                Ex: Want ET for 03/17/89-03/23/89? scnd_fcst_st_day=17
        scnd_fcst_end_day: int
                Input the ending day of the 1 week forecast window.
                Ex: Want ET for 03/17/89-03/23/89? scnd_fcst_end_day=23

        Returns
        ------
        plt.show(): graph
                Function creates plot of all ET values meeting function
                criteria within time frame.
        fig: figure variable
                Function returns figure variable so users can specify
                additional plot attributes for the generated graph
                during individual use of the function.
        '''

    line_pal = sns.color_palette('plasma', 5)
    clr_choose = 0
    fig, ax = plt.subplots(2, 1)
    for i in range(startyear, endyear):
        fcst_1_plot = precip_dataframe[(precip_dataframe.index.year == i) &
                           (precip_dataframe.index.month == month) &
                           (precip_dataframe.index.day >= first_fcst_st_day)
                           & (precip_dataframe.index.day <= first_fcst_end_day)]
        ax[0].plot(fcst_1_plot.index.day, fcst_1_plot['prate'],
                   color=line_pal[clr_choose], label=i)
        ax[0].set(title='Precip History During 1 Week Forecast Window',
                  ylabel='Precip Rate [kg/m^2/s]')
        ax[0].legend(loc='upper left')
        ax[0].grid(None, 'major', 'both', alpha=0.15)
        fcst_2_plot = precip_dataframe[(precip_dataframe.index.year == i) &
                           (precip_dataframe.index.month == month) &
                           (precip_dataframe.index.day >= scnd_fcst_st_day) &
                           (precip_dataframe.index.day <= scnd_fcst_end_day)]
        ax[1].plot(fcst_2_plot.index.day, fcst_2_plot['prate'],
                   color=line_pal[clr_choose], label=i)
        ax[1].set(title='Precip History During 2 Week Forecast Window',
                  xlabel='Day in Month', ylabel='Precip Rate [kg/m^2/s]')
        ax[1].grid(None, 'major', 'both', alpha=0.15)
        clr_choose = clr_choose+1
    fig.set(facecolor='lightgrey', tight_layout=True)
    plt.show()

    return fig


# %%
# Find mean flow for Week 10 forecast period

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
ax.set(title="Observed Flow for Week 10/31/21 - 11/06/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 10, 31), datetime.date(2021, 11, 6)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

# fig.savefig('../../Forecast_Submissions/images/Wk11_Obs.png',
#              dpi=300, bbox_inches='tight')

# %%
# The historical_weekly function will generate a line plot with lines
# for each of the years within the forecast range between the starting year
# and ending year. Flows in 2018 are excluded on the second subplot to make
# the plot more readable.

# Run new function for 1 Week forecast period, create plot
# of 5 year history.
start_year = 2016
end_year = 2021
fcst_month = 11
one_wk_st = 7
one_wk_end = 13
two_wk_st = 14
two_wk_end = 20

fig = historical_weekly_flow(start_year, end_year, fcst_month, one_wk_st,
                             one_wk_end, two_wk_st, two_wk_end)

# %%
# Print histogram of November flows for the whole dataset, 1989-2021.
fig, ax = plt.subplots()

m = 11
month = data[data.index.month == m]
plot_title = 'November Flow Histogram'
ax.hist(np.log10(month['flow']), bins=30,
        edgecolor='grey', color='aquamarine')
ax.set(xlabel='Flow (cfs) [log scale]', ylabel='count', title=plot_title)
ax.grid(None, 'major', 'both', alpha=0.15)
fig.set(facecolor='lightgrey')

# %%
# Insert netcdf data for first dataset:
hier_path1 = os.path.join('..', 'data', 'Hierarchical_Data',
                          '1989_2021_NCEP_PrecipRate_Data.nc')
precip_netcdf = xr.open_dataset(hier_path1)
precip_netcdf

# Grab the precipitation data from the netcdf
precip = precip_netcdf['prate']
precip

# See the lat and lon values in the dataset
precip_netcdf['prate']['lat'].values
precip_netcdf['prate']['lon'].values

# Pull lat and lon values for the first data point in the dataset
# lat = 35.2375, lon = 247.5
precip_lat = precip_netcdf["prate"]["lat"].values[0]
precip_lon = precip_netcdf["prate"]["lon"].values[0]
print('lat =', precip_lat)
print('lon =', precip_lon)
precip_points = precip_netcdf["prate"].sel(lat=precip_lat, lon=precip_lon)
precip_points.shape

# Convert to dataframe
precip_dataframe = precip_points.to_dataframe()

# %%
# Insert netcdf data for second dataset:
hier_path2 = os.path.join('..', 'data', 'Hierarchical_Data',
                          '2006_2011_Livneh_DailyET_Data.nc')
ET_netcdf = xr.open_dataset(hier_path2)
ET_netcdf

# Grab the evapotranspiration data from the netcdf
evapotrans = ET_netcdf['et']
evapotrans

# Find all the lat and lon values in the dataset to find the
# closest lat/lon pair to the values pulled from the precip dataset
ET_netcdf['et']['lat'].values
ET_netcdf['et']['lon'].values

# Closest pair is lat = 34.84375, lon = 247.84375
# (closer individual lat and lon values but this was a close pair)
ET_lat = ET_netcdf['et']['lat'].values[29]
ET_lon = ET_netcdf["et"]["lon"].values[29]
print('lat =', ET_lat)
print('lon =', ET_lon)
ET_points = ET_netcdf["et"].sel(lat=ET_lat, lon=ET_lon)
# Check shape of ET_points dataset (should have 1 value per year,
# so should be same size as time dimension in ET dataset)
ET_points.shape

# Convert to dataframe
ET_dataframe = ET_points.to_dataframe()

# See what the dataframe looks like
ET_dataframe

# %%
# Make a timeseries plot of ET and Precip rate
fig, [ax1, ax2] = plt.subplots(2, 1, figsize=(12, 8))
fig.patch.set_facecolor('lightgray')
precip_points.plot.line(hue='lat',
                        marker="o",
                        ax=ax1,
                        color="grey",
                        markerfacecolor="blue",
                        markeredgecolor="blue")
ax1.set(title="Time Series for 35.2375N, 247.5E")
ax1.grid(None, 'major', 'both', alpha=0.15)
ET_points.plot.line(ax=ax2,
                    color="r", linewidth=0.5)
ax2.set(title="Time Series for 34.84375N, 247.84375E")
ax2.grid(None, 'major', 'both', alpha=0.15)
fig.tight_layout()
plt.show()

# fig.savefig('../../Forecast_Submissions/images/ET_Precip_Timeseries.png',
#             dpi=300, bbox_inches='tight')

# %%
# Make plot of ET value changes over the ET dataframe within
# the forecast periods
start_year = 2006
end_year = 2011
fcst_month = 11
one_wk_st = 7
one_wk_end = 13
two_wk_st = 14
two_wk_end = 20

fig = historical_ET(start_year, end_year, fcst_month, one_wk_st,
                             one_wk_end, two_wk_st, two_wk_end)

# %%
# Precipitation rate change every 10 years
start_year = 1989
end_year = 2021

fig = annual_precip(start_year, end_year)

# %%
# Precipitation rate during forecast windows
start_year = 2006
end_year = 2011
fcst_month = 11
one_wk_st = 7
one_wk_end = 13
two_wk_st = 14
two_wk_end = 20

fig = historical_precip(start_year, end_year, fcst_month, one_wk_st,
                             one_wk_end, two_wk_st, two_wk_end)
# %%
print('1 Week Forecast:', 128, 'cfs')
print('2 Week Forecast:', 125, 'cfs')
