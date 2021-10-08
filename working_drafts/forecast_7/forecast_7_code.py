# %%
# Import the modules used in the code
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# %%
# Set the file name and path to where you have stored the data
# Modify file name and path as needed to access streamflow data for Week 7
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# Read the data into a pandas dataframe (Should not need to change this)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no', 'datetime',
                            'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek









# %%

data[(data['month'] == 10)].describe()
last_week = data[['flow']].tail(6)
last_week.mean()

# Plots used for Forecast 6:

# Plot 1 - Observed flow for Week 5 Forecast
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], label='Daily Flow', 
        color='darkturquoise')
ax.set(title="Observed Flow for Week 09/26/21 - 10/01/21", xlabel="Date",
                ylabel="Flow [cfs]", ylim=[0, 250],
                xlim=[datetime.date(2021, 9, 26), datetime.date(2021, 10, 1)])
ax.grid(None,'major','both', alpha= 0.15)
ax.legend(loc='lower right')
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_1.png")

# Plot 2 - Line plot showing trends of flows for last 5 years
my_Sep_pal = sns.color_palette('plasma', 5)
clr_choose1 = 0
fig, ax = plt.subplots()
for i in range(2017, 2022):
        plot_data=data[(data['year']==i) & (data['month']==9)]
        ax.plot(plot_data['day'], plot_data['flow'],
                color=my_Sep_pal[clr_choose1], label=i)
        ax.set(title='September Flow Trends for Previous 5 Years', 
                xlabel='Day of Month', ylabel='Flow (cfs)', yscale='log')
        ax.grid(None,'major','both', alpha= 0.15)
        ax.legend()
        clr_choose1 = clr_choose1+1
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_2a.png")

my_Oct_pal = sns.color_palette('viridis', 5)
clr_choose2 = 0
fig, ax = plt.subplots()
for i in range(2016, 2021):
        plot_data=data[(data['year']==i) & (data['month']==10)]
        ax.plot(plot_data['day'], plot_data['flow'],
                color=my_Oct_pal[clr_choose2], label=i)
        ax.set(title='October Flow Trends for Previous 5 Years', 
                xlabel='Day of Month', ylabel='Flow (cfs)', yscale='log')
        ax.grid(None,'major','both', alpha= 0.15)
        ax.legend()
        clr_choose2 = clr_choose2+1
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_2b.png")

# Plot 3 - Scatter plot comparing 2021 September flow to 2017 September flow

fig, ax = plt.subplots()

ax.scatter(data[(data['year'] == 2017) & (data['month'] == 9)].flow, 
        data[(data['year'] == 2021) & (data['month'] == 9)].flow, 
        label= 'September Flow Values', marker='o',
           color='darkcyan')
ax.set(title='September 2017 v. September 2021', xlabel='2017 flow', 
        ylabel='2021 flow', yscale='log', xscale='log')
ax.grid(None,'major','both', alpha= 0.15)
ax.legend()
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_3.png")

# Plot 4 - Box Plot showing potential departure of values from average flow values
fig, ax = plt.subplots()
ax = sns.boxplot(x="month", y="flow", palette='plasma', data=data,
                 linewidth=0.3)
ax.set(title='Flow Trends Per Month 1989-2021', yscale='log', xlabel='Month of Year', ylabel='Average Flow (cfs)')
ax.grid(None,'major','both', alpha= 0.15)
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_4.png")

# Plot 5 - Line plots showing weekly flow for 1 week forecast for Week 6 for last 5 years
my_past_pal = sns.color_palette('inferno', 5)
my_past_pal
clr_choose3 = 0
fig, ax = plt.subplots(2,1,sharex=True)
for i in range(2016, 2021):
        plot_data=data[(data['year']==i) & 
                (data['month']==10) & (data['day']<=9) & (data['day']>=3)]
        ax[0].plot(plot_data['day'], plot_data['flow'],
                color=my_past_pal[clr_choose3], label=i)
        ax[0].set(title='5 Year Flow History for Week 10/03/21 - 10/09/21', 
                yscale='log', ylabel='Flow (cfs)')
        ax[0].legend(loc='upper right')
        ax[0].grid(None,'major','both', alpha= 0.15)
        clr_choose3 = clr_choose3+1
clr_choose4 = 0
for i in range(2016, 2021):
        plot_data=data[(data['year']==i) & (data['year']!=2018) & # this code gets rid of the 2018 data so it doesn't show on the plot
                (data['month']==10) & (data['day']<=9) & (data['day']>=3)]
        ax[1].plot(plot_data['day'], plot_data['flow'],
                color=my_past_pal[clr_choose4], label=i)
        ax[1].set(title='Same Plot for 10/03/21 - 10/09/21 (Excluding 2018)', 
                xlabel='Day in October', ylabel='Flow (cfs)')
        ax[1].grid(None,'major','both', alpha= 0.15)
        clr_choose4 = clr_choose4+1
fig.tight_layout()
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_5.png")

# Plot 6 - Histogram of flows in September and October
fig, ax = plt.subplots(2,1, sharex=True)

m = 9
month = data[data['month'] == m]
plot_title = 'Month ' + str(m)
ax[0].hist(np.log10(month['flow']), bins=30, 
        edgecolor='grey', color='powderblue')
ax[0].set(ylabel='Count', title=plot_title)
ax[0].grid(None,'major','both', alpha= 0.15)

mo = 10
month = data[data['month'] == mo]
plot_title = 'Month ' + str(mo)
ax[1].hist(np.log10(month['flow']), bins=30,
           edgecolor='grey', color='powderblue')
ax[1].set(xlabel='Flow (cfs) [log scale]', ylabel='count', title= plot_title)
ax[1].grid(None,'major','both', alpha= 0.15)

fig.tight_layout()
fig.set(facecolor='lightgrey')
plt.show()

fig.savefig("Plot_6.png")

# %%
