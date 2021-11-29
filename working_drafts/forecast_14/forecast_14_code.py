# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import xarray as xr
from sklearn.linear_model import LinearRegression

# Fix paths for new data before submitting forecast values

# %%
# Add in streamflow data
flow_url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb" \
              + "&site_no=09506000&referred_module=sw&period=" + \
                "&begin_date=1989-01-01&end_date=2021-11-27"
flow_data = pd.read_table(flow_url, sep='\t', skiprows=30,
                          names=['agency_cd', 'site_no', 'datetime', 'flow',
                                 'code'], parse_dates=['datetime'],
                          index_col=['datetime'])

# Assign additional datetime columns for use in plotting throughout the code
flow_data['month'] = pd.DatetimeIndex(flow_data.index).month
flow_data['day'] = pd.DatetimeIndex(flow_data.index).day
flow_data['year'] = pd.DatetimeIndex(flow_data.index).year

# %%
# Create plot of streamflow behavior during last forecast period
date_format = mdates.DateFormatter("%m/%d")
fig, ax = plt.subplots()
ax.plot(flow_data['flow'], label='Daily Flow', marker='o',
        color='lightgray',
        markerfacecolor='steelblue',
        markeredgecolor='steelblue')
ax.set(title="Observed Flow for Week 11/21/21 - 11/27/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 11, 21), datetime.date(2021, 11, 27)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

# %%
# Print flow data for last week
print('Flow during the last forecast period:')
last_week = flow_data[['flow']].tail(7)
print(last_week)
print('Avg flow for last week was:', last_week.mean())

# %%
# Add in Air temp data
temp_path = os.path.join('..', '..', 'working_drafts', 'data', 'Hierarchical_Data',
                         '2010_2021_NCEP_AirTemp_Data.nc')
temp = xr.open_dataset(temp_path)
temp

lat = temp['air']['lat'].values[0]
lon = temp['air']['lon'].values[0]

point_temp = temp['air']
temp_df = point_temp.to_dataframe()
temp_df = temp_df.groupby('time').mean()
temp_df['year'] = pd.DatetimeIndex(temp_df.index).year
temp_df['month'] = pd.DatetimeIndex(temp_df.index).month
temp_df['day'] = pd.DatetimeIndex(temp_df.index).day
temp_df.drop(temp_df[temp_df['year'] < 2020].index, inplace=True)

# %%
# Add in precipitation rate data
precip_path = os.path.join('..', '..', 'working_drafts', 'data', 'Hierarchical_Data',
                           '2010_2021_NCEP_PrecipRate_Data.nc')
precip = xr.open_dataset(precip_path)
precip
point_precip = precip['prate']
precip_df = point_precip.to_dataframe()
precip_df = precip_df.groupby('time').mean()
precip_df['year'] = pd.DatetimeIndex(precip_df.index).year
precip_df['month'] = pd.DatetimeIndex(precip_df.index).month
precip_df['day'] = pd.DatetimeIndex(precip_df.index).day
precip_df.drop(precip_df[precip_df['year'] < 2020].index, inplace=True)

# %%
# Do some data configuration to prepare data for use in the regression model

# Drop data before 2020
flow_drop = flow_data.drop(flow_data[flow_data.index.year < 2020].index, inplace=True)

precip_df
temp_df
# Drop the last value of the flow data since the precip and temp data
# do not go to 11/20
flow_data = flow_data[:-1]

# Combine streamflow, precip, and air temp into one dataframe
# Note that these three data types are at slightly different spatial resolutions
flow_data['precip'] = (precip_df['prate']-np.mean(precip_df['prate']))/np.std(precip_df['prate'])
flow_data['temp'] = (temp_df['air']-np.mean(temp_df['air']))/np.std(temp_df['air'])

# %%
# Build an autoregressive model
flow_mean = flow_data.resample('W').mean()
flow_mean['flow_tm1'] = flow_mean['flow'].shift(1)

# Traing the model using the flow, precip, and air temp data
train = flow_mean[1:][['flow', 'flow_tm1' , 'precip', 'temp']]

# Build a linear regression model
model = LinearRegression()
x = train[['flow_tm1', 'precip', 'temp']] 
y = train['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

# Print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Model forecast predictions
prediction = model.predict(train[['flow_tm1', 'precip', 'temp']])
print("1 Wk Forecast:", round(prediction[0], 1))
print("2 Wk Forecast:", round(prediction[1], 1))

# Line plot comparison of predicted and observed flows
fig, ax = plt.subplots(figsize=(20, 4))
ax.plot(flow_mean.index[1:], flow_mean['flow'][1:], color='blue',
        label='simulated 2 lag')
ax.plot(flow_mean.index[1:], prediction, color='red', label='obs')
ax.set(title="Linear regression flow results", xlabel="Time",
       ylabel="Simulation with 2 lag (cfs)",
       yscale='log', ylim=(1, 15000))
ax.legend()
fig.set(facecolor='lightgray')
plt.show()

# %%
