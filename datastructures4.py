#Empty tuple
my_tuple = ()
print(my_tuple)

#Tuple with integers
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

#Tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)


#Accesing tuple elements using indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0])    # First element
print(my_tuple[5])    # Last element

#Tuple with nested tuples
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

#Nested indes
print(my_tuple[0][3])        # Output: s
print(my_tuple[1][1])        # Output: 4

#Slicing
print("Sliced :", my_tuple[1][1:4])   # Output: [4, 6]

#Iterating through a tuple
for letter in (my_tuple):
    print("Here is :", letter)