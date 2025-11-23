print("first function")
def fun1(n):
    iterations = 1
    result =n*(n+1)/2
    return result, iterations
result, iterations = fun1(4)
print("(sum , iteration) = ",fun1(4))
print("second function")
def fun2(n):
    sum = 0
    iterations = 0
    for i in range(1,n+1):
        sum += i
        iterations += 1
    return sum, iterations
result, iterations = fun2(4)
print("(sum , iteration) = ",fun2(4))
print("third function")
def fun3(n):
    iteration = 0
    sum = 0
    for i  in range(1,n+1):
        for j in range(1,i+1):
            sum += 1
            iteration += 1    
    return sum, iteration
result, iteration = fun3(4)
print("N(sum , iteration) = ",fun3(4))