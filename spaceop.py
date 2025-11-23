def functions1(n):
    iterations = 1
    big_o = "O(1)"
    return iterations, big_o
def functions2(n):
    iterations = 0
    for i in range(1, n + 1 ):
        iterations += 1         
    big_o = "O(n^2)"
    return iterations, big_o
n = 5
print(functions1(n))
print(functions2(n))
