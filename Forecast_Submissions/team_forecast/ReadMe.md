# Week 12 - Team forecast
## Group 2 - Connal Boyd, Andrew Hoopes, Steph Serrano, Zhang Xingyu


======\
1 Week Forecast: **156.1**

2 Week Forecast: **134.9**

Data used in Forecast:

1.1 the streamflow data before 2021 Nov 11, downloaded from the USGS web.
1.2 the precipitaion rate data in 1989 Jan 1st to 2021 Nov 11th, downloaded from the PSl web, averaged by time.
1.3 the air temperature data in 1989 Jan 1st to 2021 Nov 11th, downloaded from the PSl web, averaged by time.
(1.1 downloaded by Connal, 1.2 and 1.3 data downloaded by Xingyu)

=======\
### A brief summary of your collaboration. What did each team member bring to the table, who did what and how did you decide how to combine things?
  - Andrew:
    - Coded the USGS daily streamflow values into the code while adding time-series plots and aiding in creating a map
  - Connal
    - Aided in the creation of the map and time-series plots while cleaning the code and adjusting file paths. Added in previous week's flow plot.
  - Xingyu
    - Linear regression plots with precipitation rates and air temperatures using NetCDF data from the NOAA PSL website.
  - Steph
    - Added a logarithmic function that showed daily flow values for the month of November for a given year.

=======\
### A summary of your forecast. This should be written as a narrative summary without any blocks of code. It should summarize the inputs and approach used and must include at least 1 map and 1 graph. Only include graphs that you talk about in your narrative.

  The USGS daily streamflow data values were coded into a Pandas Dataframe using a URL link where they were then resampled to extract only the November flow.The November flow averages for each year in the dataset were then plotted to see if there were any outliers within the data.
  
  ![picture 1](./Nov_flow.jpg) 

  The plot showed that the flow values before 2005 were extremely high in comparison to the rest of the values. The flow data was then modified to reflect values after 2005. Plots of precipitation and air temperature were also generated.

  ![picture 2](./Nov_precip.jpg)

  ![picture 3](./Nov_temp.jpg)

  Due to the high peak in flow in 2005, we could not use a long time series for our regression model. The linear regression algorithm could be overfitted if the sample time is too long, so years before 2020 were dropped from the analysis period. Although the latitude and longitude of precipitation and air temperature are different, we can make an average of the whole region (33-37N,246-250E). Streamflow, precipitation, and air temperature data were merged into one dataframe for use in the regression model. In addition, precipitation and air temperature data were normalized (minus mean and divided by standard deviation). Hierarchical data was then added to provide outside data that could potentially affect the streamflow values. The precipitation rates and air temperature near the Verde River Watershed were extracted from NetCDF files  using the NOAA PSL website and plotted on graphs. We then resampled the precipitation, air temperature, and flow data into weekly data and used this to train the regression model. The coefficient of determination was 0.64, showing that the model fitted well. In this way, the forecast = 156.1 and 134.9, respectively. A plot of the streamflow during the previous forecast period (November 7th, 2021 to November 13th, 2021) was also added to see what current trend is occurring at the stream gage. 
  
  ![picture 4](./last_week_stream_flow.jpg) 

  A map of the state of Arizona was also added to the code. This map plotted the state of Arizona, the Verde River/Salt River Boundaries, and important points in the state. 
  
  ![picture 5](./linear_regression.jpg) 

  Finally, a logarithmic plot of the daily flow values for the month of November for whatever year was desired to be viewed was added in.

   ![picture 6](./Nov_log_obs.jpg) 
