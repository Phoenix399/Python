from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Square(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

r = Rectangle(10, 5)
t = Triangle(6, 4)
s = Square(7)

print("Rectangle area:", r.area())
print("Triangle area:", t.area())
print("Square area:", s.area())
