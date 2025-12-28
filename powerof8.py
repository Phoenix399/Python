def powerof8(number):
    # 0 is not a power of 8
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

    # For power of 8, count must be a multiple of 3
    if count % 3 == 0:
        return True
    else:
        return False


number = int(input("Enter your number: "))

if powerof8(number):
    print(number, "is a power of 8")
else:
    print(number, "is not a power of 8")
