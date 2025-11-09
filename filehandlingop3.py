#create a new file
new_file = open("New_file.txt", "x")
new_file.close()


#check if file exists 
import os
print("Checking if 'my_file.txt' exists or not...")
if os.path.exists("my_file.txt"):
    print("'my_file.txt' exists.")
else:
    print("'my_file.txt' does not exist.")

    #create a new file if it does not exist
    my_file = open("my_file.txt", "w")
    my_file.write("This is a newly created file.")
    my_file.close()

    #delete file named codingal
    os.remove("Codingal3.txt")