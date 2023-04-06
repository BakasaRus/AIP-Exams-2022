def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0

    return f(start + 1, end) + f(start * 2, end)


result = f(5, 8) * (f(8, 60) - f(8, 22) * f(22, 60))
print(result)
