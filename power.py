def power2(number):
    # 0 is not a power of 2
    if number == 0:
        return 0

    # A power of 2 has only one set bit
    if (number & (number - 1)) == 0:
        return 1
    else:
        return 0


number = int(input("Enter the number: "))

if power2(number):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")
