#### Instructions for Running Boyd_HW7.py
#### HW #7
##### Connal Boyd

1.) Hello and welcome! Good luck with this code and thank you for reviewing it for me.

2.) This code was written to run with 6 days of last week's forecast flow data. I will be checking starting early Saturday morning 10/09/21 to download the streamflow data so that you can get started as soon as you want to. I will download the data no later than 10:00 am.

3.) Please insert values generated by the code starting from here on.

Average flow for the past 6 days of the forecast period:

(please replace zero with the output from the code)

flow = 179.666667 cfs


Summary statistics for all October flows 1989-2021: (please replace each zero with the value generated by the code)

    count  1000
    mean   144.4368
    std    110.307682
    min    59.8
    25%    105
    50%    124
    75%    153
    max    1910

4.) Please insert plots generated by the code.

Observed Flow for Week 10/03/21-10/08/21:

This plot has been saved automatically as "Wk6_Obs.png" in the file titled "images" within "Forecast_Submissions." Utilize the VSCode plugin we installed to copy the plot from its file into this markdown.

![picture 1](../../images/d034ea823005d5e5f879cd73c39dbe243128e63b9ed3d608d8c7307c35e31bd8.png)  


1 Week Forecast Window 5 Year History Plot:

I could not figure out how to properly save this plot individually as it is set up in a function, so you will have to save it from within VSCODE. Please save it within the file titled "images" within "Forecast_Submissions." See the following path: HAS_Tools_Repo_Dump\homework\Forecast_Submissions\images.
Please name this file '1Wk_Past.png'. Then utilize the VSCode plugin we installed to copy the plot from its file into this markdown. p.s. I'm sorry for the hassle.


![picture 4](../../images/fcae85e6d04dd5e557099f9a0d616eae78d317c582b97fe1d84a1f2e25b5311a.png)  


2 Week Forecast Window 5 Year History Plot:

Same issue as previous plot. I could not figure out how to properly save this plot individually as it is set up in a function, so you will have to save it from within VSCODE. Please save it within the file titled "images" within "Forecast_Submissions." See the following path: HAS_Tools_Repo_Dump\homework\Forecast_Submissions\images.
Please name this file '2Wk_Past.png'. Then utilize the VSCode plugin we installed to copy the plot from its file into this markdown. p.s. I'm sorry for the hassle, again.

![picture 5](../../images/2cd7e0fc2c8d9577ce2ec549cc381edd58c9165894c507aa02de4b53abdf603d.png)  


October Flow Histogram:

This plot has been saved automatically as "Oct_Hist.png" in the file titled "images" within "Forecast_Submissions." Utilize the VSCode plugin we installed to copy the plot from its file into this markdown.

![picture 3](../../images/e1e191596ffd2fcce461aca909c49c161ea2ea5bfd2a5fc65869847e7bd4c4b8.png)  


4.) Enter forecast submissions generated by the code.

1 Week Forecast Submission, Week 7:

168 cfs

2 week Forecast Submission, Week 7:

157 cfs

Code Review Rubric: (feel free to delete the rubric after completing your
  review. I leave it up to you on how you prefer to write it!)

Use the following questions to guide your review. At a minimum you should provide (1) a written assessment and (2) a numeric score to each of the three questions listed below. Refer to the rubric for a guide to scoring.

Wherever possible include line numbers and specific pointers. Remember the goal is not just to point out areas that could be improved but to provide your partner ideas for how to do better. For example you might suggest:
- Clever ways to use built-in functionality (when appropriate)
- Simpler ways to implement the same functionality
- General improvements to structure, style, and naming

And of course remember to always be courteous to the person you are reviewing!

Sierra's Notes: 

I sadly could not run the code, but I tried to give feeback!

The script is relatively easy to understand. In the function, all the variables are defined which is very helpful for another user to interpret. The use of the functions was very well done as the user took another step forward and used the functions to creat graphs. I think that lines 135 and 144 are maybe not the most useful code, but could have been useful for the writer to have. This was the only section of code where I wish there were more commenting to know what should be output when run. Other than those lines, the code was very well written and relaively easy to follow. I like how lots of steps were taken to create really nice graphs. The PEP8 style was mostly followed except for a few indentations and spacing, which I do not find an issue of. 

### Questions to consider
1. Is the script easy to read and understand?
 - Are variables and functions named descriptively when useful?
  5/5
 - Are the comments helpful?
  4/5
 - Can you run the script on your own easily?

 - Are the doc-strings useful?
  5/5
  

2. Does the code follow PEP8 style consistently?
 - If not are there specific instances where the script diverges from this style?
5/5

3. Is the code written succinctly and efficiently?
 - Are there superfluous code sections?
4/5
 - Is the use of functions appropriate?
5/5
 - Is the code written elegantly without decreasing readability?
4/5

### Rubric
(Adapted from Kyle Mandli [Intro to Numerical Methods](https://github.com/mandli/intro-numerical-methods))
![](assets/code_review_rubric-ff0ecab3.png)
