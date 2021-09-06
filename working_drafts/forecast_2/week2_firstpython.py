# %%
# Step 1 - Download the data from the USGS website
# https: // waterdata.usgs.gov/nwis/dv?referred_module = sw & site_no = 09506000
# For now you should save this file to the directory you put this script in

# %%
# Step 2 - Import the modules we will use
import pandas as pd
import matplotlib.pyplot as plt
import os

# %% 
# Step 3 - Read in the file in as dataframe
# You will need to change the filename to match what you downloaded
filename = 'streamflow_week2.txt'
filepath = os.path.join(filename)

data=pd.read_table(filepath, sep = '\t', skiprows=30, 
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )
data = data.set_index('datetime')


# %%
# Step 4 - Look at the data
data.shape  # See how many rows and columns the data has
data.head(6) # look at the first x rows of the data
data.tail(7) # look at the last  x rows  of the data

data.iloc[11900:11920] # grab any subset of rows to look at
data.flow[247:254]  #Grab a subset of just the flow data dat look at
data.flow[3899:3906]  #Grab a subset of just the flow data dat look at
data.flow[7552:7559]  #Grab a subset of just the flow data dat look at

data.flow[254:261]  #Grab a subset of just the flow data dat look at
data.flow[3906:3913]  #Grab a subset of just the flow data dat look at
data.flow[7559:7566]  #Grab a subset of just the flow data dat look at

data.flow[11928:11934]  #Grab a subset of just the flow data dat look at

data.loc['1990-08-01']  #find a specific date

# %%
# Step 5 - Make a plot of the data
# Change the numbers on the followin lines to plot a different portion of the data
ax=data.iloc[0:11934]['flow'].plot(linewidth=0.5)
ax.set_ylabel('Daily Flow [cfs]')
ax.set_xlabel('Date')


# %%
