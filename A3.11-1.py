for x in range(150_000_000, 300_000_000 + 1):
    _x = x
    n, m = 0, 0

    while x % 2 == 0:
        x //= 2
        m += 1

    if m % 2 != 1:
        continue

    while x % 3 == 0:
        x //= 3
        n += 1

    if n % 2 != 0:
        continue

    if x == 1:
        print(_x, m + n)
