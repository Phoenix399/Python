def reverse_binary(n):
    b = bin(n)[2:]
    rb = b[::-1]
    return int(rb, 2)

n = int(input("Enter your original number: "))
print("Reversed Number:", reverse_binary(n))
