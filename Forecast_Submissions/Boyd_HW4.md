### Connal Boyd
###### Homework #4
###### 09/20/21

______________
## Grade
3/3 - Great work! Seems like things are pushing to the right branch now so I think we are good. 
______________
Quantiles (for all flows):

    10th: 61.77 cfs
    25th: 93.5 cfs
    50th: 157.0 cfs
    90th: 462.6 cfs

1.) My one week forecast for 09/19-09/25 is 88 cfs. Looking at the histograms
submitted with the homework code, the flow is highest between 0 and 200 cfs. A
closer look between 0 and 100 cfs shows that flows between 50 and 100 cfs
are common. Since last week's average flow value almost exactly matched the
25th quantile flow, it makes sense to estimate flows around this value.
Previous flows showed declining flow averages week by week, so a decline
from this week to next week would not be unexpected. The monsoon season is
drawing to a close, however, so it would make sense that rains would become
more infrequent in coming weeks. This could lead to a less drastic decrease between weekly flow averages than in
previous weeks. Since the histograms show that the average lies between 50
and 100 cfs, and the previous week average was near the 25th percentile for all flows, an estimate of 88 cfs for the next week and 85 for the
week after are conservative guesses.

Avg for 3 weeks ago: 157.3 cfs

Avg for 2 weeks ago: 112.6 cfs

Avg for 1 week ago: 93.7 cfs


2.) Flow_data is a numpy array. It contains float data types. It has two dimensions and its shape is (11948, 4). This means it has 11948 rows and 4 columns.

3.)

Number of times flow was greater than 88 cfs in September was 734 times.
Of those times, the average flow was 204.5 cfs.
Percent of time flow was higher than prediction was 75.1% of the time.

Number of times flow was greater than 85 cfs in September was 768 times.
Of those times, the average flow was 199.3 cfs.
Percent of time flow was higher than prediction was 78.6% of the time.

Total number of flows in September = 977 times

4.)

Number of times flow was greater than 88 cfs in September, in or before 2000 was 321 times.
Of those times, the average flow was 234.7 cfs.
Total flows in September in or before 2000 was 360 times.
Percent of time flow was higher than prediction was 89.2% of the time.

Number of times flow was greater than 88 cfs in September, in or after 2010 was 231 times.
Of those times, the average flow was 161.7 cfs.
Total flows in September in or after 2010 was 347 times.
Percent of time flow was higher than prediction was 66.6% of the time.

Number of times flow was greater than 85 cfs in September, in or before 2000 was 325 times.
Of those times, the average flow was 232.9 cfs.
Total flows in September in or before 2000 was 360 times.
Percent of time flow was higher than prediction was 90.3% of the time.

Number of times flow was greater than 85 cfs in September, in or after 2010 was 247 times.
Of those times, the average flow was 156.8 cfs.
Total flows in September in or after 2010 was 347 times.
Percent of time flow was higher than prediction was 71.2% of the time.

5.) There is a decrease of about 10 cfs from the first half to the second half
of September. The average flow for the first half of September is 176.6 cfs, historically.
The average flow for the second half of September is 166.7 cfs.
