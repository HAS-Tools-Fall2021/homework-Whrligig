# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Create a basic dataframe
dataframe_1=pd.DataFrame(columns=["Precip_mm", "ET_mm"],
                                data=[
                                        [0.3, 0.7],
                                        [0.2, 0.5],
                                        [0.2, 0.9]
                                ])

