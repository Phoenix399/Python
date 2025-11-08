#open the file in read mode
file_read = open("Codingal1.txt", 'r')
print("File in read mode:")
print(file_read.read())
file_read.close()

#open the file in write mode
file_write = open("Codingal1.txt", 'w')
#write in the file
file_write.write("File in write mode....")
file_write.write("Hi I am a Penguin and I am 1yr old")
file_write.close()

#open the file in append mode
file_append = open("Codingal1.txt", 'a')
#append in the file
file_append.write("\nFile in append mode....")
file_append.write("Hi I am a Penguin and I am 1yr old")
file_append.close()