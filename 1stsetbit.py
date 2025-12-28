def rightmost_set_bit(n):
    if n == 0:
        return 0
    return (n & -n).bit_length()

# Example
num = 18  # Binary: 10010
print("Position of rightmost set bit:", rightmost_set_bit(num))
