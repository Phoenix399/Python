# Open a file in write mode and create initial content
f = open("student_data.txt", "w")
f.write("Alice - 15\n")
f.write("Ben - 16\n")
f.write("Chris - 14\n")
f.close()

# Read the entire file
f = open("student_data.txt", "r")
print("Full file content:")
print(f.read())
f.close()

# Append new data
f = open("student_data.txt", "a")
f.write("Diana - 17\n")
f.close()

# Read line-by-line
f = open("student_data.txt", "r")
print("\nReading line by line:")
for line in f:
    print(line.strip())
f.close()

# Count lines, words, and characters
f = open("student_data.txt", "r")
text = f.read()
f.close()

lines = text.split("\n")
words = text.split()
chars = len(text)

print("\nStatistics:")
print("Number of lines:", len([l for l in lines if l]))
print("Number of words:", len(words))
print("Number of characters:", chars)

# Copy the file to another file
src = open("student_data.txt", "r")
dest = open("backup.txt", "w")
dest.write(src.read())
src.close()
dest.close()

print("\nFile has been copied to backup.txt")
