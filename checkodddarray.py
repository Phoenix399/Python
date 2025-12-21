def OddOccuring(arr):
    # Initialize result
    res = 0

    # Traverse the array
    for element in arr:
        # XOR with the result
        res = res ^ element

    return res


# Initialize our array
arr = []

# Take array size as input
n = int(input("Enter array size: "))

# Take array element input
while n:
    num = int(input("Enter number: "))
    arr.append(num)
    n -= 1

# Print result
print("\nOdd occurring number is:", OddOccuring(arr))
