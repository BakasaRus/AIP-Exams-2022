def F(n):
    if n <= 3:
        return n
    elif n > 3 and n <= 32:
        return n // 4 + F(n - 3)
    else:
        return 2 * F(n - 5)


print(F(100))
