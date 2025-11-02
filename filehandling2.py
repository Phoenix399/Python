#open the file in read mode
file_read = open("Codingal.txt", 'r')

print("File in read mode")
#read the content of the file
print(file_read.read())

#close the file
file_read.close()

#open the file in write mode
file_write = open("Codingal.txt", 'w')

#write in the file
file_write.write("File in write mode...")
file_write.write("Hi I am a Penguin. I am 1yr old.")
file_write.close()

#open the file in append mode
file_append = open("Codingal.txt", 'a')
#append in the file
file_append.write("\nFile in append mode...")
file_append.write("Hi I am a Penguin. I am 1yr old.")
file_append.close()