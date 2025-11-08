# Create a sample file
file = open("data.txt", "w")
file.write("Python is fun!\nLearning file handling.\nKeep practicing daily.")
file.close()

# 1. Read the entire file at once
file = open("data.txt", "r")
print("Reading full file using read():")
print(file.read())
file.close()

# 2. Read line by line using readline()
file = open("data.txt", "r")
print("\nReading line by line using readline():")
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline())
file.close()

# 3. Read all lines into a list using readlines()
file = open("data.txt", "r")
print("\nReading all lines using readlines():")
lines = file.readlines()
print(lines)
file.close()

# 4. Read using a for loop
file = open("data.txt", "r")
print("\nReading file using a for loop:")
for line in file:
    print(line.strip())
file.close()
