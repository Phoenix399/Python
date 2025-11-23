def multiply_once(a, b):
    return a * b   # O(1)

def multiply_loop(a, b):
    total = 0
    for i in range(a):   # O(N)
        total += b
    return total

# Example
a = 5
b = 3

print("O(1) multiplication:", multiply_once(a, b))
print("O(N) multiplication:", multiply_loop(a, b))
