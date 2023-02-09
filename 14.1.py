def F(n):
    if n > 2:
        print(n)
        F(n - 3)
        F(n - 4)


# 33
F(10)
