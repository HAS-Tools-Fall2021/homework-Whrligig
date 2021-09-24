# %%

# Testing Lists

boulder_precip_in = [0.70, 0.75, 1.85]

months = ["January", "February", "March", "May"]


jan = 0.70

boulder_avg_precip = [1, jan, "january"]


# %%
# Testing Indexing

months = ["January", "February", "March", "May"]

months[:3]



# %%

# Testing object type of a function

type(boulder_avg_precip)

# %%

len(months)

# It can help to include len( ) as part of a print( ) output

print("The length of the months list is:", len(months))

# Challenge 1:

precip_by_location = [46.23, "inches", "New York City"]

precip_by_location[2]

# %%

# Updating an index value

boulder_precip_in[1] = 0

# Insert an item into a list

months.insert(3,"April")

months[3]

print(months)

# Delete an item from a list

del months[4]

print(months)

# Add an item to the END of a list

months.append("May")

print(months)

# Adding items to a list in another way

boulder_precip_in = [35.0] + boulder_precip_in

boulder_precip_in



#Challenge 2:

precip_by_location = [46.23, "inches", "New York City"]

precip_by_location.insert(0,1)

precip_by_location[1] = 20.23

precip_by_location[3] = "Boulder"

precip_by_location.append("Colorado")

print(precip_by_location)


# Challenge 3:

list_of_lists = [[1,2,3],[8,9,10]]

list_of_lists[0]

type(list_of_lists[0])

# Challenge 4:

list_of_lists[0][1]

list_of_lists[1][2]

# %%
