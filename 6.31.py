for X in range(-1000, 1000):
    ok = True
    for a in range(1, 1000):
        for b in range(1, 1000):
            f = (2 * a + 4 * b > 17) or ((a <= X) and (b < X))
            if not f:
                ok = False
                break
        if not ok:
            break
    else:
        print(X)
        break
