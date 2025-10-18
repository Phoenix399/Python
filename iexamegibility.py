from datetime import datetime

# Ask the user for their date of birth
dob_input = input("Enter your date of birth (YYYY-MM-DD): ")

# Change the text (string) into a date
dob = datetime.strptime(dob_input, "%Y-%m-%d")

# Get today's date
today = datetime.today()

# Work out the user's age
age = today.year - dob.year
if (today.month, today.day) < (dob.month, dob.day):
    age -= 1  # subtract 1 if birthday hasn’t come yet this year

# Show the result
print("You are", age, "years old.")

# Check exam eligibility
if age >= 18:
    print("You can take the exam.")
elif age >= 15:
    print("You can take the exam with permission.")
else:
    print("You are not old enough to take the exam.")
