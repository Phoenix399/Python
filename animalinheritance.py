# import necessary packages
from abc import ABC, abstractmethod

# Define the base class Animal
class Animal(ABC):

    @abstractmethod
    # should be implemented by all subclasses
    def move(self):
        pass


# Subclasses
class Human(Animal):
    def move(self):
        print("Humans can walk and run.")


class Snake(Animal):
    def move(self):
        print("Snakes can crawl.")


class Dog(Animal):
    def move(self):
        print("Dogs can bark and run.")


class Lion(Animal):
    def move(self):
        print("Lions can roar and run.")


# Example usage:
h = Human()
s = Snake()
d = Dog()
l = Lion()

h.move()
s.move()
d.move()
l.move()
