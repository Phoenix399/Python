#open the file and read its content
file = open("Codingal1.txt", 'r')
print(file.read())
file.close()

#open the file and read its beginning 8characters
file = open("Codingal1.txt", 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age to the file
file = open("Codingal1.txt", 'a')
file.write("Hi I am a PEnguin and I am 1yr old")
file.close()