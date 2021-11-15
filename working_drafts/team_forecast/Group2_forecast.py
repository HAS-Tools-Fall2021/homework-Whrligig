# @Date:   2021-11-11T14:10:37-07:00
# @Last modified time: 2021-11-11T14:48:29-07:00

# %%
import os
import pandas as pd
import numpy as np
# import cartopy.crs as ccrs
# import cartopy.feature as cfeature
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import geopandas as gpd
import fiona
import contextily as ctx
import xarray as xr
import shapely
from shapely.geometry import Point
from netCDF4 import Dataset
import datetime
from   sklearn.linear_model import LinearRegression

# %%
# Our Plan:

# Linear regression -- Xingyu (Use middle 10 years,
# then use most recent 10 years for regression)
       # Air temp regression with precip rate
       # Precip regression with streamflow
# Adding in precip netcdf, Air Temp netcdf -- Connal
# Add chart of previous week's flow -- Connal
# Add function (tie to regression in some way, likely w/ a graph) -- Steph
# Add Map -- Andrew
# Add timeseries plots of netcdf, spatial means of November -- Andrew

flow_url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb" \
           "&site_no=09506000&referred_module=sw" \
           "&period=&begin_date=1989-01-01&end_date=2021-11-13"
flow_data = pd.read_table(flow_url, sep='\t', skiprows=30,
                          names=['agency_cd', 'site_no', 'datetime', 'flow',
                                 'code'], parse_dates=['datetime'],
                          index_col=['datetime'])
flow_data['month'] = pd.DatetimeIndex(flow_data.index).month
flow_data['day'] = pd.DatetimeIndex(flow_data.index).day
flow_data['year'] = pd.DatetimeIndex(flow_data.index).year


## Xingyu
#flow_w=flow_data.resample('W').mean()
flow_y=flow_data.resample('Y').mean()
flow_w=flow_data
flow_w['month'] = pd.DatetimeIndex(flow_w.index).month
flow_w['day'] = pd.DatetimeIndex(flow_w.index).day
# Resample the data to find and plot mean values for month of November
nov_flow = flow_w[flow_w['month'] == 11]


nov_pmean = nov_flow.groupby('year')['flow'].mean()
f, ax = plt.subplots(figsize=(12, 6))
nov_pmean.plot.line(marker="o",
                    ax=ax,
                    color="lightgray",
                    markerfacecolor="steelblue",
                    markeredgecolor="steelblue")
ax.set(title="November flow",
       xlabel="Day of the Month",
       ylabel="flow (kg/m^2)")


####because in 2004, the flow is extremely high. The data before 2004 can not use 
flow_data.drop(flow_data[flow_data['year']<2020].index,inplace=True)
flow_data_2=flow_data[:]
flow_data=flow_data[:-2]
nov_flow = flow_data[flow_data['month'] == 11]
# %% 
# Read in NetCDF Precipitation Data
precip_path = os.path.join('..', 'data', 'Hierarchical_Data',
                           '1989_2021_NCEP_PrecipRate_Data_v4.nc')
precip = xr.open_dataset(precip_path)
precip

# Find size of NetCDF precip data
# (2 lat values, 2 lon values, 11993 time values)
precip['prate']['lat'].size
precip['prate']['lon'].size
precip["prate"]["time"].size

# Extract single point, convert it to dataframe to make time series
# Extract years, days, months from datetime index to allow for resampling
# Index 0,0 closest to stream gauge

point_precip = precip["prate"]
precip_df = point_precip.to_dataframe()
precip_df = precip_df.groupby('time').mean()
precip_df['year'] = pd.DatetimeIndex(precip_df.index).year
precip_df['month'] = pd.DatetimeIndex(precip_df.index).month
precip_df['day'] = pd.DatetimeIndex(precip_df.index).day
precip_df.drop(precip_df[precip_df['year']<2020].index,inplace=True)


