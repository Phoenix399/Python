# Return True if n is even else False (only for 2-digit numbers)
def isEvenOdd(n):
    # check if number is 2-digit
    if n < 10 or n > 99:
        return None

    # XOR with 1 equals n+1 for even numbers
    if (n ^ 1) == n + 1:
        return True
    else:
        return False


number = int(input("Enter a 2-digit number: "))

result = isEvenOdd(number)

if result is None:
    print("Not a 2-digit number")
elif result:
    print(number, "is Even")
else:
    print(number, "is Odd")
