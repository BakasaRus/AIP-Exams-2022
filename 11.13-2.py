def f(start, end):
    if start == end:
        return 1
    if start > end or start == 25:
        return 0

    return f(start + 1, end) + f(start * 2, end)


result = f(2, 14) * f(14, 29)
print(result)
