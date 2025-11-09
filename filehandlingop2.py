#write in file using()function
with open("Codingal3.txt", 'w') as file:
    file.write("Hi I am a Penguin. I am 1yr old.")
file.close

#split file into words
with open("Codingal3.txt", 'r') as file:    
    data = file.readlines()
    for line in data:
        words = line.split()
        print(words)
file.close()
