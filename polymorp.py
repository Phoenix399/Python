class Polygon:
    def area(self):
        pass  # base class method

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth
    
class Square(Polygon):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side
    
class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
#Create objects of the display areas
rect = Rectangle(10, 5)
print("Area of Rectangle:", rect.area())

sq = Square(4)
print("Area of Square:", sq.area())

tri = Triangle(6, 3)
print("Area of Triangle:", tri.area())