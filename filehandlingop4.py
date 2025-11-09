#Program to eliminate repeated lines from a file

#creating the output file
outputFile = open("UpdatedFile.txt", "w")

# Read the input file
inputFile = open("Repeated.txt", "r")



# Holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines from the file...")

# Iterate through each line in the input file
for line in inputFile:
    # Check if line is unique
    if line not in lines_seen_so_far:
        outputFile.write(line)  # Write unique line
        lines_seen_so_far.add(line)  
        # Close both files
inputFile.close()