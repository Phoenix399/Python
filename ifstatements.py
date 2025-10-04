age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up.")
elif age < 0:
    print("You cannot be younger than 0 years old.")
else:
    print("You are not old enough to sign up.")
