# Week 12 - Team forecast
## Group 2 - Connal Boyd, Andrew Hoopes, Steph Serrano, Zhang Xingyu

1) Week Forecast: **156.1**

2) Week Forecast: **134.9**

3) A brief summary of your collaboration. What did each team member bring to the table, who did what and how did you decide how to combine things?
  - Andrew:
    - Coded the USGS daily streamflow values into the code while adding time-series plots and aiding in creating a map
  - Connal
    - Aided in the creation of the map and time-series plots while cleaning the code and adjusting file paths..
  - Xingyu
    - Linear regression plots with precipitation rates and air temperatures using NetCDF data from the NOAA PSL website.
  - Steph
    - Added a logarithmic function that showed daily flow values for the month of November for a given year.

4) A summary of your forecast. This should be written as a narrative summary without any blocks of code. It should summarize the inputs and approach used and must include at least 1 map and 1 graph. Only include graphs that you talk about in your narrative.
  - The USGS daily streamflow data values were coded into a Pandas Dataframe using a URL link where they were then resampled to extract only the November flow. The November flow averages for each year in the dataset were then plotted to see if there were any outliers within the data. The plot showed that the flow values before 2005 were extremely high in comparison to the rest of the values. The flow data was then modified to reflect values after 2005. Hierarchical data was then added to provide outside data that could potentially affect the streamflow values. The precipitation rates and air temperature near the Verde River Watershed were extracted from NetCDF files  using the NOAA PSL website and plotted on graphs. A plot of the streamflow during the previous forecast period (November 7th, 2021 to November 13th, 2021) was also added to see what current trend is occurring at the streamgage. A map of the state of Arizona was also added to the code. This map plotted the state of Arizona, the Verde River/Salt River Boundaries, and important points in the state. Finally, a logarithmic plot of the daily flow values for the month of November for whatever year was desired to be viewed was added in.
