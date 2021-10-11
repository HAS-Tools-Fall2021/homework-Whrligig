# %%
# Numpy Array Training Code
    # 1-D Arrays

import numpy as np
import pandas as pd

avg_monthly_precip = np.array([0.70, 0.75, 1.85])
print(avg_monthly_precip)

# %%
# 2-D Arrays

precip_2002_2013 = np.array([
    [1.07, 44, 1.50],
    [0.27, 1.13, 1.72]
])

print(precip_2002_2013)

# %%

test_array = np.random.rand(6,12)

print(test_array)


np.round(np.mean(test_array),3)

np.std(test_array)


np.mean(test_array[:,2])


np.round("Row Averages =", np.mean(test_array, axis =1),2)
np.round("Column Averages =", np.mean(test_array, axis =0),2)


# Practice Dataframe

dataframe = pd.DataFrame(columns=["column_1", "column_2"],
                        data=[
                             [1, 2],
                             [2, 4]
                        ])


# Examples of Making Arrays:
array1 = np.array([
    [1, 2, 3],
    [3, 6, 9]
    ])

array2 = np.zeros(17)

array3 = np.ones(5)

array4 = dataframe.to_numpy()

# Key Attributes

array1.ndim
array3.ndim
array5 = np.array([])

np.insert(array5,0,5)
print(array5)

