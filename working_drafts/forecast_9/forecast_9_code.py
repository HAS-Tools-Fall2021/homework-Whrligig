# %%
import os
import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
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
    'start': '200611080000',
    'end': '201911070000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum_one_hour_1',
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
airT = responseDict['STATION'][0]['OBSERVATIONS']['air_temp_set_1']

# Now we can combine this into a pandas dataframe
data = pd.DataFrame({'Temperature': airT}, index=pd.to_datetime(dateTime))

# Now convert this to daily data using resample
data_daily = data.resample('D').mean()

# %%
