# %%

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Our Plan:
# Data
# Map
# Graphs
# Forecast Numbers

# Setting the file name and path to where we have stored the data.
filename = 'streamflow_week10.txt'
filepath = os.path.join('..', 'data', filename)
print(os.getcwd())
print(filepath)

# Filepath for forecast submission folder.
# filename = 'streamflow_week10.txt'
# filepath = os.path.join('..', '..', 'working_drafts', 'data', filename)
# print(os.getcwd())
# print(filepath)

# %%
# Read the data into a pandas dataframe.
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime']
                     )
