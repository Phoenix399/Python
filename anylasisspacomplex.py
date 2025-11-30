# T(n) = 2T(n/2)

def prints(n):
    if n <= 0:      
        return
    print("Codingal")

n = int(input("Enter a number: "))
prints(n / 2)
prints(n / 2)
