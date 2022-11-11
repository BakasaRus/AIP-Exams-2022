for A in range(1, 1000):
    for x in range(1, 1000):
        # f = ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 100)
        f = ((x % 5 == 0) and (x % 13 != 0)) or (x + A >= 10)
        if not f:
            break
    else:
        print(A)
        break
