def f(start, end):
    if start == end:
        return 1
    if start > end:
        return 0

    return f(start + 1, end) + f(start * 3, end) + f(start * 4, end)


print(f(1, 25))
