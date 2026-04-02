
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)



term = lambda x, n: (x ** n) / factorial(n)

def exp_x( x, n):
    result = 0
    i = 0
    while i < n:
        result += term(x, i)
        i += 1
    return result



x = float(input("x: "))
n = int(input("n: "))

print("e^x ≈", exp_x(x, n))