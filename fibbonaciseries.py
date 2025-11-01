def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive number.")
    elif n == 1:
        print("Fibonacci sequence:")
        print(a)
    else:
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b

n = int(input("Enter the number of terms: "))
fibonacci(n)
