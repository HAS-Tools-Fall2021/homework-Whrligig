# %%

# Arithmetic Operators

a = 2
b = 3

a + b

b - a 

b / a 

a * b

# Exponents:

a ** b

# Can use for conversion of units:

jan_precip_in = 0.70
inches_to_mm = 25.4

jan_precip_in * inches_to_mm

# Challenge 1:

march_precip_in = 1.85
inches_to_mm = 25.4

march_precip_in * inches_to_mm

type(march_precip_in)

# %%

# Assignment Operators

jan_precip = 0.70
inches_to_mm = 25.4

jan_precip *= inches_to_mm

jan_precip

# Challenge 2:

annual_avg_precip_nyc = 42.65
dec_avg_precip_nyc = 3.58

annual_avg_precip_nyc += dec_avg_precip_nyc

annual_avg_precip_nyc

# %%

# Relational Operators

type(True)

3 < 4

3 > 4

3 == 3

# This means does not equal
3 != 4 

3 <= 4

3 <= 3

3 >= 4

is_greater = (3 > 2)

# Example

rainfall = 3
if rainfall > 2:
    print("Baby Beluga")

# %%

# Membership Operators

precip = "Precipitation"
"Precip" in precip

temp_1 = [70, 68, 74]
68 in temp_1
69 not in temp_1

# %%

# Logical Operators

temp_1 = [70, 68, 74]
68 in temp_1 and 70 in temp_1
68 in temp_1 and 69 in temp_1

68 in temp_1 or 70 in temp_1
68 in temp_1 or 69 in temp_1

# %%

# Identity Operators

temp_1
temp_2 = [70, 68, 74]

temp_3 = temp_1

temp_1 is temp_3

temp_1 == temp_2

temp_1 is not temp_2

is_the_same = (temp_1 is temp_2)

is_the_same

# Challenge 3: 

# relational = (3 <= 2)

relational = (3 >= 2)
print (relational)

# identity = (4 is 3)

identity = (4 is 4)
print(identity)

membership = (72 not in temp_1)
print(membership)

temp_1 = [70, 68, 74]
logical = (68 in temp_1 and 69 not in temp_1)
print(logical)
