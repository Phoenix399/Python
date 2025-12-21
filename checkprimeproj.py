# Return True if n is prime else False (only for 2-digit numbers)
def isPrime2Digit(n):
    # check if number is 2-digit
    if n < 10 or n > 99:
        return None

    # 2-digit prime check
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


number = int(input("Enter a 2-digit number: "))

result = isPrime2Digit(number)

if result is None:
    print("Not a 2-digit number")
elif result:
    print(number, "is Prime")
else:
    print(number, "is Not Prime")

