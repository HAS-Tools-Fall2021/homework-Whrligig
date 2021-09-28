### Connal Boyd
##### HW #5
##### 09/26/21

_____
## Grade:
3/3: Nice work. A solution for #5 is posted but feel free to stop by my office hours if you want to walk through debugging your approac. The main issue is that you aren't using your iterator (i) inside your loop anywhere.  
_____

Forecast Prediction:

1 Week: 93 cfs,
2 Week: 90 cfs

The flow for the preceding week was higher than expected. I adjusted my 1 week forecast to a higher value to reflect the current conditions. By looking at summary statistics for all September flows, it can be seen that the flow for last week moved closer to the 50th percentile flow of 118.5 cfs than the 25th percentile flow of 88.6 cfs. My previous estimate was closer to the 25th percentile, but I have adjusted my estimates closer to the 50th percentile value. Therefore my one week estimate is 93 cfs and my two week estimate is 90 cfs.

1.) The column names are 'agency_cd', 'site_no', 'datetime', 'flow', 'code', 'year', 'month', and 'day.' The dataframe's index is the number of rows in the dataframe, or 11954 rows. There is a line of code written into my homework code to determine this as well.

2.) The flow column in the dataframe had the following summary statistics:

Min: 19.0 cfs,
Mean: 340.9 cfs,
Max: 63400 cfs,
Standard Deviation: 1391.2,
Quartiles:

    25%: 93.45 cfs
    50%: 157.0 cfs
    75%: 214.0 cfs


3.)

          Mean(cfs)     Min   Max    St Dev    25%    50%     75%
    Jan: 691.0       158.0    63400   2708.5   201    218.0   285
    Feb: 903.2       136.0    61000   3300.5   200    238     615.8
    Mar: 919.5       97.0     30500   1625.6   178    368     1045
    Apr: 295.6       64.9     4690    540.7    111.3  140     210
    May: 104.4       46.0     546     50.4     77.1   92      117.5
    Jun: 65.5        22.1     481     28.7     48.9   60      76.6
    Jul: 108.4       19.0     5270    219.9    53.5   71      112.5
    Aug: 171.5       29.6     5360    296.0    78.0   116     178
    Sep: 170.9       37.5     5590    282.9    88.6   118.5   169.3
    Oct: 144.1       59.8     1910    110.7    104.8  124     152.3
    Nov: 203.2       117.0    4600    232.2    154.0  174     198
    Dec: 331.9       155.0    28700   1080.4   190.0  203     226

4.)

    5 Highest:
      Year    Month   Flow
      1993    Jan     63400
      1993    Feb     61000
      1995    Feb     45500
      2005    Feb     35600
      1995    Mar     30500

    5 Lowest:
      Year    Month   Flow
      2012    Jul     23.4
      2012    Jun     22.5
      2012    Jun     22.1
      2012    Jul     20.1
      2012    Jul     19.0

5.)  Max and min flows for each month can be found above in question 3, but I struggled with this question and ultimately could not figure out how to code an answer. I did not understand how to code the for loop properly to generate the answer for each month. I kept getting answers that would apply to the whole dataset or to incorrect portions.

6.) There were 1,140 dates that were within 10% of my one week forecast value. For a complete list see my homework code.
