# Create and write to a file (write mode)
file = open("student.txt", "w")
file.write("Name: John Doe\n")
file.write("Class: 10\n")
file.write("Score: 85\n")
file.close()

# Read the file (read mode)
file = open("student.txt", "r")
print("File content after writing:")
print(file.read())
file.close()

# Append new data (append mode)
file = open("student.txt", "a")
file.write("Grade: A\n")
file.close()

# Read again to confirm changes
file = open("student.txt", "r")
print("\nFile content after appending:")
print(file.read())
file.close()

# Update (read and write mode)
file = open("student.txt", "r+")
content = file.read()
file.seek(0)
file.write("Name: Jane Doe\n" + content)
file.close()

# Final check
file = open("student.txt", "r")
print("\nFinal file content after update:")
print(file.read())
file.close()
