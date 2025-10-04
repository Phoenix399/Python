# Conditional expressions = One-line shortcut for if-else (ternary operator)
# Format: X if condition is true, Y if condition is false

num1 = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "guest"

print("Positive" if num1 > 0 else "Negative")
result = "EVEN" if num1 % 2 == 0 else "ODD"
max_num = a if a > b else b
min_num = a if a < b else b
status = "Adult" if age >= 18 else "Minor"
weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full Access" if user_role == "admin" else "Limited Access"

print("Result:", result)
print("Max number:", max_num)
print("Min number:", min_num)
print("Status:", status)
print("Weather:", weather)
print("Access Level:", access_level)
