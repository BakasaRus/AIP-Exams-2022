for A in range(1, 10000):
    for x in range(1, 50000):
        f = (x % A == 0) <= ((x % 15 == 0) or (x % 23 != 0)) and (x + A >= 150)
        if not f:
            break
    else:
        print(A)
        break
