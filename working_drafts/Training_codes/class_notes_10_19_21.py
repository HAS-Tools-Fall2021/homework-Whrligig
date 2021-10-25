# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dataretrieval.nwis as nwis

# %%
# Create API using dataretrieval package
station_id = "09379200"
start_date = '1989-01-01'
stop_date = '2021-10-17'
obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=stop_date, parameterCd='00060')

oct_flow = obs_day[obs_day.index.month == 10]
obs_day['day'] = obs_day.index.day
oct_median = obs_day.groupby(obs_day.index.day).median()
oct_median = obs_day.groupby('day').median()
oct_max = obs_day.groupby('day').max()
oct_min = obs_day.groupby('day').min()

flow_median = oct_median['00060_Mean']
flow_min = oct_min['00060_Mean']
flow_max = oct_max['00060_Mean']


fig, ax = plt.subplots()
ax.plot(flow_median, color='grey',
        linestyle='dashed', label='Median')
ax.fill_between(oct_max.index, flow_min, flow_max, color='blue', alpha=0.1)
ax.plot(flow_min, color='blue', linestyle='dashed', label='Min')
ax.plot(flow_max, color='blue', linestyle='dashed', label='Max')
ax.plot(oct_flow["2020"].index.day, oct_flow["2020"]index['00060_Mean'], color='black', label='2020 flow')
ax.set(title="Observed Flow", xlabel="Date",
       ylabel="Daily Avg Flow [cfs]",
       yscale='log')
ax.legend()


# %%
station_id = "09535300"
start_date = '1989-01-01'
stop_date = '2020-10-17'
obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=stop_date, parameterCd='00060')
