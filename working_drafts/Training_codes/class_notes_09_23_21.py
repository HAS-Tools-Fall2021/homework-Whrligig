# %%
# Find largest integers <= x1/x2 where x1 = all int 1-10 x2 = 1.3
import os
import pandas as pd
import numpy as np

# Step 1
x1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 2
x2=1.3

x3 = x1//x2 # the double slash rounds down to the decimal

np.max(x3)

np.max(np.floor(x1/x2))

answer = (x1/x2).astype(int)

# 10 numbers divided by one number
