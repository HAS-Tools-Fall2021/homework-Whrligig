# %%
import os
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json 
import urllib.request as req
import urllib

# %%
# Setting the file name and path to where I have stored the streamflow data.
filename = 'streamflow_week9.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the streamflow data into a pandas dataframe.
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime']
                     )

# %%
# THIS CELL IS BROKEN!

# First Create the URL for the rest API
# Insert your token here
mytoken = 'c8f26d3fa6ce4d13971392ca8765c76a'

# This is the base url that will be the start our final url
base_url = "https://nwis.waterdata.usgs.gov/usa/nwis/uv/"

# Remaining URL to copy from printed API
# '?cb_00045=on&format=rdb&site_no=09504000&period=&begin_date=1989-01-01&end_date=2021-10-23'

# Specific arguments for the data that we want
args = {
    'site_no': '09504000',
    'PARAmeter_cd': '0045',
    'format': 'csv',
    'period': '',
    'begin_date': '1989-01-01',
    'end_date': '2021-10-23',
    'token': mytoken}

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this
responseDict = json.loads(response.read())

# This creates a dictionary for you
# The complete format of this dictonary is descibed here:
# https://developers.synopticdata.com/mesonet/v2/getting-started/
# Keys shows you the main elements of your dictionary
responseDict.keys()

# %%
# Print flow values for each day last week and total mean flow for last week
print('Flow for each day of the previous forecast period:')
last_week = data[['flow']].tail(7)
print(last_week)
print('Avg flow for last week was:', last_week['flow'].mean())

# Create plot of Week 8 flow values
date_format = mdates.DateFormatter("%m/%d")
fig, ax = plt.subplots()
ax.plot(data['flow'], label='Daily Flow', marker='o',
        color='darkturquoise')
ax.set(title="Observed Flow for Week 10/17/21 - 10/23/21", xlabel="Date",
       ylabel="Flow [cfs]", ylim=[0, 250],
       xlim=[datetime.date(2021, 10, 17), datetime.date(2021, 10, 23)])
ax.xaxis.set_major_formatter(date_format)
ax.grid(None, 'major', 'both', alpha=0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig('../../Forecast_Submissions/images/Wk8_Obs.png',
            dpi=300, bbox_inches='tight')

print('1 Week Forecast:', 145, 'cfs')
print('2 Week Forecast:', 140, 'cfs')

# %%
# THIS CELL IS BROKEN!

# How do I do this with Mesonet????
# Mesonet Resources:

# To find a list of station variables visit the website below:
# https://developers.synopticdata.com/about/station-variables/

# To use the Mesonet API Query Builder visit the website below:
# https://developers.synopticdata.com/mesonet/explorer/

# To look for active Mesonet stations visit the website below:
# https://explore.synopticdata.com/metadata/stations?status=ACTIVE 

# First Create the URL for the rest API
# Insert your token here
mytoken = 'c8f26d3fa6ce4d13971392ca8765c76a'

# This is the base url that will be the start our final url
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specific arguments for the data that we want
args = {
    'start': '200611200000',
    'end': '201911070000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum_one_hour',
    'stids': 'VDCA3',
    'units': 'precip|mm',
    'token': mytoken}

# Takes your arguments and paste them together
# into a string for the api
# (Note you could also do this by hand, but this is better)
apiString = urllib.parse.urlencode(args)
print(apiString)

# add the API string to the base_url
fullUrl = base_url + '?' + apiString
print(fullUrl)

# Now we are ready to request the data
# this just gives us the API response... not very useful yet
response = req.urlopen(fullUrl)

# What we need to do now is read this data
# The complete format of this
responseDict = json.loads(response.read())

# This creates a dictionary for you
# The complete format of this dictonary is descibed here:
# https://developers.synopticdata.com/mesonet/v2/getting-started/
# Keys shows you the main elements of your dictionary
responseDict.keys()
# You can inspect sub elements by looking up any of the keys in the dictionary
responseDict['UNITS']
responseDict['QC_SUMMARY']
responseDict['STATION']
responseDict['SUMMARY']
# Each key in the dictionary can link to differnt data structures
# For example 'UNITS is another dictionary'
type(responseDict['UNITS'])
responseDict['UNITS'].keys()
responseDict['UNITS']['position']

# where as STATION is a list
type(responseDict['STATION'])
# If we grab the first element of the list that is a dictionary
type(responseDict['STATION'][0])
# And these are its keys
responseDict['STATION'][0].keys()

# Long story short we can get to the data we want like this:
dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip = responseDict['STATION'][0]['SENSOR_VARIABLES']['precip_accum_one_hour']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'ACCUMULATION': precip}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_daily = data.resample('D').mean()
