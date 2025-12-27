# Program to find the Least Common Multiple (LCM) of two numbers

def lcm(a, b):
    # LCM using GCD
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    return (a * b) // gcd(a, b)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM of", num1, "and", num2, "is", lcm(num1, num2))
