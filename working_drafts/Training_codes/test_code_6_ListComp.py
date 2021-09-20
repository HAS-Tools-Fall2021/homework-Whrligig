# %%

# List comprehension can transform a For Loop into a single line of code

avg_monthly_precip_in = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

[month * 25.4 for month in avg_monthly_precip_in]


# Apply a function to a list

def convert_in_to_mm(num):
    return num * 25.4

[convert_in_to_mm(month) for month in avg_monthly_precip_in]

# Conditionals in list comprehensions

    #If conditionals only:

[month for month in avg_monthly_precip_in if month > 1.5]

    #If else conditionals:

[month * -2 if month > 1.5 else month * 2 for month in avg_monthly_precip_in]