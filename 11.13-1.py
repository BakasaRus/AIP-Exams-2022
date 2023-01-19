def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0

    return f(start + 1, end) + f(start * 2, end)


result = f(2, 14) * (f(14, 29) - f(14, 25) * f(25, 29))
print(result)