# Resample the data to find and plot mean values for month of November
nov_precip = precip_df[precip_df['month'] == 11]
nov_pmean = nov_precip.groupby('day')['prate'].mean()
f, ax = plt.subplots(figsize=(12, 6))
nov_pmean.plot.line(marker="o",
                    ax=ax,
                    color="lightgray",
                    markerfacecolor="steelblue",
                    markeredgecolor="steelblue")
ax.set(title="November Mean Precipitation For Gauge Location",
       xlabel="Day of the Month",
       ylabel="Precp Rate (kg/m^2)")

# %%
# Read in NetCDF temperature data
data_path = os.path.join('..', 'data', 'Hierarchical_Data',
                         '1989_2021_NCEP_AirTemp_Data.nc')
temp = xr.open_dataset(data_path)
temp

# Find size of NetCDF precip data
# (2 lat values, 2 lon values, 11993 time values)
temp['air']['lat'].size
temp['air']['lon'].size
temp["air"]["time"].size

# Extract single point, convert it to dataframe to make time series
# Extract years, days, months from datetime index to allow for resampling
# Index 0,0 closest to stream gauge
lat = temp["air"]["lat"].values[0]
lon = temp["air"]["lon"].values[0]

point_temp = temp["air"]
temp_df = point_temp.to_dataframe()
temp_df = temp_df.groupby('time').mean()
temp_df['year'] = pd.DatetimeIndex(temp_df.index).year
temp_df['month'] = pd.DatetimeIndex(temp_df.index).month
temp_df['day'] = pd.DatetimeIndex(temp_df.index).day
temp_df.drop(temp_df[temp_df['year']<2020].index,inplace=True)


# Resample the data to find and plot mean values for month of November
nov_temp = temp_df[temp_df['month'] == 11]
nov_tmean = nov_temp.groupby('day')['air'].mean()
fig, ax = plt.subplots(figsize=(12, 6))
nov_tmean.plot.line(marker="o",
                    ax=ax,
                    color="lightgray",
                    markerfacecolor="steelblue",
                    markeredgecolor="steelblue")
ax.set(title="November Mean Temperature For Gauge Location",
       xlabel="Day of the Month",
       ylabel="Temperature(K)")
fig.set(facecolor='lightgrey')
plt.show()


# Extract precip values as a numpy array for spatial plotting
precip_val = precip["prate"].values
precip_val.shape
type(precip_val)

# %%
# Add in plot of streamflow behavior during last forecast period
date_format = mdates.DateFormatter("%m/%d")
fig, ax = plt.subplots()
ax.plot(flow_data_2['flow'], label='Daily Flow', marker='o',
        color='darkturquoise')
ax.set(title="Observed Flow for Week 11/07/21 - 11/13/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 11, 7), datetime.date(2021, 11, 13)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

# %%
# Reading in gage data using geopandas
gages_file = os.path.join('..', 'data', 'Shapefiles_and_GDBs',
                          'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(gages_file)

# Get data just from the state of Arizona
gages_AZ = gages[gages['STATE'] == 'AZ']
gages_AZ.shape
gages_AZ.head()

# Plot drainage area of each gage in AZ
fig, ax = plt.subplots(figsize=(10, 10))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=45, cmap='cividis',
              ax=ax)
ax.set_title("Arizona stream gauge drainge area\n (sq km)")
fig.set(facecolor='lightgrey')
plt.show()

# %%
# Read in watershed boundary shapefile
HUC_file = os.path.join('..', 'data', 'Shapefiles_and_GDBs',
                        'NHD_H_15060202_HU8_GDB.gdb')
fiona.listlayers(HUC_file)
HUC4 = gpd.read_file(HUC_file, layer="WBDHU4")

# Check the type and see the list of layers
# Isolate HUC4 basin of interest (Salt River, includes verde)
type(HUC4)
HUC4.head()
HUC4 = HUC4.set_index('name')
saltverde = HUC4.loc[['Salt']]

# %%
# Add some points corresponding with those used in forecast (what are PSR, FGZ?)
# PSR: 34.6501, -112.4283
# FGZ: 35.1403, -111.6710
# Daymet Data:  34.5582, -111.8591
# Stream gauge:  34.44833333, -111.7891667
point_list = np.array([[-112.4283, 34.6501],
                       [-111.6710, 35.1403],
                       [-111.8591, 34.5582],
                       [-111.7891667, 34.44833333]])

# Convert these into spatial features, make a geodataframe
point_geom = [Point(xy) for xy in point_list]
point_geom
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC4.crs)

