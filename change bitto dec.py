binary = input("Enter binary number: ")

decimal = 0
for bit in binary:
    decimal = (decimal << 1) | int(bit)

print(decimal)
