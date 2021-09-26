# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
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
data['flow'].describe()
data.groupby
data.head(6)
data.tail(6)
data.sort_values



data[11949:11955][['flow']].describe()


# %%
# Question 1:
data.columns
print('The index of the dataframe follows:')
data.index
data.dtypes
# %%
# Question 2:
# This version puts the output in a data series format (but it provides the dtype)
data['flow'].describe()
# This version puts the output in a dataframe
data[['flow']].describe()

# %%
# Question 3:
month_data = data.groupby(['month'])[['flow']].describe()

# %%
# Question 4:
# Using sort_values should give an abbreviated table that automatically has the max 5 and min 5 flow values,
# but in case it does not, the additional code below can also be used to find the values, although not in one table.
data.sort_values(by='flow', ascending=False)

print('The 5 largest flow values for the period of record:')
print(data.sort_values(by='flow', ascending=False).head(5))
print('The 5 smallest flow values for the period of record:')
print(data.sort_values(by='flow', ascending=False).tail(5))


# %%
