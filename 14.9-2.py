from functools import cache


@cache
def F(n):
    if n >= 1:
        return F(n - 1) + F(n - 3) + 2 + 1
    else:
        return 1


# В задаче 40, а не 400
print(F(400))
