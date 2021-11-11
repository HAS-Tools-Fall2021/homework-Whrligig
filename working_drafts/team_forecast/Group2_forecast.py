# @Date:   2021-11-11T14:10:37-07:00
# @Last modified time: 2021-11-11T14:13:40-07:00



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

flow_url = "https://waterdata.usgs.gov/nwis/dv?cb_00060=on&format=rdb" \
           "&site_no=09506000&referred_module=sw" \
           "&period=&begin_date=1989-01-01&end_date=2021-11-06"
flow_data = pd.read_table(flow_url, sep='\t', skiprows=30,
                          names=['agency_cd', 'site_no', 'datetime', 'flow',
                                 'code'], parse_dates=['datetime'],
                          index_col=['datetime'])


# Linear regression
# precip netcdf, evapotrans cdf, compare to streamflow
# Add air temperature data
       # Air temp regression with precip rate
       # Precip regression with streamflow
# Use middle 10 years, then use most recent 10 years for regression

