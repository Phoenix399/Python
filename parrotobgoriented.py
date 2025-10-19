#create class
class parrot:

    #class atribute
    species = "bird"

    #instances attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

        #instanciate the parrot class
blu = parrot("Blu", 10)
woo = parrot("Woo", 15)

#access the class attributes
print("Blu is a " , blu.species)
print("Woo is also a ", woo.species)

#access the instances attributes
print(blu.name, " is ", blu.age, " years old")
print(woo.name, " is ", woo.age, " years old")