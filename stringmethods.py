name = input("Enter your full name: ")



print("Original Name:", name)

# Common string methods:
print("Length of name:", len(name))
print("First position of 'a':", name.find("a"))         # Finds first 'a'
print("Is all alphabetic?", name.isalpha())             # Only true if no spaces
print("Is alphanumeric?", name.replace(" ", "").isalnum())  # Removes space first
print("Is lowercase?", name.islower())
print("Is uppercase?", name.isupper())
print("Name in lowercase:", name.lower())
print("Name in uppercase:", name.upper())
print("Name capitalized:", name.capitalize())
print("Name title case:", name.title())                 # Capitalizes each word
print("Name reversed:", name[::-1])                     # Slicing to reverse
print("Name starts with 'N'?", name.startswith("N"))
print("Name ends with 'i'?", name.endswith("i"))
print("Replace spaces with underscores:", name.replace(" ", "_"))
print("Count of 'a':", name.count("a"))
print("Name with no leading/trailing spaces:", name.strip())
print("Split name into list:", name.split())
