def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0

    return f(start + 1, end) + f(start * 2, end)


result = (f(3, 18) - f(3, 12) * f(12, 18)) * f(18, 55)
print(result)
