## Group 2 -- Connal Boyd, Andrew Hoopes, Stephanie Serrano, Zhang Xingyu

1 Wk Forecast:156.1

2 Wk Forecast:134.9

3.) A brief summary of your collaboration. What did each team member bring to the table, who did what and how did you decide how to combine things?

Connal:[]

Andrew:[]

Xingyu: Download reanalysis data. Merge the data into one dataframe and normalize it. Calculate the forecast. Write part of the Readme file

Stephanie:[]



4.) A summary of your forecast. This should be written as a narrative summary without any blocks of code. It should summarize the inputs and approach used and must include at least 1 map and 1 graph. Only include graphs that you talk about in your narrative.

1. data: 
1.1the streamflow data before 2021 Nov 11, downloaded from the USGS web.
1.2the precipitaion rate data in 1989 Jan 1st to 2021 Nov 11th, downloaded from the PSl web, averaged by time.
1.3 the air temperature data in 1989 Jan 1st to 2021 Nov 11th, downloaded from the PSl web, averaged by time.
(1.1 downloaded by Connal, 1.2 and 1.3 data downloaded by Xingyu)

2. Correct the data: becuase the flow data has a great peak in 2005, we cannot use a long time series. Because the linear regression algorithm may be overfitted if the sample time is too lang, I droped the time before 2020. Although the latitude and longitude of precipitation and air temperatrue are different, we can make an average of the whole region(33-37N,246-250E). After that, I merge the streamflow data, precipitation data and the air temperature data into one dataframe. The precipitaiton and air temperature data should be normalinzed(minus mean and devided by std). 

3. Calculate the forecast: resample the data into weekly. the use the precipitation, air temperature and last week flow to train the model. The coefficient of determination is 0.64, so that this model fitted well. In this way, the forecast = 156.1 and 134.9, respectively.

4. plot[]

5.  map[]


