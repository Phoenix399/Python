#Programe to count number of lines in this file
#Opening a file
file =open("Codingal.txt",'r')
Counter=0

#Reading each line from file
Content = file.read()
#Splitting the content based on new line character
#and storing the lines in a list
Lines = Content.split("\n")

for i in Lines:
    if i:

        Counter+=1
print("Number of lines in the file:",Counter)