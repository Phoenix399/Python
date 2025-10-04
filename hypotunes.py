import math

a = float(input("Enter side A:  "))
b = float(input("Enter side B:  "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f"The length of the hypotenuse is: {c}")