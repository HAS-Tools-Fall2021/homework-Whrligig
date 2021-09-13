### Connal Boyd
##### 09/13/21
##### HW #3

The average for last week's flow was much lower than I predicted, only about 115 cfs.
As a result, I have lowered my one and two week predictions this week even further than in previous weeks.
My one week prediction is only 96 cfs, and my two week prediction is 84 cfs.

###### Describe the variables flow, year, month, and day. What type of objects are they? What data types are they composed of? How long are they?

The variables flow, year, month, and day are all lists. The flow list contains floats, and all the others contain integer data types. Each list is 11941 items long.

###### How many times was the daily flow greater than your prediction in the month of September (express your answer in terms of the total number of times and as a percentage)?

The number of times in the historical record that the daily flow was greater than my one week prediction in the month of September was 645 times.
This means about 5.4% of the values were larger than my prediction.
The number was higher for my two week prediction, with 732 values greater than my prediction in the month of September. This indicates about 6.1% of the flow values were greater than my two week prediction.

###### How would your answer to the previous question change if you considered only daily flows in or before 2000? Same question for the flows in or after the year 2010? (again report total number of times and percentage)

The total number of times daily flow was greater than my one week prediction is 299 times.
The percentage of values larger than my one week prediction in or before 2000 is 6.8%.
For my two week prediction 328 values were larger.
This means about 7.5% of the flow values before 2000 were larger than my prediction.
For flows after 2010, 220 or 5.2% of flows were larger than my one week prediction.
For my two week prediction, 462 or 10.8% of flows were larger.

###### How does the daily flow generally change from the first half of September to the second?

The mean daily flow for the first half of September for the dataset is about 150.7 cfs, whereas the second half of September is somewhat higher at 188.7 cfs.
This is an increase of about 38 cfs over the span of a couple weeks from the first half to the second half.


Copy of my code seen below:

# %%

# Forecast 3 Code

print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))


# 1 week prediction: 96
# 2 week prediction: 84


if type(flow[27]) is int:
        print("is an integer")
elif type(flow[27]) is str:
        print("is a string")
elif type(flow[27]) is float:
        print("is a float")

len(flow)

if type(year[27]) is int:
        print("is an integer")
elif type(year[27]) is str:
        print("is a string")
elif type(year[27]) is float:
        print("is a float")

len(year)

if type(month[27]) is int:
        print("is an integer")
elif type(month[27]) is str:
        print("is a string")
elif type(month[27]) is float:
        print("is a float")

len(month)

if type(day[27]) is int:
        print("is an integer")
elif type(day[27]) is str:
        print("is a string")
elif type(day[27]) is float:
        print("is a float")

len(day)


#####################################

ilist = []      

for i in range(len(flow)):
        if flow [i] > 96 and month[i] == 8:
                ilist.append(i)

print(len(ilist))

jlist = []

for i in range(len(flow)):
        if flow [i] > 84 and month[i] == 8:
                jlist.append(i)

print(len(jlist))


######################################

klist = []

for i in range(len(flow)):
        if flow[i] > 96 and month[i] == 8 and year[i] <= 2000:
                klist.append(i)

print(len(klist))

mlist = []

for i in range(len(flow)):
        if flow[i] > 84 and month[i] == 8 and year[i] <= 2000:
                mlist.append(i)

print(len(mlist))


# The number of flow values between January 1st, 1989 and December 31st, 2000
# is 4382, but I could not figure out how to write a code to find this number.
# I just calculated it from the text file instead.

nlist = []

for i in range(len(flow)):
        if flow[i] > 96 and month[i] == 8 and year[i] >= 2010:
                nlist.append(i)

print(len(nlist))

olist = []

for i in range(len(flow)):
        if flow[i] > 84 and month[i] == 8 and year[i] >= 2000:
                olist.append(i)

print(len(olist))

# The number of flow values between January 1st, 2010 and September 13th, 2021
# is 4270, but I couldn't figure out how to write a code to find this number.
# I just calculated it from the text file instead.

ilist2 = [i for i in range(len(flow)) if month[i]==8 and day[i] <= 14]

subset = [flow[j] for j in ilist2]

print(np.mean(subset))



ilist3 = [i for i in range(len(flow)) if month[i]==8 and day[i] >= 15]

subset = [flow[j] for j in ilist3]

print(np.mean(subset))
