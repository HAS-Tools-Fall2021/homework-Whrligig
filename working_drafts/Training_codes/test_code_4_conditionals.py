# %%

# Conditional statements like If/Else

x = 5

if x >= 6:
    print("Spicy Soup")
else:
    print("Bland Soup")

x = 25

if x >= 6:
    print("Spicy Soup")
else:
    print("Bland Soup")

y = 4

if x < y:
    print("x has a value of", x, "which is less than", y)
else:
    print("x has a value of", x, "which is greater than", y)

# Can check for presence of something in a list

avg_monthly_precip = [0.70, 0.75, 1.85, 2.93]

if 0.70 in avg_monthly_precip:
    print("value is in list")
else:
    print("value is not in list")

# Can use conditionals to check for words in strings

"avg_monthly_temp"
type("avg_monthly_temp")
if "precip" in "avg_monthly_temp":
    print("This textstring contains the word precip")
else:
    print("This textstring does not contain the word precip")

# Checking object type using conditionals

x = 0

if type(x) is int:
    print(x, "is an integer")
else:
    print(x, "is not an integer")

if type(x) is float:
    print(x, "is a float.")
else:
    print(x, "is not a float.")

if type(x) is not str:
    print(x, "is not a string")
else:
    print(x, "is a string")

# Can compare types of objects to see if objects are the same type or not

months = ["Jan","Feb","Mar","Apr","May"]

if type(avg_monthly_precip) is type(months):
    print("These objects are the same type")
else:
    print("These objects are not the same type")

# %%

# Using elif statements

x = 5
y = 10

if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")


x = 15

if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")


x = 10

if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")


# %%

# Checking if multiple conditions are true

x = 5
y = 10


if type(x) is int and type(y) is int:
    print(x + y)
else:
    print("Either x or y is not an integer.")


x = 5
y = "Blue fish"

if type(x) is int and type(y) is int:
    print(x + y)
else:
    print("Either x or y is not an integer, so they cannot be added.")