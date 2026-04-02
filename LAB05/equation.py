S = 0

def func(n):
    global S

    if n == 0:
        return

    func(n - 1)

    if n % 2 == 1:
        S += 1 / n
    else:
        S -= 1 / n

n = int(input("n: "))
func(n)
print(S)