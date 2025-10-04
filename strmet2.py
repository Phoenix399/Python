#validate user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain special characters
#4. username must not contain digits


username = input("Enter your username: ")

# Validate username
if len(username) > 12:
    print("Username must be no more than 12 characters.")
elif " " in username:
    print("Username must not contain spaces.")
elif not username.isalnum():
    print("Username must not contain special characters.")
elif any(char.isdigit() for char in username):
    print("Username must not contain digits.")
else:
    print("Username is valid.")