# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Create a basic dataframe from scratch
dataframe_1 = pd.DataFrame(columns=["Precip_mm", "ET_mm"],
                           data=[
                                [0.3, 0.7],
                                [0.2, 0.5],
                                [0.2, 0.9]
                                ])
print(dataframe_1)

dataframe_1.iloc[0:3, 0:2]

# %%
# Create a dataframe by reading in a file
filename = 'streamflow_week8.txt'
filepath = os.path.join('../../working_drafts/data', filename)
print(os.getcwd())
print(filepath)

# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime'], index_col=['datetime']
                     )
