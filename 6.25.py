for A in range(1000, 0, -1):
    for x in range(1, 1000):
        f = (x % A != 0) <= ((x % 14 != 0) and (x % 21 != 0))
        if not f:
            break
    else:
        print(A)
        break
