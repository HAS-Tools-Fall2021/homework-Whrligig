# Part 1 of data loading notes: 
# Options for loading streamflow data

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
import datetime
import os
import json 
import urllib.request as req
import urllib
import dataretrieval.nwis as nwis
from matplotlib.gridspec import GridSpec
# %%
# There are 3 ways to read data: 
# 1) Load a file that you have locally using read_table
# 2) Read a file using a URL for a Rest API using read_table 
# 3) Useing packages for specific APIs


#%%
#Note that we can also use this to make our URL within our code
station_id = "09506000"
start='1989-01-01'
end='2021-10-31'
data = nwis.get_record(sites=station_id, service='dv', start=start, end=end, parameterCd='00060')
data.columns = ['flow','agency_cd','site_no']

# What we are doing here is actually just interacting with the USGS's
# Rest API:
# Application Programming Interface: Application Programming Interface
# RESTful API is composed of a URL and the associated parameters
# We were just building the call to that API ourselves. 
# %%
flow_mean     = data.resample('W').mean()



# Generate two y axis plot
# %%


# %%
# Build an autoregressive model 
flow     = data.resample('W').mean()
flow_mean['flow_tm1'] = flow_mean['flow'].shift(1)
flow_mean['flow_tm2'] = flow_mean['flow'].shift(2)
flow_mean['flow_tm3'] = flow_mean['flow'].shift(3)

# Using the entire flow data  
train = flow_mean[3:][['flow', 'flow_tm1', 'flow_tm2','flow_tm3']]

# Build a linear regression model
model = LinearRegression()
x = train[['flow_tm1', 'flow_tm2','flow_tm3']] 
y = train['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

#print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Prediction
prediction = model.predict(train[['flow_tm1', 'flow_tm2','flow_tm3']])
print(" This week mean flow is ", round(prediction[0], 1))
print(" This week mean flow is ", round(prediction[1], 1))
#
# %%
# Line  plot comparison of predicted and observed flows
fig, ax = plt.subplots(figsize=(20,4))
ax.plot(flow_mean.index[3:], flow_mean['flow'][3:],color='blue', label='simulated 2 lag')
ax.plot(flow_mean.index[3:], prediction,color='red', label='obs')
ax.set(title="Linear regression flow results", xlabel="time", ylabel="Simulation with 2 lag (cfs)",
       yscale='log', ylim=(0,15000))
ax.legend()
plt.show()

fig.savefig('forecast.jpg', dpi=300)

# %%

# %%
