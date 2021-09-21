# %%
# Numpy Array Training Code
    # 1-D Arrays

import numpy as np

avg_monthly_precip = np.array([0.70, 0.75, 1.85])
print(avg_monthly_precip)

# %%
# 2-D Arrays

precip_2002_2013 = np.array([
    [1.07, 0.44, 1.50],
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