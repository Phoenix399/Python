# Return True if n is even else False
def isEvenOdd(n):
    # XOR with 1 equals n+1 for even numbers
    if (n ^ 1) == n + 1:
        return True
    else:
        return False


number = int(input("Enter your number: "))

if isEvenOdd(number):
    print(number, "is Even")
else:
    print(number, "is Odd")
