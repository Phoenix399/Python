
def powerof4(number):
    # 0 is not a power of 4
    if number == 0:
        return False

    count = 0

    # Check if only one set bit exists (power of 2)
    if (number & (number - 1)) != 0:
        return False

    # Count 0 bits before the set bit
    while number > 1:
        number >>= 1
        count += 1

    # If count is even, it is a power of 4
    if count % 2 == 0:
        return True
    else:
        return False


number = int(input("Enter your number: "))

if powerof4(number):
    print(number, "is a power of 4")
else:
    print(number, "is not a power of 4")
