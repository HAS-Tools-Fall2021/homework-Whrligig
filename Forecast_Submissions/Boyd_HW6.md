### Connal Boyd

#### HW #6
#### 10/03/21

1 Week: 180 cfs, 
2 Week: 174 cfs

Last week's flow showed an increase in the flow as the week went on, as seen below.

![picture 14](../../../images/d6d89bb2094c4ba95047fb619eaeac4e1b932f1720924f5794a5f58a77136a87.png)  


I used data from the whole dataset to create this plot, but set limits along the x axis to only capture the window of time I wanted to look at.
I wanted to see what kind of trend last week's flow would follow.
I then looked at what the previous five years' trends looked like for flows in September and October as seen below.

![picture 16](../../../images/b68b622514aa9bbb4e396bfdf07cb9c67eccf2afb2f5c66249ed220c99ac9809.png)  
![picture 17](../../../images/43e854b9458e838d662cff725448b3aca3329ff9c7cfbd73bb37a0e973628729.png)  


These showed that this year's September flow pretty closely followed the 2017 flow for much of the middle of the month, 
but the ends of the month had much higher flow trends.
Flow has been higher over the last couple of weeks than for the same time period in the last five years.
October flows generally fall along the same trajectory of flows in the 100s cfs.
I used the same for loop structure to create both of these graphs. This helped to pull data iteratively from each year I wanted to graph instead of trying to graph each year individually.
I then used a scatter plot to see if there was any correlation between September 2017 and September 2021 flow values. I had hoped this would narrow my prediction values for the next couple of weeks. However, if the two datasets were more strongly correlated then they would follow a more strongly 1:1 linear path. This is missing in the plot so this graph was not very helpful in the end.

![picture 18](../../../images/b36e27adb3eddf9be1c6d411f14e4c65339057477a3e6c57264cc2a5193ba2b0.png)  
  
Next I used a boxplot to determine how much error there is around September and October average flow values.
This plot shows that October has a much smaller spread than September, but both are pretty good in terms of accuracy around the mean value.
This indicates that as the months go on, our predictions could trend closer and closer toward the historical averages since there is less error around those values in the dataset near the end of the year (see below).

![picture 19](../../../images/308e7f8b1822423cd412a025510cd47a0ff083b3f6a5d9a6ca102e44e981a846.png)  
 
The historical values for the last 5 years for this week's forecast window shows that the flow was generally between 60 and 130 cfs (excluding 2018 flows). 
Flow in 2018 was much higher than any of the other years, and this made the first graph more difficult to read.

![picture 20](../../../images/cdf65cca81283ef1a5ea123aaddf9c3d10938c78cb3bd3081e2dd81677a29f56.png)  
 
Since flow was much higher last week than expected, I generated a histogram plot to compare September flows to October flows for the whole dataset.
Overall, flows most often occur in September at a little less than 200 cfs.
In October this number is slightly higher than 200 cfs, likely around 215 cfs or so.

![picture 21](../../../images/84f6a50b233dabf52ddd6ad460938b45f8267fef3fd38a0c56af83a64a401f6e.png)  
 
As a result of the information that all of these graphs show me, I predicted that the 1 week flow will be 180 cfs. This is slightly lower than the whole month's average of 200 some cfs. I also predicted a lower 2 week prediction of 174 cfs since I wanted to be conservative in my estimation.