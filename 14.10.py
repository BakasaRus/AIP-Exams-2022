# F(n) = n ** 2 + 2 * n + 1 + F(n - 3) + F(n // 2) if n > 1
# F(n) = n ** 2 otherwise
def f(n):
    if n > 1:
        return n ** 2 + 2 * n + 1 + f(n - 3) + f(n // 2)
    else:
        return n ** 2


def F(n):
    print(n * n)
    if n > 1:
        print(2 * n + 1)
        F(n - 3)
        F(n // 2)


for n in range(10000):
    s = f(n)
    if s > 3_300_000:
        print(n, s)
        break
