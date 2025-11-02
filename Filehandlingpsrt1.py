#open the file and store the file object in a variable
file = open("Codingal.txt", 'r')

#read the content of the file
print(file.read())

#close the file
file.close()
