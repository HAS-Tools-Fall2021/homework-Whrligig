# %%

# Practice with For Loops

list_of_values = [1, 2, 3, 4, 5]

for avalue in list_of_values:
    print(avalue)

for avalue in list_of_values:
    print("the current value is:" , avalue)

for avalue in list_of_values:
    print("the current value is:" , avalue + 1)


num_list = [12, 5, 136, 47]

for i in num_list:
    i += 10
    print(i)

# i is just a placeholder, can be replaced with anything (banana, for example)

for banana in num_list:
    banana *= 25
    print(banana)

# %%

# Practicing While Loops

x = 0

while x < 10:
    x += 1
    print(x)

x = 0

while x < 10:
    print(x)
    x += 1
        
print("Final value:", x)


# %%

# While loops with range limits

x = 1

while x in range(1,5):
    x += 1
    print(x)
    