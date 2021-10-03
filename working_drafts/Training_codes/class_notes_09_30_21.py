# %%

import numpy as np
import pandas as pd

# Pandas Indexing Exercise 1
# start with the following dataframe of all 1's
data = np.ones((7, 3))
data_frame = pd.DataFrame(data,
                          columns=['data1', 'data2', 'data3'],
                          index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# 1. Change the values for all of the vowel rows to 3

data_frame.iloc[0] = 3

data_frame.loc['e'] = 3

data_frame.loc['banana'] = 3

# 2. Multiply the first 4 rows by 7

data_frame.iloc[0:4] *=7

# 3. Make the dataframe into a checkerboard  of 0's and 1's using loc

# Make a new dataframe for this one, don't just start from where I left off with question 2.

# 4. Same question as 3 but without using loc
