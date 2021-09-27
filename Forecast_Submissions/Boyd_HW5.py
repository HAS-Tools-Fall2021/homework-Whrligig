# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set the file name and path to where you have stored the data
filename = 'streamflow_week5.txt'
filepath = os.path.join('..\data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week5.txt'

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# List of Functions that I can use with dataframes
data['flow'].describe()
data.groupby
data.head(6)
data.tail(6)
data.sort_values

# Code to find the avg flow for one month as well as the 50th percentile flow.
# But remember that the years are not connected to the flows in this frame.
data[data['month']==9].describe()

# Code for the last week of flow data, gives the mean flow value 
# among other summary statistics.
data[11949:11955][['flow']].describe()

# %%
# Question 1:
# This gives the column names in the dataframe
data.columns
# This gives the index of the dataframe
print('The index of the dataframe follows:')
data.index
# This gives the datatypes stored in the dataframe
data.dtypes
# %%
# Question 2:
# This version puts the output in a data series format (but it provides the dtype)
data['flow'].describe()
# This version puts the output in a dataframe
data[['flow']].describe()

# %%
# Question 3:
data.groupby(['month'])[['flow']].describe()

# %%
# Question 4:
# Using sort_values should give an abbreviated table of the dataset that automatically has the max 5 and min 5 flow values shown,
# but in case it does not, the additional code below can also be used to find the values, although not in one table.
data.sort_values(by='flow', ascending=False)

print('The 5 largest flow values for the period of record:')
print(data.sort_values(by='flow', ascending=False).head(5))
print('The 5 smallest flow values for the period of record:')
print(data.sort_values(by='flow', ascending=False).tail(5))

# %%
# Question 5:

# This code does not run properly, but I can't figure out how to get it to work.

min_array = np.array([])
max_array = np.array([])

for i in data:
            month_data = data.groupby(['month'])[['flow']]
            jan_head = data.sort_values(by='flow', ascending=False).head(1)    
            jan_tail = data.sort_values(by='flow', ascending=False).tail(1)    
            min_array = np.append(min_array, jan_tail)
            max_array = np.append(max_array, jan_head)


# Question 6:

tenguess1 = 93 * 0.1
low = 93 - tenguess1
high = 93 + tenguess1

data[(data['flow'] > low) & (data['flow'] < high)]

# This code yields 1,140 dates where the flow is within 
# 10% (plus or minus) my 1 week forecast.