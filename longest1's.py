def longest_consecutive_ones(n):
    count = 0
    while n != 0:
        n = n & (n << 1)
        count += 1
    return count

# Example
num = 29  # Binary: 11101
print("Longest consecutive 1's:", longest_consecutive_ones(num))