# %%
# Plot these on the first dataset, one layer at a time
fig, ax = plt.subplots(figsize=(10, 10))
saltverde.plot(ax=ax)
point_df.plot(ax=ax, color='crimson', label='Important Sites in Watershed')
saltverde.boundary.plot(ax=ax, color=None,
                        edgecolor='black', linewidth=1,
                        label='Salt River Watershed Extent')
ax.set_title("Salt River HUC4 Boundaries")
ax.legend()
fig.set(facecolor='lightgrey')
plt.show()

# %%
river_file = os.path.join('..', 'data', 'Shapefiles_and_GDBs',
                          'UAiR_Major_Rivers.shp')
rivers = gpd.read_file(river_file)

# %%
# Note this is a different projection system than the stream gauges
# CRS = Coordinate Reference System
saltverde.crs
gages.crs
rivers.crs

# The points won't show up in AZ because they are in a different projection
# We need to project them first
# points_project = point_df.to_crs(gages_AZ.crs)

# Now put it all together on one plot, clip to limit extent to Salt River
gages_project = gages_AZ.to_crs(saltverde.crs)
gages_project = gpd.clip(gages_project, saltverde)
river_project = rivers.to_crs(saltverde.crs)
river_project = gpd.clip(river_project, saltverde)

# Now plot again
fig, ax = plt.subplots(figsize=(10, 10))
gages_project.plot(column='DRAIN_SQKM', categorical=False,
                   legend=True, legend_kwds={'label': r'Drainage Area (km^2)'},
                   markersize=25, cmap='cividis', ax=ax, label='Gages')
river_project.plot(ax=ax, color='blue', label='Rivers')
point_df.plot(ax=ax, color='crimson', label='Forecast Points')
saltverde.boundary.plot(ax=ax, color=None,
                        edgecolor='black', linewidth=1,
                        label='Watershed Boundary')
ax.set(title="Salt River Basin Drainage (km^2)", xlabel="Longitude",
       ylabel="Latitude")
ctx.add_basemap(ax, crs=saltverde.crs)
ax.legend()
fig.set(facecolor='lightgrey')
plt.show()



########regression and forecast Xingyu
#%%
precip_df
temp_df
flow_data

flow_data['precip'] = (precip_df['prate']-np.mean(precip_df['prate']))/np.std(precip_df['prate'])
flow_data['temp'] = (temp_df['air']-np.mean(temp_df['air']))/np.std(temp_df['air'])
flow_data
# %%
# Build an autoregressive model 
flow_mean     = flow_data.resample('W').mean()
flow_mean['flow_tm1'] = flow_mean['flow'].shift(1)

# Using the entire flow data  
train = flow_mean[1:][['flow', 'flow_tm1' , 'precip', 'temp']]

# Build a linear regression model
model = LinearRegression()
x = train[['flow_tm1', 'precip', 'temp']] 
y = train['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

#print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Prediction
prediction = model.predict(train[['flow_tm1', 'precip', 'temp']])
print(" This week mean flow is ", round(prediction[0], 1))
print(" This week mean flow is ", round(prediction[1], 1))
#
# %%
# Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots(figsize=(20,4))
ax.plot(flow_mean.index[1:], flow_mean['flow'][1:],color='blue', label='simulated 2 lag')
ax.plot(flow_mean.index[1:], prediction,color='red', label='obs')
ax.set(title="Linear regression flow results", xlabel="time", ylabel="Simulation with 2 lag (cfs)",
       yscale='log', ylim=(0,15000))
ax.legend()
plt.show()

fig.savefig('forecast.jpg', dpi=300)
# %%
