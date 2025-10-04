# Logical operators = evaluate multiple conditions
# or = if one of the conditions is true, the result is true
# and = if both conditions are true, the result is true
# not = reverses the result of the condition

# First example
temp = 25
is_raining = False

if temp > 35 or temp < 15 or is_raining:
    print("The outdoor event is canceled.")
else:
    print("The outdoor event will continue as planned.")

# Second example
temp = 25
is_sunny = True

if temp >= 28 and is_sunny:
    print("It's a great day for a picnic!")
else:
    print("Maybe we should stay indoors.")

