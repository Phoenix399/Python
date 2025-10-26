class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print("First Name:", self.fname)
        print("Last Name:", self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year


x = Student("John", "Doe", 2023)
x.display()
print("Graduation Year:", x.year)
